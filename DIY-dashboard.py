import random
import time
import tkinter as tk
from tkinter import ttk

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Racecar Dashboard")
        self.geometry("400x300")

        # Labels for displaying data
        self.speed_label = ttk.Label(self, text="Speed: N/A km/h", font=("Helvetica", 16))
        self.speed_label.pack(pady=10)

        self.rpm_label = ttk.Label(self, text="RPM: N/A", font=("Helvetica", 16))
        self.rpm_label.pack(pady=10)

        self.coolant_label = ttk.Label(self, text="Coolant Temp: N/A °C", font=("Helvetica", 16))
        self.coolant_label.pack(pady=10)

        self.oxygen_label = ttk.Label(self, text="Oxygen Intake: N/A V", font=("Helvetica", 16))
        self.oxygen_label.pack(pady=10)

        self.update_dashboard()

    def update_dashboard(self):
        # Simulate vehicle data
        speed = random.randint(0, 240)  # Speed in km/h
        rpm = random.randint(0, 8000)    # RPM
        coolant_temp = random.uniform(70, 100)  # Coolant temperature in °C
        oxygen_intake = random.uniform(0, 1)  # Oxygen sensor output in volts

        # Update labels with simulated data
        self.speed_label.config(text=f"Speed: {speed} km/h")
        self.rpm_label.config(text=f"RPM: {rpm} RPM")
        self.coolant_label.config(text=f"Coolant Temp: {coolant_temp:.2f} °C")
        self.oxygen_label.config(text=f"Oxygen Intake: {oxygen_intake:.2f} V")

        # Refresh every second
        self.after(1000, self.update_dashboard)

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()

