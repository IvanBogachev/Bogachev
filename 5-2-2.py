import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)
dac = [8,11,7,1,0,5,12,6]

def decimal2binary(value):
    return [int(element) for element in  bin(value)[2:].zfill(8)]

x = 0
y = 1
GPIO.setup(dac, GPIO.OUT)
try:
    period = float(input("Период "))
    while True:
        GPIO.output(dac, decimal2binary(x))
        if x == 0:
            y = 1
        elif x == 255:
            y = 0
        if y == 1:
            x += 1
        else:
            x -= 1
        time.sleep(period/512)

    
            
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()