import customtkinter as ctk
import plyer
import schedule
import time
import threading
import pyttsx3

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

engine = pyttsx3.init()

def reminder():
    plyer.notification.notify(
        title="💧 Drink Water",
        message="Stay hydrated!",
        timeout=5
    )

    engine.say("Drink water. Stay hydrated.")
    engine.runAndWait()

def start_reminder():
    try:
        minutes = int(entry.get())

        schedule.clear()
        schedule.every(minutes).minutes.do(reminder)

        status_label.configure(
            text=f"Reminder every {minutes} min started ✅"
        )

    except:
        status_label.configure(
            text="Enter valid number ❌"
        )

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

app = ctk.CTk()
app.geometry("450x350")
app.title("Hydration Reminder")

title = ctk.CTkLabel(
    app,
    text="💧 Hydration Reminder",
    font=("Arial", 28, "bold")
)
title.pack(pady=25)

subtitle = ctk.CTkLabel(
    app,
    text="Stay healthy and hydrated",
    font=("Arial", 15)
)
subtitle.pack(pady=5)

entry = ctk.CTkEntry(
    app,
    placeholder_text="Enter time in minutes",
    width=220,
    height=40,
    font=("Arial", 14)
)
entry.pack(pady=20)

button = ctk.CTkButton(
    app,
    text="Start Reminder",
    command=start_reminder,
    width=200,
    height=45,
    font=("Arial", 15, "bold"),
    corner_radius=15
)
button.pack(pady=15)

status_label = ctk.CTkLabel(
    app,
    text="No reminder started",
    font=("Arial", 13)
)
status_label.pack(pady=10)

footer = ctk.CTkLabel(
    app,
    text="Made by Dev Hami ©",
    font=("Arial", 11)
)
footer.pack(side="bottom", pady=10)

thread = threading.Thread(target=run_schedule, daemon=True)
thread.start()

app.mainloop()
