#!/usr/bin/python
import sys
import Adafruit_DHT
import Adafruit_CharLCD as LCD

from RPLCD import CharLCD


lcd = LCD.Adafruit_CharLCDPlate()

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)


    lcd.message("Temp: %d C\n" % temperature)
    lcd.message("Humidity: %d %%" % humidity)
