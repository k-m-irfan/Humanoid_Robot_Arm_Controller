<p align = "right">
<img src="https://api.visitorbadge.io/api/visitors?path=https://github.com/k-m-irfan/Humanoid_Robot_Arm_Controller%2F&label=VIEWS&countColor=%2337d67a" align="right">
<a href="https://doi.org/10.1016/j.sna.2024.115019"><img src="https://img.shields.io/badge/Paper-414141" align="left" height="30px"></a>
</p>
<br>

# Introduction
![image](https://github.com/user-attachments/assets/714ed050-902c-46ee-afb7-702d65a2b8a0)
This paper introduces a wearable robotic controller for teleoperation, capturing up to seventeen degrees of freedom (DoF) in human arm-hand movements. The system consists of a master side with IMU sensors for arm orientation and potentiometers for finger motion, and a slave side that calculates joint angles. Data is transmitted via RF, with the slave side translating sensor readings into joint angles using a Relative Orientation Vector approach. These joint angles are mapped to a robot arm-hand model, validated through simulations and experiments, showcasing effective remote control of robotic limbs.

#
# Demo Video: [[VIDEO]](https://drive.google.com/file/d/1db3AKoa-e-W6HV--gTsGyHlMbmqHGK8M/view)

# Components.
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

**<ins>5. Charger + DC-DC Step-Up Module</ins>**

- Charges a 3.7V Li-ion battery and boosts its output voltage to 6V-27V for Arduino Nano compatibility.

**<ins>6. Lithium-Ion Battery (3.7V)</ins>**

- Rechargeable battery for portable power; output boosted by the DC-DC step-up module.
  
**<ins>7. Potentiometer</ins>**

- Adjustable resistor for variable output voltage, useful for control inputs.

# Schematic for sensor interface and control.
**Reference Module:**

![reference module schematic](https://github.com/user-attachments/assets/d56d033a-2f0b-4a6d-a230-f4dae4044baa)
![reference module pcb](https://github.com/user-attachments/assets/91dc172d-0a0a-4724-a2dc-f2c8518e0fea)

**Palm Module:**

![palm module schematic](https://github.com/user-attachments/assets/634c17da-0cc0-4486-b1f0-364b6890b712)
![palm module pcb](https://github.com/user-attachments/assets/73ccbfe4-abd4-4b09-9dcf-7b95b35a1bf5)

**Receiver Module:**

![receiver schematic](https://github.com/user-attachments/assets/a51928ca-a00d-42aa-a243-14f4f337553e)
![receiver pcb](https://github.com/user-attachments/assets/eac086eb-ccc3-4661-90b0-06d74d1bf56b)

