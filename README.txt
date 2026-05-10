# 🌦️ Weather App (Python GUI)

A simple and modern Weather Application built with Python using Tkinter.  
It fetches real-time weather data using a weather API and displays it in a clean graphical interface.

---

## 🚀 Features

- 🌍 Search weather by city name  
- 🌡️ Shows temperature in Celsius  
- ☁️ Displays weather condition  
- 💧 Shows humidity level  
- ✨ Animated text output (typewriter effect)  
- 🖥️ Simple and clean GUI (Tkinter)

---

## 🛠️ Tech Stack

- Python  
- Tkinter (GUI)  
- Requests (API handling)  
- OpenWeather API (data source)

---

## ⚙️ How It Works

1. User enters city name  
2. App sends request to weather API  
3. API returns JSON data  
4. App extracts:
   - Temperature  
   - Weather condition  
   - Humidity  
5. Data is shown in GUI with animation

---

## 🔑 API Setup

This project uses the **OpenWeather API**.

👉 For security reasons, the API key is not included.

To run the project:

1. Get your API key from OpenWeather
2. Add it in your `config.py` file:

```python
API_KEY = "your_api_key_here"