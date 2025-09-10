# WEBBOT - WiFi Controlled Robot

This project is an ESP8266-based robot controller that allows you to control a robot over your WiFi network using a web browser. The robot can move forward, backward, left, right, and stop via a simple web interface.

## Features

- Connects to your existing WiFi network (Station mode)
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

1. **Edit WiFi Credentials**  
   In `src/main.cpp`, set your WiFi SSID and password:

   ```cpp
   char ssid[] = "YOUR_SSID";
   char pass[] = "YOUR_PASSWORD";
   ```

2. **Upload the Code**  
   Use the Arduino IDE or PlatformIO to upload the code to your ESP8266.

3. **Power the Robot**  
   Ensure your ESP8266 and motors are powered appropriately.

4. **Connect to the Robot**

   - After boot, the ESP8266 will connect to your WiFi.
   - Open the Serial Monitor at 115200 baud to find the robot's IP address.

5. **Control via Browser**
   - Enter the IP address in your browser.
   - Use the on-screen buttons to control the robot.

## Web Interface

- **Forward:** Moves the robot forward
- **Backward:** Moves the robot backward
- **Left:** Turns the robot left
- **Right:** Turns the robot right
- **Stop:** Stops all movement

## Notes

- Ensure your phone/computer is on the same WiFi network as the robot.
- Adjust motor speed by changing the `SPEED` macro in `main.cpp`.

## License

MIT License

---

Made for TAG RACE COMPETITION
