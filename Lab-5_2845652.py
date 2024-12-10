import requests  # Import the requests library to make HTTP requests
import json      # Import the json library to handle JSON data

# Function to get the Cleveland weather forecast
def GetClevelandWeather():
    # Step 1: Set up the endpoint for the weather forecast
    # This is the specific URL given in the question for Cleveland, OH forecast
    endpoint = "https://api.weather.gov/gridpoints/CLE/84,66/forecast"
    
    try:
        # Step 2: Make a GET request to fetch the weather data from the endpoint
        response = requests.get(endpoint)
        
        # Step 3: Check if the request was successful (HTTP status code 200)
        response.raise_for_status()  # This will raise an error if the request failed

        # Step 4: Convert the response text (which is in JSON format) into a Python dictionary
        weather_data = response.json()

        # Step 5: Access the 'periods' list in the response and get the first element (most current forecast)
        current_forecast = weather_data['properties']['periods'][0]

        # Step 6: Extract and print the temperature and detailed forecast as required
        temperature = current_forecast['temperature']
        temperature_unit = current_forecast['temperatureUnit']  # Unit like Fahrenheit (°F)
        detailed_forecast = current_forecast['detailedForecast']

        # Step 7: Display the Cleveland weather report with the temperature and detailed forecast
        print("Cleveland Weather Report")
        print(f"Temperature: {temperature}°{temperature_unit}")
        print(f"Detailed Forecast: {detailed_forecast}")

    except requests.exceptions.RequestException as e:  # This will handle any errors like network issues
        print(f"Error fetching weather data: {e}")

# Call the function to run the program and get the Cleveland weather
GetClevelandWeather()
