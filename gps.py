import RPi.GPIO as led
import time 
led.setwarnings(False)
led.setmode(led.BCM)
led.setup(2,led.OUT)
import serial
ser=serial.Serial(port='/dev/ttyS0',baudrate=9600,parity=serial.PARITY_NONE,timeout=1)


data=[]

while(1):
    data=[]
    a=''
    data.append(ser.read().decode('UTF-8'))
    for i in range(len(data)):
        a+=data[i]
        print(a,end='')
    time.sleep(0.1)
    
