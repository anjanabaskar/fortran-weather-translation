from weather import Weather

def main():
    num_temps = 7
    f_high_array = [65, 68, 70, 72, 75, 73, 71]
    f_low_array = [45, 46, 47, 50, 52, 49, 48]
    wind_speed = 5
    weather_code = 'P'  # Partly Cloudy

    forecast = Weather(f_high_array, f_low_array, num_temps, wind_speed, weather_code)

    print(f"Weather Forecast: {forecast.description}")
    print(f"Wind Speed: {forecast.wind_speed} mph")
    print()
    forecast.display_today_weather()
    forecast.display_weekly_weather()

if __name__ == "__main__":
    main()
