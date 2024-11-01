# Introduction
![image](https://github.com/user-attachments/assets/714ed050-902c-46ee-afb7-702d65a2b8a0)
This paper introduces a wearable robotic controller for teleoperation, capturing up to seventeen degrees of freedom (DoF) in human arm-hand movements. The system consists of a master side with IMU sensors for arm orientation and potentiometers for finger motion, and a slave side that calculates joint angles. Data is transmitted via RF, with the slave side translating sensor readings into joint angles using a Relative Orientation Vector approach. These joint angles are mapped to a robot arm-hand model, validated through simulations and experiments, showcasing effective remote control of robotic limbs.
#
# Demo Video: [[VIDEO]](https://drive.google.com/file/d/1db3AKoa-e-W6HV--gTsGyHlMbmqHGK8M/view)
#


# Components
[**1. Adafruit BNO055 Absolute Orientation Sensor**](https://learn.adafruit.com/adafruit-bno055-absolute-orientation-sensor/arduino-code?view=all)

- A Bosch-manufactured sensor that uses a MEMS accelerometer, magnetometer, and gyroscope with an ARM Cortex-M0 processor for sensor fusion. Provides data as Euler angles, quaternions, angular velocity, linear and gravitational acceleration, magnetic field strength, and temperature.
- Pinout: Power (Vin, GND), I2C (SCL, SDA)

[**2. NRF24L01 Transceiver Module**](https://howtomechatronics.com/tutorials/arduino/arduino-wireless-communication-nrf24l01-tutorial/)

- A 2.4 GHz transceiver with up to 2 Mbps baud rate and 100 m range in open space. Supports SPI communication and can form networks of up to 3,125 nodes.
- Pinout: SPI (MOSI, MISO, SCK), CSN, CE, IRQ (optional)

[**3. 16-Channel Analog Multiplexer (74HCT4067)**](https://www.instructables.com/Tutorial-74HC4067-16-Channel-Analog-Multiplexer-De/)

- Bidirectional switch for analog signal control across 16 channels. Selection depends on digital signals (S0-S3).
- Pinout: Control pins (S0-S3), analog channels

[**4. Arduino Nano**](https://docs.arduino.cc/hardware/nano/)

- Compact microcontroller board with 8 analog and 12 digital I/O pins, ideal for prototyping.
- Pinout: Power and I/O pins

**5. Charger + DC-DC Step-Up Module**

- Charges a 3.7V Li-ion battery and boosts its output voltage to 6V-27V for Arduino Nano compatibility.

**6. Lithium-Ion Battery (3.7V)**

- Rechargeable battery for portable power; output boosted by the DC-DC step-up module.
  
**7. Potentiometer**

- Adjustable resistor for variable output voltage, useful for control inputs.

# Schematic for sensor interface and control.
**Reference Module:**
**Palm Module:**
**Receiver Module:**
