import numpy as np
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the monthly data from an Excel file
df = pd.read_excel('monthly_passengers.xlsx', sheet_name='Sheet1')
df['Month'] = pd.to_datetime(df['Month'])
df.set_index('Month', inplace=True)

# Convert index to period since SARIMAX requires a PeriodIndex for seasonal data
df.index = df.index.to_period('M')

# Calculate decay factor using data up to a point for a linear trend
# Assuming the last month of 2019 is the cutoff point for pre-COVID data
cutoff = pd.Period('2019-12', freq='M')
train_data = df[df.index <= cutoff]
X_train = np.arange(len(train_data)).reshape(-1, 1)
y_train = train_data['Total Passengers'].values
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

# Predict passenger numbers for months after the cutoff point
X_future = np.arange(len(train_data), len(df)).reshape(-1, 1)
y_pred = lin_reg.predict(X_future)

# Calculate decay factor
actual = df[df.index > cutoff]['Total Passengers'].values
decay_factor = actual / y_pred

# Insert decay factor into DataFrame
df['Decay'] = 1  # Default to 1 for months without decay
df.loc[df.index > cutoff, 'Decay'] = decay_factor

# Create a binary variable to represent the impact of COVID-19
df['COVID19'] = ((df.index > cutoff) & (df.index.year <= 2024)).astype(int)

# Fit the SARIMAX model with COVID-19 and decay factor as exogenous variables
exog = df[['COVID19', 'Decay']]
model = SARIMAX(df['Total Passengers'], exog=exog,
                order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))  # Assuming a yearly seasonality
results = model.fit()

# Predict future passenger numbers without considering COVID-19 after 2024
# This creates a range of periods for the next 10 years at a monthly frequency
exog_forecast = pd.DataFrame({
    'COVID19': [0] * 120,  # Extend for 10 years with monthly frequency
    'Decay': [1] * 120  # Assuming no decay after 2024
}, index=pd.period_range(start=df.index[-1] + 1, periods=120, freq='M'))

# Forecast for the next 10 years
forecast = results.get_forecast(steps=120, exog=exog_forecast)
forecast_df = forecast.conf_int(alpha=0.05)  # 95% confidence interval
forecast_df['forecast'] = forecast.predicted_mean

# Round the forecast to the nearest whole number
forecast_df['forecast'] = forecast_df['forecast'].round()

# Save forecast to CSV
forecast_df.to_csv('forecast_10years_V2.csv')

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(df.index.to_timestamp(), df['Total Passengers'], label='Actual')
plt.plot(forecast_df.index.to_timestamp(),
         forecast_df['forecast'], label='Forecast')
plt.xlabel('Date')
plt.ylabel('Total Passengers')
plt.title('10-Year Passenger Forecast')
plt.legend()
plt.show()
