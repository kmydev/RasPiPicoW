from machine import Pin
import utime

led = Pin(7, Pin.OUT)

while (True):
    led.value(1)
    utime.sleep(0.5)
    led.value(0)
    utime.sleep(0.5)

