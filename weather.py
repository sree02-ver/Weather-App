import tkinter as tk
import tkinter.messagebox
import requests
import json

class WeatherApp:
    def __init__(self, master):
        self.master = master
        master.title("Weather App")

        self.city_entry = tk.Entry(master, width=15)
        self.city_entry.grid(row=0, column=1, padx=(0, 10))

        self.get_weather_button = tk.Button(master, text="Get Weather", command=self.get_weather)
        self.get_weather_button.grid(row=0, column=2)

        self.temperature_label = tk.Label(master, text="Temperature:")
        self.temperature_label.grid(row=1, column=0)
        self.temperature_value = tk.Label(master, text="")
        self.temperature_value.grid(row=1, column=1)

        self.description_label = tk.Label(master, text="Description:")
        self.description_label.grid(row=2, column=0)
        self.description_value = tk.Label(master, text="")
        self.description_value.grid(row=2, column=1)

        self.api_key = "30d4741c779ba94c470ca1f63045390a"  # Replace with your actual API key

    def get_weather(self):
        city = self.city_entry.get()
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                main = data["main"]
                temperature = main["temp"]
                weather = data["weather"]
                description = weather[0]["description"]

                self.temperature_value.config(text=f"{temperature}°C")
                self.description_value.config(text=description.capitalize())
            else:
                tkinter.messagebox.showerror("Error", "Error fetching weather data. Please check the city name and try again.")
        else:
            tkinter.messagebox.showerror("Error", "Please enter a city name.")

root = tk.Tk()
app = WeatherApp(root)
root.mainloop()
