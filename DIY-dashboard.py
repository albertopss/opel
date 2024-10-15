#dashboard that reads data from the OBD-II port
import obd
import time
import os

# Clear the console screen for a better display
def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

def main():
    connection = obd.OBD()  # Connect to OBD-II
    print("Connected to OBD-II.")

    try:
        while True:
            clear_console()
#displays vehicle speed and RPM.            
            # Query vehicle speed
            speed_response = connection.query(obd.commands.SPEED)
            speed = speed_response.value.mph if speed_response.value else "N/A"
            
            # Query RPM
            rpm_response = connection.query(obd.commands.RPM)
            rpm = rpm_response.value.to("rpm") if rpm_response.value else "N/A"
            
            # Display the dashboard
            print("=== Racecar Dashboard ===")
            print(f"Speed: {speed} mph")
            print(f"RPM: {rpm} RPM")
            print("==========================")
            
            # Update every second
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nExiting dashboard.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

