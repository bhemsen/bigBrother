#!/usr/bin/env python
# -*- coding: utf8 -*-
import time
import RPi.GPIO as GPIO
import MFRC522
import signal
import busio
import board as board1
import adafruit_character_lcd.character_lcd_i2c as character_lcd

# Definiere LCD Zeilen und Spaltenanzahl.
lcd_columns = 16
lcd_rows    = 2
# Initialisierung I2C Bus
i2c = busio.I2C(board1.SCL, board1.SDA)
# Festlegen des LCDs in die Variable LCD
lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows, 0x21)

continue_reading = True
 
def entry(sample_var):
    # Skript starten, Daten loggen, etc.
    print("Moooooin Meister")
    lcd.backlight = True
    lcd.message = ("Geiler Typ\nViel Erfolg!")
    time.sleep(5.0)
    lcd.backlight = False
    lcd.clear()
    MIFAREReader.MFRC522_StopCrypto1()

def noentry(sample_var1):
    print ("Kein Zutritt!")
    lcd.backlight = True
    lcd.message = ("Kein Zutritt\nFrag den Admin")
    time.sleep(5.0)
    lcd.backlight = False
    lcd.clear()
    MIFAREReader.MFRC522_StopCrypto1()
    
def nichtbekannt(sample_var2):
    print("Karte nicht bekannt")
    lcd.backlight = True
    lcd.message = ("----!Hau ab!----\n----!SOFORT!----")
    lcd.backlight = False
    time.sleep(1.0)
    lcd.backlight = True
    time.sleep(1.0)
    lcd.backlight = False
    time.sleep(1.0)
    lcd.backlight = True
    time.sleep(1.0)
    lcd.backlight = False
    time.sleep(1.0)
    lcd.backlight = True
    time.sleep(1.0)
    lcd.backlight = False
    lcd.clear()
    MIFAREReader.MFRC522_StopCrypto1()
# ...
 
MIFAREReader = MFRC522.MFRC522()
# die ersten 9 Ziffern sind der Authentifizierungscode
authcode = [34, 36, 37, 77, 55, 1, 1, 1, 1]
noauthcode = [10, 10, 10, 10, 10, 10, 10, 10, 10]
#unbekannt = [0, 0, 0, 0, 0, 0, 0, 0, 0]
 
try:
    while True:
        # Scan for cards    
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        # If a card is found
        if status == MIFAREReader.MI_OK:
            # Get the UID of the card
            (status,uid) = MIFAREReader.MFRC522_Anticoll()
            # This is the default key for authentication
            key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
            # Select the scanned tag
            MIFAREReader.MFRC522_SelectTag(uid)
            # Authenticate
            status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
            # Check if authenticated
            if status == MIFAREReader.MI_OK:
                # Read block 8
                data = MIFAREReader.MFRC522_Read(8)
                if data[:9] == authcode:
                    entry(data)
                    
                elif data[:9] == noauthcode:
                    noentry(data)
                    
                else:
                    nichtbekannt(data)
              
                   
except KeyboardInterrupt:
    print("Abbruch")
    GPIO.cleanup()