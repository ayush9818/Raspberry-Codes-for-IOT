import RPi.GPIO as GPIO
import time

rs= 7
en =8
d0=25
d1=24
d2=23
d3=18

#low = False
#high = True

def ini():
    lcdcmd(0x33)
    lcdcmd(0x32)
    lcdcmd(0x01)
    lcdcmd(0x28)
    lcdcmd(0x80)
    lcdcmd(0x0e)
    lcdcmd(0x06)

def lcdcmd(value):
    GPIO.output(rs,False)
    
    GPIO.output(d0,False)
    GPIO.output(d1,False)
    GPIO.output(d2,False)
    GPIO.output(d3,False)
    
    if value&0x10==0x10:
        GPIO.output(d0,True)
    if value&0x20==0x20:
        GPIO.output(d1,True)
    if value&0x40==0x40:
        GPIO.output(d2,True)
    if value&0x80==0x80:
        GPIO.output(d3,True)

    GPIO.output(en,True)
    time.sleep(0.001)
    GPIO.output(en,False)
    time.sleep(0.001)

    GPIO.output(d0,False)
    GPIO.output(d1,False)
    GPIO.output(d2,False)
    GPIO.output(d3,False)
    
    if value&0x01==0x01:
        GPIO.output(d0,True)
    if value&0x02==0x02:
        GPIO.output(d1,True)
    if value&0x04==0x04:
        GPIO.output(d2,True)
    if value&0x08==0x08:
        GPIO.output(d3,True)

    GPIO.output(en,True)
    time.sleep(0.001)
    GPIO.output(en,False)
    time.sleep(0.001)
    
def lcddata(value):
    GPIO.output(rs,True)
    
    GPIO.output(d0,False)
    GPIO.output(d1,False)
    GPIO.output(d2,False)
    GPIO.output(d3,False)
    
    if value&0x10==0x10:
        GPIO.output(d0,True)
    if value&0x20==0x20:
        GPIO.output(d1,True)
    if value&0x40==0x40:
        GPIO.output(d2,True)
    if value&0x80==0x80:
        GPIO.output(d3,True)

    GPIO.output(en,True)
    time.sleep(0.001)
    GPIO.output(en,False)
    time.sleep(0.001)

    GPIO.output(d0,False)
    GPIO.output(d1,False)
    GPIO.output(d2,False)
    GPIO.output(d3,False)
    
    if value&0x01==0x01:
        GPIO.output(d0,True)
    if value&0x02==0x02:
        GPIO.output(d1,True)
    if value&0x04==0x04:
        GPIO.output(d2,True)
    if value&0x08==0x08:
        GPIO.output(d3,True)

    GPIO.output(en,True)
    time.sleep(0.001)
    GPIO.output(en,False)
    time.sleep(0.001)

def stri(message):
    
    for i in range (len(message)):
        
        lcddata(ord(message[i]))

if __name__ == '__main__':

    try :
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(rs,GPIO.OUT)
        GPIO.setup(en,GPIO.OUT)
        GPIO.setup(d0,GPIO.OUT)
        GPIO.setup(d1,GPIO.OUT)
        GPIO.setup(d2,GPIO.OUT)
        GPIO.setup(d3,GPIO.OUT)
        ini()
        while(True):
            lcdcmd(0x01)
            lcdcmd(0x80)
            stri("welcome to cetpa ")
            time.sleep(2)
            lcdcmd(0xc0)
            stri("welcome cetpians")
            time.sleep(2)
            print("hello")
        
    except KeyboardInterrupt:
        pass
    
    
