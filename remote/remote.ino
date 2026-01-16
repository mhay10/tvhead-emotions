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
  { D1, HAPPY },
  { D2, SAD },
  { D5, ANGRY },
  { D6, SURPRISED },
};

// Status LED
const int statusLed = D0;

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
  for (int i = 0; i < numButtons; i++) {
    ButtonMap button = buttons[i];
    if (digitalRead(button.pin) == 0) {
      API_setExpression(client, button.expression);
      delay(200);
    }
  }
}

void showConnectingStatus() {
  digitalWrite(statusLed, 0);
  delay(250);
  digitalWrite(statusLed, 1);
  delay(250);
}

void showConnectedStatus() {
  for (int i = 0; i < 4; i++) {
    digitalWrite(statusLed, 0);
    delay(100);
    digitalWrite(statusLed, 1);
    delay(100);
  }
}