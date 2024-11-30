import serial
import csv

# Configure Serial Port
serial_port = 'COM3'  # Update with your port (e.g., /dev/ttyUSB0 on Linux)
baud_rate = 9600

# Open Serial Connection
ser = serial.Serial(serial_port, baud_rate, timeout=1)

# Collect Data and Save to CSV
with open("vibration_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["x", "y", "z"])  # Header
    
    try:
        while True:
            line = ser.readline().decode("utf-8").strip()
            if line:
                data = line.split(",")
                writer.writerow(data)
                print(data)
    except KeyboardInterrupt:
        print("Data collection stopped.")
    finally:
        ser.close()
