# WEBBOT - WiFi Controlled Robot

This project is an ESP8266-based robot controller that allows you to control a robot over WiFi using a web browser. The robot can move forward, backward, left, right, and stop via a simple web interface.

## Features

- ESP8266 creates its own WiFi network (Access Point mode)
- Hosts a web server for robot control
- Simple and responsive web-based control panel
- Real-time control of motors via browser buttons

## Hardware Requirements

- ESP8266 (NodeMCU or similar)
- Motor driver (L298N or similar)
- 2 DC motors (left and right)
- Robot chassis and power supply
- Wiring to connect ESP8266 to motor driver

## Pin Connections

| ESP8266 Pin | Motor Driver Function |
| ----------- | --------------------- |
| D1          | Left Motor IN1        |
| D2          | Left Motor IN2        |
| D5          | Right Motor IN1       |
| D6          | Right Motor IN2       |
| D3          | ENA (Left Motor PWM)  |
| D4          | ENB (Right Motor PWM) |

## Setup

1. **Edit WiFi Credentials (Optional)**  
   In `src/main.cpp`, you can set a custom SSID and password for the ESP8266 Access Point:

   ```cpp
   char ssid[] = "WEBBOT_AP";      // Default SSID for robot AP
   char pass[] = "robot123";       // Default password for robot AP
   ```

2. **Upload the Code**  
   Use the Arduino IDE or PlatformIO to upload the code to your ESP8266.

3. **Power the Robot**  
   Ensure your ESP8266 and motors are powered appropriately.

4. **Connect to the Robot**

   - After boot, the ESP8266 will start its own WiFi network (default SSID: `WEBBOT_AP`).
   - On your phone or computer, connect to this WiFi network using the set SSID and password.
   - Open the Serial Monitor at 115200 baud to find the robot's IP address (usually `192.168.4.1`).

5. **Control via Browser**
   - In your browser, enter the robot's IP address (e.g., `192.168.4.1`).
   - Use the on-screen buttons to control the robot.

## Web Interface

- **Forward:** Moves the robot forward
- **Backward:** Moves the robot backward
- **Left:** Turns the robot left
- **Right:** Turns the robot right
- **Stop:** Stops all movement

## Notes

- Your phone/computer must be connected to the robot's WiFi network (Access Point) to control it.
- Adjust motor speed by changing the `SPEED` macro in `main.cpp`.

## License

MIT License

---

Made for TAG RACE COMPETITION
