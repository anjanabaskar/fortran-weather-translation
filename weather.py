from typing import List

class Weather:
    def __init__(self, f_high_array: List[int], f_low_array: List[int], num_temps: int, wind_speed: int, weather_code: str):
        self.f_high_array = f_high_array
        self.f_low_array = f_low_array
        self.num_temps = num_temps
        self.wind_speed = wind_speed
        self.weather_code = weather_code
        self.description = ""
        self.determine_description()

    def calculate_average_fahrenheit_high_temp(self) -> float:
        return sum(self.f_high_array) / self.num_temps

    def calculate_average_fahrenheit_low_temp(self) -> float:
        return sum(self.f_low_array) / self.num_temps

    def find_weekly_fahrenheit_high_temp(self) -> int:
        return max(self.f_high_array)

    def find_weekly_fahrenheit_low_temp(self) -> int:
        return min(self.f_low_array)

    def determine_description(self):
        code_map = {
            'S': 'SUNNY',
            'P': 'PARTLY CLOUDY',
            'C': 'CLOUDY',
            'N': 'CLEAR'
        }
        self.description = code_map.get(self.weather_code.upper(), 'UNKNOWN')

    def display_today_weather(self):
        print("SUNDAY FORECAST")
        print(f"High: {self.f_high_array[0]} (F), Low: {self.f_low_array[0]} (F)")
        print()

    def display_weekly_weather(self):
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        print("THE WEEKLY FORECAST")
        print(f"Average Hi: {self.calculate_average_fahrenheit_high_temp():.2f}")
        print(f"Average Low: {self.calculate_average_fahrenheit_low_temp():.2f}")
        print()
        print(f"Highest Weekly Temperature: {self.find_weekly_fahrenheit_high_temp()} (F)")
        print(f"Lowest Weekly Temperature: {self.find_weekly_fahrenheit_low_temp()} (F)")
        print()
        for i in range(self.num_temps):
            print(days[i])
            print(f"High: {self.f_high_array[i]} (F), Low: {self.f_low_array[i]} (F)")
            print()
            #
