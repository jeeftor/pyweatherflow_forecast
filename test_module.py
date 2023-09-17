"""
This module is only used to run some realtime data tests
while developing the module.
Create a .env file and add STATION_ID with the id of your station and API_TOKEN with the personal Token
"""
from __future__ import annotations

from dotenv import load_dotenv
import os
import logging

from pyweatherflow_forecast import (
    WeatherFlow,
    WeatherFlowForecastData,
    WeatherFlowStationData,
)

_LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

load_dotenv()
station_id = os.getenv("STATION_ID")
api_token = os.getenv("API_TOKEN")

weatherflow = WeatherFlow(station_id, api_token)

data: WeatherFlowStationData = weatherflow.get_station()
print("STATION NAME: ", data.station_name)

# data: WeatherFlowForecastData = weatherflow.get_forecast()
# print("TEMPERATURE: ", data.temperature)
# for item in data.forecast:
#     print(item.temperature, item.temp_low, item.icon, item.condition, item.precipitation_probability)

# hourly: WeatherFlowForecastData = weatherflow.get_forecast_hour()
# print("FEELS LIKE: ", hourly.apparent_temperature)
# for item in hourly.forecast:
#     print(item. valid_time, item.temperature, item.apparent_temperature, item.icon, item.condition, item.precipitation, item.precipitation_probability)
