# Arduino Soil Moisture Monitoring and Water Pump Control System with ESP8266

This project uses an Arduino Uno and an ESP8266 module to monitor soil moisture levels and control a water pump based on the detected moisture. The data is sent to a server for further processing or visualization.


<details>
 <summary>Components Used</summary>

- Arduino Uno
  
- ESP8266 Wi-Fi module
  
- Soil Moisture Sensor
  
- Relay Module
  
- Jumper Wires
  
- Water Pump

</details>

<details>
  <summary>Connections</summary>
  
Soil Moisture Sensor:

VCC to 3.3V or 5V on the Arduino

GND to GND on the Arduino

Analog output to A0 on the Arduino

Connect the water pump to the relay module according to the relay's specifications.

</details>

<details>
  <summary>Relay Module</summary>

VCC to 5V on the Arduino

GND to GND on the Arduino

IN to pin 8 on the Arduino

</details>

<details>
  <summary>ESP8266 Wi-Fi Module</summary>

VCC to 3.3V (Note: Ensure the ESP8266 is powered by a 3.3V regulator)

GND to GND on the Arduino

RX to pin 1 (TX) on the Arduino (use a voltage divider if needed)

TX to pin 0 (RX) on the Arduino

</details>

<details>
  <summary>Water Pump</summary>
  
  Connect the water pump to the relay module according to the relay's specifications.
  
</details>

<details>
  <summary>Instructions</summary>

Install the Arduino IDE: Download and install the Arduino IDE on your computer.

Connect the Arduino Uno: Use a USB cable to connect your Arduino Uno to your computer.

Upload the Code:

Open the Arduino IDE.

Copy the provided code into a new sketch.

Select your board and port from the Tools menu.

Click the Upload button to upload the code to the Arduino.

Wiring: Connect the components as described in the "Connections" section.

Run the System:

Open the Serial Monitor in the Arduino IDE to see the soil moisture values being read and the HTTP responses.

The water pump will turn on if the soil moisture level is below the threshold (300 in this case).

The ESP8266 module will send the soil moisture data to the specified server endpoint.

</details>
