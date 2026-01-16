#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <ArduinoJson.h>
#include "expressions.h"

bool API_setExpression(WiFiClient client, const char* expression) {
  // Connect to server
  HTTPClient http;
  http.begin(client, API_BASE_URL "/set-expression");

  // Create JSON body
  StaticJsonDocument<200> data;
  data["expression"] = expression;

  // Serialize and send request
  String body;
  serializeJson(data, body);
  int responseCode = http.POST(body);

  // Return success (200 = true)
  return responseCode == 200;
}


bool API_resetExpression(WiFiClient client) {
  // Connect to server
  HTTPClient http;
  http.begin(client, API_BASE_URL "/reset-expression");

  // Serialize and send request
  int responseCode = http.POST("");

  // Return success (200 = true)
  return responseCode == 200;
}