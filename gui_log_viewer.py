
import tkinter as tk
from tkinter import ttk, scrolledtext
import re
from datetime import datetime

# Simulated log input 
mock_logs = [
    "[BOOT] Initializing hardware...",
    "[I2C] Sensor init failed.",
    "[ERROR] Stack overflow detected.",
    "[INFO] Entering sleep mode.",
    "[REBOOT] Unexpected system reset detected.",
    "[INFO] Device entered standby mode.",
    "[ERROR] I2C timeout occurred."
]

# Classify logs
event_patterns = {
    "BOOT": r"\[BOOT\]",
    "I2C_ERROR": r"\[I2C\].*failed|timeout",
    "CRITICAL": r"\[ERROR\]",
    "INFO": r"\[INFO\]",
    "SYSTEM_RESET": r"\[REBOOT\]"
}
event_colors = {
    "BOOT": "green",
    "I2C_ERROR": "orange",
    "CRITICAL": "red",
    "INFO": "blue",
    "SYSTEM_RESET": "purple",
    "UNKNOWN": "gray"
}
def classify_line(line):
    for label, pattern in event_patterns.items():
        if re.search(pattern, line):
            return label
    return "UNKNOWN"

# Tkinter UI
def start_gui():
    root = tk.Tk()
    root.title("Debug Assistant Log Viewer")

    log_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
    log_display.grid(column=0, row=0, padx=10, pady=10)

    for line in mock_logs:
        timestamp = datetime.now().strftime("%H:%M:%S")
        status = classify_line(line)
        color = event_colors.get(status, "black")
        log_display.insert(tk.END, f"[{timestamp}] {line} --> {status}\n", status)
        log_display.tag_config(status, foreground=color)

    root.mainloop()

if __name__ == "__main__":
    start_gui()
