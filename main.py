"""
MicroPython Piano
By Khoa Hoang

Use hotkey 1-8 to play
"""

from machine import Pin, PWM
from time import sleep
from notes import *

#Number of buttons
number_of_buttons = 8

#Button pins
button_pin = [26, 22, 21, 20, 19, 18, 17, 16]

#Setup buzzer
buzzer_pin = 0
buzzer = PWM(Pin(buzzer_pin, Pin.OUT))

#Notes
note = [note_C4, note_D4, note_E4, note_F4, note_G4, note_A4, note_B4, note_C5]

#Dictionary to assign note to each button
button_note = dict()

#Function for handling button press event
def button_handler(pin):
    debounce_time = 0.01   # Debounce time (s)
    sleep(debounce_time)
    if pin.value() == 0:
        play_note(button_note[pin])
        sleep(0.1)
        be_quiet()

#Function to setup button
def setup():
    global button_note
    #Button setup
    for i in range(number_of_buttons):
        btn = Pin(button_pin[i], Pin.IN, Pin.PULL_UP)
        #Assign interrupt for each button
        btn.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)
        #Assign note for each button
        button_note[btn] = note[i]

def play_note(freq):
    buzzer.duty_u16(1000)   #Turn PWM duty to 50%
    buzzer.freq(freq)

def be_quiet():
    buzzer.duty_u16(0)

setup()