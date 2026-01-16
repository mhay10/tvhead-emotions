#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

// Expressions
#define NEUTRAL "neutral"
#define HAPPY "happy"
#define SAD "sad"
#define ANGRY "angry"
#define SURPRISED "surprised"
#define TIRED "tired"
#define SKEPTICAL "skeptical"
#define LOVE "love"
#define CONFUSED "confused"

// API Server
#define API_BASE_URL "http://192.168.1.246:5000"

bool API_setExpression(WiFiClient client, const char* expression);
bool API_resetExpression(WiFiClient client);