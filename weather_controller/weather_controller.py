# weather_controller.py
import os

import requests


class WeatherController:

    def __init__(self):
        self.api_key = os.getenv("LOCATIONIQ_API_KEY")
        print(f"API key set: {self.api_key}")

    def get_longitude_and_latitude_url(self, city, state_abbreviation):
        return f"https://us1.locationiq.com/v1/search?key={self.api_key}&q={city},{state_abbreviation}&format=json&"

    def get_long_and_lat_for_default_city_and_state_url(self):
        return self.get_longitude_and_latitude_url("Pittsburgh", "PA")

    def get_grid_points_url(self, latitude, longitude):
        return f"https://api.weather.gov/points/{latitude},{longitude}"

    def get_forecast_url(self, office, grid_x, grid_y):
        return f"https://api.weather.gov/gridpoints/{office}/{grid_x},{grid_y}/forecast"

    def get_latitude_and_longitude(self, city, state_abbreviation):
        print("Making latitude and longitude request")
        if city is None or state_abbreviation is None:
            response = requests.get(self.get_long_and_lat_for_default_city_and_state_url())
        else:
            response = requests.get(self.get_longitude_and_latitude_url(city, state_abbreviation))

        if response.ok:
            print("Latitude and longitude successfully retrieved")
            data = response.json()
            latitude = data[0]['lat']
            longitude = data[0]['lon']
            return {'lat': latitude, 'long': longitude}
        else:
            raise requests.HTTPError(f"Error: request failed: f{response.status_code} - {response.text}")

    def get_location(self, latitude, longitude):
        print(f"Making location request. Latitude: {latitude}, longitude: {longitude}")

        response = requests.get(self.get_grid_points_url(latitude, longitude))

        if response.ok:
            data = response.json()
            office = data['properties']['gridId']
            grid_x = data['properties']['gridX']
            grid_y = data['properties']['gridY']

        else:
            raise requests.HTTPError(f"Error: request failed: f{response.status_code} - {response.text}")

        return {
            'office': office,
            'grid_x': grid_x,
            'grid_y': grid_y
        }

    def get_weather_discussion(self, city, state_abbreviation):
        print(f"Making weather discussion request. City: {city}, state: {state_abbreviation}")

        lat_and_long = self.get_latitude_and_longitude(city, state_abbreviation)
        location_data = self.get_location(lat_and_long['lat'], lat_and_long['long'])

        response = requests.get(
            self.get_forecast_url(location_data['office'], location_data['grid_x'], location_data['grid_y']))

        if response.ok:
            forecast_data = response.json()
            print(forecast_data)
            return forecast_data
