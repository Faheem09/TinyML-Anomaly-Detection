# TinyML Anomaly Detection

This project demonstrates how to use TinyML for unsupervised anomaly detection with vibration data collected from an Arduino Nano 33 BLE Sense.

## Features
- Real-time data collection using Arduino Nano 33 BLE Sense
- Anomaly detection using Python and Isolation Forest
- Data visualization of detected anomalies

## Hardware Requirements
- Arduino Nano 33 BLE Sense
- USB Cable
- PC with Python and VS Code

## Software Requirements
- Arduino IDE
- Python 3.7 or higher
- Libraries: `pandas`, `scikit-learn`, `matplotlib`, `pyserial`

## Setup Instructions

### Arduino Setup
1. Upload the `Nano33BLE_Accelerometer.ino` sketch to the Arduino.
2. Connect the Arduino to your PC.

### Python Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/TinyML-Anomaly-Detection.git
   cd TinyML-Anomaly-Detection
   ```
2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```
3. Run the `data_collection.py` script to collect vibration data:
   ```bash
   python Python_Code/data_collection.py
   ```
4. Run the `anomaly_detection.py` script to detect anomalies:
   ```bash
   python Python_Code/anomaly_detection.py
   ```

## Example Visualization
![Anomaly Detection Plot](example_plot.png)

## License
This project is licensed under the MIT License.
