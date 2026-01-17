#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <ArduinoJson.h>
#include "expressions.h"

// Hand Configuration (true = right, false = left)
#define IS_RIGHT_HAND true

// Mapped Expression Structure
struct ButtonMap {
  int pin;
  const char* expression;
};

// Wifi Information
const char WIFI_SSID[] = "theghetto";
const char WIFI_PSK[] = "Poggibonsi";
WiFiClient client;

// Button pins
const int numButtons = 4;
ButtonMap buttons[numButtons] = {
  { D1, IS_RIGHT_HAND ? HAPPY : TIRED },
  { D2, IS_RIGHT_HAND ? SAD : SKEPTICAL },
  { D5, IS_RIGHT_HAND ? ANGRY : LOVE },
  { D6, IS_RIGHT_HAND ? SURPRISED : CONFUSED },
};

// Status LED pin
const int statusLed = D0;

// States for button presses
int prevButtonPress = -1;

void setup() {
  // Setup pins
  for (int i = 0; i < numButtons; i++) {
    ButtonMap button = buttons[i];
    pinMode(button.pin, INPUT_PULLUP);
  }
  pinMode(statusLed, OUTPUT);

  // Start Wifi connection
  WiFi.begin(WIFI_SSID, WIFI_PSK);
  while (WiFi.status() != WL_CONNECTED)
    showConnectingStatus();
  showConnectedStatus();
}

void loop() {
  // Handle button presses
  for (int i = 0; i < numButtons; i++) {
    ButtonMap button = buttons[i];
    if (digitalRead(button.pin) == 0 && button.pin != prevButtonPress) {
      // Only send request when button first pressed
      API_setExpression(client, button.expression);
      prevButtonPress = button.pin;
    }
  }

  // Handle button releases
  for (int i = 0; i < numButtons; i++) {
    ButtonMap button = buttons[i];
    if (digitalRead(button.pin) == 1 && button.pin == prevButtonPress) {
      // Only send request when button released
      API_resetExpression(client);
      prevButtonPress = -1;
    }
  }
}

void showConnectingStatus() {
  digitalWrite(statusLed, 0);
  delay(500);
  digitalWrite(statusLed, 1);
  delay(500);
}

void showConnectedStatus() {
  for (int i = 0; i < 3; i++) {
    digitalWrite(statusLed, 0);
    delay(100);
    digitalWrite(statusLed, 1);
    delay(100);
  }
}