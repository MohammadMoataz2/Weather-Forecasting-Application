/**
 * DHT11 Sensor Reader
 * This sketch reads temperature and humidity data from the DHT11 sensor and prints the values to the serial port.
 * It also handles potential error states that might occur during reading.
 *
 * Author: Dhruba Saha
 * Version: 2.1.0
 * License: MIT
 */

// Include the DHT11 library for interfacing with the sensor.
#include <DHT11.h>
#include "time.h"

#define trig 11
#define echo 12

String ledValue = "off";


int distance =0,t = 0;

// Create an instance of the DHT11 class.
// - For Arduino: Connect the sensor to Digital I/O Pin 2.
// - For ESP32: Connect the sensor to pin GPIO2 or P2.
// - For ESP8266: Connect the sensor to GPIO2 or D4.
DHT11 dht11(2);

void setup() {
    // Initialize serial communication to allow debugging and data readout.
    // Using a baud rate of 9600 bps.
    Serial.begin(9600);
    pinMode(trig,OUTPUT);
    pinMode(echo,INPUT);
    pinMode(4,OUTPUT);
    
    // Uncomment the line below to set a custom delay between sensor readings (in milliseconds).
    // dht11.setDelay(500); // Set this to the desired delay. Default is 500ms.
}

void loop() {
    int temperature = 0;
    int humidity = 0;

    // Attempt to read the temperature and humidity values from the DHT11 sensor.
    int result = dht11.readTemperatureHumidity(temperature, humidity);

    // Check the results of the readings.
    // If the reading is successful, print the temperature and humidity values.
    // If there are errors, print the appropriate error messages.
    if (result == 0) {


digitalWrite(trig,LOW);
delayMicroseconds(5);
digitalWrite(trig,HIGH);
delayMicroseconds(10);

digitalWrite(trig,LOW);



t = pulseIn(echo,HIGH);


distance = t/57;

if (distance < 10) {

  digitalWrite(4,HIGH);

 ledValue = "On";

}

if (distance >= 10) {

  digitalWrite(4,LOW);
  ledValue = "Off";


}



 Serial.print("{\"Hum\":");
 Serial.print(humidity);
 Serial.print(",\"Temp\":");
 Serial.print(temperature);
 Serial.print(",\"dist\":");
 Serial.print(distance);

Serial.print(",\"led\":");
 Serial.print("\""+ledValue +"\"");
 Serial.println("}");


        
    } else {
        // Print error message based on the error code.
        Serial.println(DHT11::getErrorString(result));
    }
}