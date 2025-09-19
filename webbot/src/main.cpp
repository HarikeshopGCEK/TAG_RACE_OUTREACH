// Programme by Harikesh OP
// GCEK IEEE RAS SB 
// CONTACT 23B472@GCEK.AC.IN
// Phone No : 6238622195
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESPAsyncWebServer.h>
#include <AsyncTCP.h>

#define LM1 D1
#define LM2 D2
#define RM1 D5
#define RM2 D6

#define ENA D3
#define ENB D4

#define MAX_SPEED 255

volatile int leftSpeed = 0;   // 0-255
volatile int rightSpeed = 0;  // 0-255
volatile int turnSpeed = 0;   // 0-255

// Current drive state
enum DriveMode { MODE_STOP, MODE_FORWARD, MODE_BACKWARD, MODE_LEFT, MODE_RIGHT };
volatile DriveMode driveMode = MODE_STOP;

void applyMotorOutputs(int leftPwm, int rightPwm, bool leftForward, bool rightForward)
{
  // Left motor direction
  digitalWrite(LM1, leftForward ? HIGH : LOW);
  digitalWrite(LM2, leftForward ? LOW : HIGH);
  // Right motor direction
  digitalWrite(RM1, rightForward ? HIGH : LOW);
  digitalWrite(RM2, rightForward ? LOW : HIGH);
  // PWM
  analogWrite(ENA, constrain(leftPwm, 0, MAX_SPEED));
  analogWrite(ENB, constrain(rightPwm, 0, MAX_SPEED));
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

AsyncWebServer server(80);
String html = "<html><head><title>TAG RACE Robot</title>"
              "<style>"
              "body { background:#222; color:#fff; font-family:sans-serif; text-align:center; padding:20px; }"
              ".row { display:flex; justify-content:center; align-items:center; gap:10px; margin:10px 0; }"
              ".card { background:#333; padding:16px; border-radius:12px; box-shadow:0 2px 10px #0006; width:90%; max-width:640px; margin:0 auto; }"
              ".btn { padding:10px 16px; border-radius:10px; border:none; background:#444; color:#fff; cursor:pointer; box-shadow:0 2px 8px #0006; }"
              ".btn:active { background:#4CAF50; }"
              "input[type=range] { width: 60%; }"
              "label { width:120px; text-align:right; margin-right:10px; }"
              "</style>"
              "<script>"
              "function send(cmd){ fetch('/drive?mode='+cmd); }"
              "function qs(v){return document.querySelector(v);}"
              "function updateLabel(id,val){ qs('#'+id+'Val').innerText = val; }"
              "function sendSpeed(name,val){ fetch('/set?'+name+'='+val); }"
              "window.addEventListener('DOMContentLoaded',()=>{"
              "  const ls=qs('#left'); const rs=qs('#right'); const ts=qs('#turn');"
              "  ls.addEventListener('input', e=>{ updateLabel('left',e.target.value); sendSpeed('left',e.target.value); });"
              "  rs.addEventListener('input', e=>{ updateLabel('right',e.target.value); sendSpeed('right',e.target.value); });"
              "  ts.addEventListener('input', e=>{ updateLabel('turn',e.target.value); sendSpeed('turn',e.target.value); });"
              "});"
              "</script></head><body>"
              "<h1>TAG RACE COMPETITION</h1>"
              "<h2>Robot Control Panel</h2>"
              "<div class='card'>"
              "  <div class='row'>"
              "    <label>Left Speed</label><input id='left' type='range' min='0' max='255' value='0'/>"
              "    <span id='leftVal'>0</span>"
              "  </div>"
              "  <div class='row'>"
              "    <label>Right Speed</label><input id='right' type='range' min='0' max='255' value='0'/>"
              "    <span id='rightVal'>0</span>"
              "  </div>"
              "  <div class='row'>"
              "    <label>Turn Speed</label><input id='turn' type='range' min='0' max='255' value='0'/>"
              "    <span id='turnVal'>0</span>"
              "  </div>"
              "  <div class='row'>"
              "    <button class='btn' onclick=\"send('forward')\">Forward</button>"
              "    <button class='btn' onclick=\"send('backward')\">Backward</button>"
              "    <button class='btn' onclick=\"send('left')\">Left</button>"
              "    <button class='btn' onclick=\"send('right')\">Right</button>"
              "    <button class='btn' onclick=\"send('stop')\">Stop</button>"
              "  </div>"
              "</div>"
              "</body></html>";

void applyDrive()
{
  switch (driveMode)
  {
    case MODE_FORWARD:
      applyMotorOutputs(leftSpeed, rightSpeed, true, true);
      break;
    case MODE_BACKWARD:
      applyMotorOutputs(leftSpeed, rightSpeed, false, false);
      break;
    case MODE_LEFT: // pivot/turn using turnSpeed
      applyMotorOutputs(turnSpeed, turnSpeed, false, true);
      break;
    case MODE_RIGHT:
      applyMotorOutputs(turnSpeed, turnSpeed, true, false);
      break;
    case MODE_STOP:
    default:
      stop();
      break;
  }
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

  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request) {
    request->send(200, "text/html", html);
  });

  server.on("/drive", HTTP_GET, [](AsyncWebServerRequest *request) {
    if (request->hasParam("mode"))
    {
      String mode = request->getParam("mode")->value();
      if (mode == "forward") driveMode = MODE_FORWARD;
      else if (mode == "backward") driveMode = MODE_BACKWARD;
      else if (mode == "left") driveMode = MODE_LEFT;
      else if (mode == "right") driveMode = MODE_RIGHT;
      else driveMode = MODE_STOP;
      applyDrive();
      request->send(200, "text/plain", "OK");
    }
    else request->send(400, "text/plain", "mode required");
  });

  server.on("/set", HTTP_GET, [](AsyncWebServerRequest *request) {
    bool updated = false;
    if (request->hasParam("left"))
    {
      leftSpeed = constrain(request->getParam("left")->value().toInt(), 0, MAX_SPEED);
      updated = true;
    }
    if (request->hasParam("right"))
    {
      rightSpeed = constrain(request->getParam("right")->value().toInt(), 0, MAX_SPEED);
      updated = true;
    }
    if (request->hasParam("turn"))
    {
      turnSpeed = constrain(request->getParam("turn")->value().toInt(), 0, MAX_SPEED);
      updated = true;
    }
    if (updated)
    {
      applyDrive();
      request->send(200, "text/plain", "OK");
    }
    else request->send(400, "text/plain", "no params");
  });

  server.begin();
  Serial.println("HTTP async server started");
}

void loop()
{
  // Async server does not require handling here
}
