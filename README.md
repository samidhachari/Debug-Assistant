# Debug-Assistant
Debug Assistant Tool for Embedded SoC Bring-up

Developed a Python-based tool to classify UART logs during SoC boot/debug cycles.
Identified bootloader, I2C, and system reset errors; added timestamped RCA tagging.
Integrated with Tkinter GUI and GitHub Actions CI pipeline for automated test validation.
Designed to simulate real on-site debug and embedded Linux log workflows.


# 🔧 Debug Assistant Tool for Embedded Systems

A real-time debug assistant that reads serial logs from embedded devices, classifies events, logs them to CSV/JSON, and supports GUI visualization and CI/CD automation.

## 💡 Features

- Serial log listener via `/dev/ttyUSB0` or `COM3`
- Automatic classification: BOOT, ERROR, REBOOT, I2C_ERROR, etc.
- Real-time color-coded console + optional Tkinter GUI
- Logs stored in `.csv` and `.json` format
- GitHub Actions pipeline integration for firmware CI

## 🚀 Quick Start

### Core Script
```bash
pip install pyserial
python debug_assistant_tool.py
```

### GUI Mode
```bash
python gui_log_viewer.py
```

### GitHub Actions CI
Push a test log to `test_logs/` to trigger the pipeline.

## 📂 File Structure

```
.
├── debug_assistant_tool.py     # Serial log parser
├── gui_log_viewer.py           # GUI visualizer (Tkinter)
├── test_logs/                  # Sample logs for CI test
├── debug_log.csv               # Output log file
├── .github/
│   └── workflows/
│       └── log_check.yml       # GitHub Actions workflow
└── README.md
```

## 🛠️ Use Case
Perfect for:
- Embedded Test Engineers
- SoC Bring-up Debugging
- Firmware Validation & CI Automation

## 👩‍💻 Author
Samidha Sudesh Chari

