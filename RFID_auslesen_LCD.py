#!/usr/bin/env python
# -*- coding: utf8 -*-
import time
import RPi.GPIO as GPIO
import MFRC522
import signal
import busio
import board as board1
import adafruit_character_lcd.character_lcd_i2c as character_lcd
import Database 
from Database import Database
import ast


# Definiere LCD Zeilen und Spaltenanzahl.
lcd_columns = 16
lcd_rows    = 2
# Initialisierung I2C Bus
i2c = busio.I2C(board1.SCL, board1.SDA)
# Festlegen des LCDs in die Variable LCD
lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows, 0x21)

continue_reading = True
 
def entry(name):
    # Skript starten, Daten loggen, etc.
    lcd.backlight = True
    lcd.message = (name +", du geiler Typ\nViel Erfolg!")
    time.sleep(5.0)
    lcd.backlight = False
    lcd.clear()
    MIFAREReader.MFRC522_StopCrypto1()

def noentry(name):
    print ("Kein Zutritt!")
    lcd.backlight = True
    lcd.message = ("Kein Zutritt, "+ name + "\nFrag den Admin")
    time.sleep(5.0)
    lcd.backlight = False
    lcd.clear()
    MIFAREReader.MFRC522_StopCrypto1()
    
def unknown():
    print("Karte nicht bekannt")
    lcd.backlight = True
    lcd.message = ("----!Hau ab!----\n----!SOFORT!----")
    lcd.backlight = False
    time.sleep(1.0)
    for i in range(4):
        lcd.backlight = True
        time.sleep(.7)
        lcd.backlight = False
        time.sleep(.7)
    lcd.clear()
    MIFAREReader.MFRC522_StopCrypto1()

def compareKeyWithDatabaseKeys(key):
    db = Database("localhost", "webadmin", "password", "sensoro")
    result = db.getAllowdRFIDS()

    for i in range(len(result)):
        respondKey = ast.literal_eval(result[i][0])
        allowedKey = respondKey[:9]
        securityLevel = result[i][2]
        name = result[i][1]
        print(allowedKey)
        if allowedKey == key:
            if securityLevel == 2:
                entry(name)
                access = "granted"
                db.logEntry(name , key, access)
                return

            else:
                noentry(name)
                access = "denied"
                db.logEntry(name , key, access)
                return

    unknown()
    name = "unknown"
    access = "denied"
    db.logEntry(name , key, access)


# ...
 
MIFAREReader = MFRC522.MFRC522()
# die ersten 9 Ziffern sind der Authentifizierungscode
 
try:
    while True:
        # Scan for cards    
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        # If a card is found
        if status == MIFAREReader.MI_OK:
            # Get the UID of the card
            (status,uid) = MIFAREReader.MFRC522_Anticoll()
            print(uid)
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
                compareKeyWithDatabaseKeys(data[:9])
                       
except KeyboardInterrupt:
    print("Abbruch")
  #  GPIO.cleanup()