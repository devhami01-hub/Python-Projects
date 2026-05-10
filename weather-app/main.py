import requests
import tkinter as tk
from tkinter import messagebox

API = "YOUR_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def type_text(label, text, index=0):
    if index < len(text):
        label.config(text=text[:index + 1])
        root.after(30, type_text, label, text, index + 1)


def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showerror("Error", "Please enter a city name")
        return

    result_label.config(text="⏳ Fetching weather...")
    root.update()

    url = f"{BASE_URL}?q={city}&appid={API}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if str(data["cod"]) != "200":
            result_label.config(text="❌ City not found")
            return

        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        final_text = (
            f"🌍 City: {city}\n"
            f"🔥 Temp: {temp}°C\n"
            f"🌡 Weather: {weather}\n"
            f"💧 Humidity: {humidity}%"
        )

        result_label.config(text="")
        type_text(result_label, final_text)

    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Weather App")
root.geometry("320x300")
root.configure(bg="#1e1e1e")

title = tk.Label(root, text="🌦 Weather App", font=("Arial", 16), fg="white", bg="#1e1e1e")
title.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(pady=5)

btn = tk.Button(root, text="Get Weather", command=get_weather)
btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), fg="white", bg="#1e1e1e", justify="left")
result_label.pack(pady=10)

root.mainloop()