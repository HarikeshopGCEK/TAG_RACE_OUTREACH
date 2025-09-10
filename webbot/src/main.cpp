// Programme by Harikesh OP
// GCEK IEEE RAS SB 
// CONTACT 23B472@GCEK.AC.IN
// Phone No : 6238622195
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

#define LM1 D1
#define LM2 D2
#define RM1 D5
#define RM2 D6

#define ENA D3
#define ENB D4

#define SPEED 255

void forward()
{
  digitalWrite(LM1, HIGH);
  digitalWrite(LM2, LOW);
  digitalWrite(RM1, HIGH);
  digitalWrite(RM2, LOW);
  analogWrite(ENA, SPEED);
  analogWrite(ENB, SPEED);
}
void backward()
{
  digitalWrite(LM1, LOW);
  digitalWrite(LM2, HIGH);
  digitalWrite(RM1, LOW);
  digitalWrite(RM2, HIGH);
  analogWrite(ENA, SPEED);
  analogWrite(ENB, SPEED);
}
void left()
{
  digitalWrite(LM1, LOW);
  digitalWrite(LM2, HIGH);
  digitalWrite(RM1, HIGH);
  digitalWrite(RM2, LOW);
  analogWrite(ENA, SPEED);
  analogWrite(ENB, SPEED);
}
void right()
{
  digitalWrite(LM1, HIGH);
  digitalWrite(LM2, LOW);
  digitalWrite(RM1, LOW);
  digitalWrite(RM2, HIGH);
  analogWrite(ENA, SPEED);
  analogWrite(ENB, SPEED);
}
void stop()
{
  digitalWrite(LM1, LOW);
  digitalWrite(LM2, LOW);
  digitalWrite(RM1, LOW);
  digitalWrite(RM2, LOW);
  analogWrite(ENA, 0);
  analogWrite(ENB, 0);
}

char ssid[] = "your-SSID";     // your network SSID (name)
char pass[] = "your-PASSWORD"; // your network password

ESP8266WebServer server(80);
String html = "<html><head><title>TAG RACE Robot</title>"
              "<style>"
              "body { background:#222; color:#fff; font-family:sans-serif; text-align:center; padding-top:40px; }"
              ".dpad { display:inline-block; }"
              ".row { display:flex; justify-content:center; margin:5px; }"
              ".btn {"
              "  width:70px; height:70px; margin:5px; font-size:20px; border-radius:20px;"
              "  border:none; background:#444; color:#fff; cursor:pointer; transition:background 0.2s;"
              "  box-shadow:0 2px 8px #0006;"
              "}"
              ".btn:active { background:#4CAF50; }"
              ".btn.stop { background:#c62828; }"
              ".btn.stop:active { background:#ff5252; }"
              "</style>"
              "<script>"
              "function send(cmd){ fetch('/'+cmd); }"
              "</script></head><body>"
              "<h1>TAG RACE COMPETITION</h1>"
              "<h2>Robot Control Panel</h2>"
              "<p>Use the buttons below to control the robot.</p>"
              "<div class='dpad'>"
              "  <div class='row'><button class='btn' onclick=\"send('forward')\">&#9650;</button></div>"
              "  <div class='row'>"
              "    <button class='btn' onclick=\"send('left')\">&#9664;</button>"
              "    <button class='btn stop' onclick=\"send('stop')\">&#9632;</button>"
              "    <button class='btn' onclick=\"send('right')\">&#9654;</button>"
              "  </div>"
              "  <div class='row'><button class='btn' onclick=\"send('backward')\">&#9660;</button></div>"
              "</div>"
              "</body></html>";
void handleRoot()
{
  server.send(200, "text/html", html);
}
void handleForward()
{
  Serial.println("FORWARD");
  // Add your motor control code here
  server.send(200, "text/html", html);
  forward();
}
void handleBackward()
{
  Serial.println("BACKWARD");
  // Add your motor control code here
  server.send(200, "text/html", html);
  backward();
}

void handleLeft()
{
  Serial.println("LEFT");
  // Add your motor control code here
  server.send(200, "text/html", html);
  left();
}

void handleRight()
{
  Serial.println("RIGHT");
  // Add your motor control code here
  server.send(200, "text/html", html);
  right();
}

void handleStop()
{
  Serial.println("STOP");
  // Add your motor control code here
  server.send(200, "text/html", html);
  stop();
}
void setup()
{
  pinMode(LM1, OUTPUT);
  pinMode(LM2, OUTPUT);
  pinMode(RM1, OUTPUT);
  pinMode(RM2, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  // put your setup code here, to run once:
  WiFi.mode(WIFI_AP);
  WiFi.softAP(ssid, pass);

  Serial.begin(115200);
  Serial.println("WiFi Access Point started");
  Serial.print("AP IP address: ");
  Serial.println(WiFi.softAPIP());
  Serial.print("AP SSID: ");
  Serial.println(WiFi.softAPSSID());
  Serial.print("AP Password: ");
  Serial.println(WiFi.softAPPSK());

  server.on("/", handleRoot);
  server.on("/forward", handleForward);
  server.on("/backward", handleBackward);
  server.on("/left", handleLeft);
  server.on("/right", handleRight);
  server.on("/stop", handleStop);

  server.begin();
  Serial.println("HTTP server started");
}

void loop()
{
  // put your main code here, to run repeatedly:
  server.handleClient();
}
