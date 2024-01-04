import numpy as np
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the monthly passengers data from an Excel file
df_passengers = pd.read_excel('monthly_passengers.xlsx', sheet_name='Sheet1')
df_passengers['Month'] = pd.to_datetime(
    df_passengers['Month']).dt.to_period('M')
df_passengers.set_index('Month', inplace=True)

# Load the annual GDP data from another Excel file
df_gdp = pd.read_excel('Grand_Dallas_GDP.xlsx', sheet_name='Sheet1')
df_gdp['Years'] = pd.to_datetime(
    df_gdp['Years'], format='%Y').dt.to_period('A-DEC')
df_gdp.set_index('Years', inplace=True)

# Ensure that GDP values are repeated for each month of the year in the GDP dataframe
df_gdp = df_gdp.resample('M').ffill().reindex(
    df_passengers.index, method='pad')

# Add the GDP data to the passengers DataFrame
df_passengers['GDP'] = df_gdp['GDP']

# Calculate decay factor using data up to 2019 for a linear trend
cutoff = pd.Period('2019-12', freq='M')
train_data = df_passengers[df_passengers.index <= cutoff]
X_train = np.arange(len(train_data)).reshape(-1, 1)
y_train = train_data['Total Passengers'].values
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

# Predict passenger numbers for months after the cutoff point
X_future = np.arange(len(train_data), len(df_passengers)).reshape(-1, 1)
y_pred = lin_reg.predict(X_future)

# Calculate decay factor
actual = df_passengers[df_passengers.index > cutoff]['Total Passengers'].values
decay_factor = actual / y_pred

# Insert decay factor into DataFrame
df_passengers['Decay'] = 1  # Default to 1 for months without decay
df_passengers.loc[df_passengers.index > cutoff, 'Decay'] = decay_factor

# Create a binary variable to represent the impact of COVID-19
df_passengers['COVID19'] = ((df_passengers.index >= pd.Period('2020-01', 'M')) &
                            (df_passengers.index <= pd.Period('2024-12', 'M'))).astype(int)

# Fit the SARIMAX model with COVID-19, decay factor, and GDP as exogenous variables
exog = df_passengers[['COVID19', 'Decay', 'GDP']]
model = SARIMAX(df_passengers['Total Passengers'], exog=exog,
                order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
results = model.fit()

# Predict future passenger numbers
forecast_start = df_passengers.index[-1] + 1
exog_forecast = pd.DataFrame({
    'COVID19': [0] * 120,  # Assuming no COVID-19 effect after 2024
    'Decay': [1] * 120,  # Assuming no decay after 2024
    # Assuming GDP stays constant after last known value
    'GDP': [df_passengers['GDP'][-1]] * 120
}, index=pd.period_range(start=forecast_start, periods=120, freq='M'))

# Forecast for the next 10 years
forecast = results.get_forecast(steps=120, exog=exog_forecast)
forecast_df = forecast.conf_int(alpha=0.05)
forecast_df['forecast'] = forecast.predicted_mean

# Round the forecast to the nearest whole number
forecast_df['forecast'] = forecast_df['forecast'].round()

# Save forecast to CSV
forecast_df['forecast'].to_frame(
    name='forecast').to_csv('forecast_10years_V3.csv')

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(df_passengers.index.to_timestamp(),
         df_passengers['Total Passengers'], label='Actual')
plt.plot(forecast_df.index.to_timestamp(),
         forecast_df['forecast'], label='Forecast')
plt.fill_between(forecast_df.index.to_timestamp(),
                 forecast_df.iloc[:, 0],
                 forecast_df.iloc[:, 1],
                 color='k', alpha=0.1)
plt.title('10-Year Passenger Forecast with GDP Consideration')
plt.xlabel('Date')
plt.ylabel('Total Passengers')
plt.legend()
plt.show()
