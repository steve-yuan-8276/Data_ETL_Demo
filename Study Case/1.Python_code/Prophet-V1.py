import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt

# Load the monthly data from the provided XLSX file
# Assuming that the Excel file has a sheet named 'Sheet1' with 'Month' and 'Total Passengers' columns
df = pd.read_excel('monthly_passengers.xlsx',
                   sheet_name='Sheet1', parse_dates=['Month'])
df.set_index('Month', inplace=True)

# Create a binary variable to represent the impact of COVID-19
# Assuming the impact of COVID-19 starts from 2020 and ends by the end of 2023
df['COVID19'] = ((df.index >= '2020-01-01') &
                 (df.index <= '2023-12-01')).astype(int)

# Fit the SARIMAX model with COVID-19 as an exogenous variable
exog = df[['COVID19']]
model = SARIMAX(df['Total Passengers'],
                exog=exog,
                order=(1, 1, 1),
                seasonal_order=(1, 1, 1, 12))  # Adding seasonal_order for monthly data
results = model.fit()

# Predict future passenger numbers for the next 120 months (10 years)
# Set COVID19 impact to 0 for the predictions as we are assuming that there will be no impact after 2023
exog_forecast = pd.DataFrame({'COVID19': [0] * 120},
                             index=pd.date_range(start=df.index[-1] + pd.offsets.MonthEnd(), periods=120, freq='M'))

forecast = results.get_forecast(steps=120, exog=exog_forecast)
forecast_df = forecast.conf_int(alpha=0.05)  # 95% confidence interval
forecast_df['forecast'] = forecast.predicted_mean

# Round the forecast to the nearest whole number
forecast_df['forecast'] = forecast_df['forecast'].round()

# Save the forecast to a CSV file
forecast_df.to_csv('forecast_10years_v1.csv')

# Plot the historical data and the forecast
plt.figure(figsize=(10, 5))
plt.plot(df['Total Passengers'], label='Historical Monthly Passengers')
plt.plot(forecast_df['forecast'], label='Forecasted Monthly Passengers')
plt.fill_between(forecast_df.index,
                 forecast_df['lower Total Passengers'],
                 forecast_df['upper Total Passengers'],
                 color='k', alpha=0.1, label='Confidence Interval')
plt.title('Monthly Passenger Forecast for the Next 10 Years')
plt.legend()
plt.show()
