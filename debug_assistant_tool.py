
import serial
import re
import csv
from datetime import datetime

# Configuration
SERIAL_PORT = '/dev/ttyUSB0'  # Change this to your actual serial port, e.g., 'COM3' on Windows
BAUD_RATE = 9600              # Adjust based on your device
LOG_FILE = 'debug_log.csv'

# Define patterns for classification
event_patterns = {
    "BOOT": r"\[BOOT\]",
    "I2C_ERROR": r"\[I2C\].*failed",
    "CRITICAL": r"\[ERROR\]",
    "INFO": r"\[INFO\]",
    "SYSTEM_RESET": r"\[REBOOT\]"
}

# Classify a log line
def classify_log_line(line):
    for label, pattern in event_patterns.items():
        if re.search(pattern, line):
            return label
    return "UNKNOWN"

# Initialize serial connection
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Listening on {SERIAL_PORT} at {BAUD_RATE} baud...")
except serial.SerialException as e:
    print(f"Error: Could not open serial port {SERIAL_PORT}.\n{e}")
    exit(1)

# Open CSV file for logging
with open(LOG_FILE, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Event", "Status"])

    try:
        while True:
            if ser.in_waiting:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                if line:
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    status = classify_log_line(line)
                    writer.writerow([timestamp, line, status])
                    print(f"[{timestamp}] {line} --> {status}")
    except KeyboardInterrupt:
        print("\nStopped by user.")
    finally:
        ser.close()
