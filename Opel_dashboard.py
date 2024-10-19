import obd
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

        self.connection = obd.OBD()  # Connect to OBD-II
        print("Connected to OBD-II.")

        self.update_dashboard()

    def update_dashboard(self):
        # Query vehicle data
        speed_response = self.connection.query(obd.commands.SPEED)
        speed = speed_response.value.to("km/h") if speed_response.value else "N/A"

        rpm_response = self.connection.query(obd.commands.RPM)
        rpm = rpm_response.value.to("rpm") if rpm_response.value else "N/A"

        coolant_response = self.connection.query(obd.commands.COOLANT_TEMP)
        coolant_temp = coolant_response.value.to("C") if coolant_response.value else "N/A"

        oxygen_response = self.connection.query(obd.commands.O2S1_B1)
        oxygen_intake = oxygen_response.value if oxygen_response.value else "N/A"

        # Update labels
        self.speed_label.config(text=f"Speed: {speed} km/h")
        self.rpm_label.config(text=f"RPM: {rpm} RPM")
        self.coolant_label.config(text=f"Coolant Temp: {coolant_temp} °C")
        self.oxygen_label.config(text=f"Oxygen Intake: {oxygen_intake} V")

        # Refresh every second
        self.after(1000, self.update_dashboard)

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()

