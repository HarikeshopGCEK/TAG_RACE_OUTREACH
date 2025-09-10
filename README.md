# WEBBOT - WiFi Controlled Robot

This project is an ESP8266-based robot controller that allows you to control a robot via a web browser. The ESP8266 creates its own WiFi network that you can connect to directly. The robot can move forward, backward, left, right, and stop via a simple web interface.

## Features

- Creates its own WiFi network (Access Point mode)
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

1. **Configure WiFi Access Point**  
   In `src/main.cpp`, set your desired WiFi network name and password:

   ```cpp
   char ssid[] = "YOUR_ROBOT_WIFI_NAME";
   char pass[] = "YOUR_PASSWORD";
   ```

2. **Upload the Code**  
   Use the Arduino IDE or PlatformIO to upload the code to your ESP8266.

3. **Power the Robot**  
   Ensure your ESP8266 and motors are powered appropriately.

4. **Connect to the Robot**

   - After boot, the ESP8266 will create its own WiFi network.
   - On your phone/computer, connect to the WiFi network named as configured in step 1.
   - The robot's web interface will be available at: `http://192.168.4.1`

5. **Control via Browser**
   - Open your browser and go to `http://192.168.4.1`
   - Use the on-screen buttons to control the robot.

## Web Interface

- **Forward:** Moves the robot forward
- **Backward:** Moves the robot backward
- **Left:** Turns the robot left
- **Right:** Turns the robot right
- **Stop:** Stops all movement

## Notes

- Connect your phone/computer directly to the robot's WiFi network to control it.
- The robot creates its own WiFi network - no existing WiFi infrastructure needed.
- Adjust motor speed by changing the `SPEED` macro in `main.cpp`.

## License

MIT License

---

Made for TAG RACE COMPETITION
