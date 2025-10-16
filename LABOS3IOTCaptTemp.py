from lcd1602 import LCD1602
from machine import I2C,Pin,ADC
from utime import sleep

def main():
    
    ROTARY_ANGLE_SENSOR = ADC(0)
    i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)  #definition du display
    d = LCD1602(i2c, 2, 16) #defintion du display

    d.display() #enable dsiplay
#     sleep(1)
# 
#     d.clear()
#     d.print('Coucou hibou') #display
# 
#     sleep(1)
#     d.setCursor(0,1)
#     d.print('world')

    while True:
        sleep(1)
        d.clear()
        d.setCursor(0, 0)
        d.print(str(ROTARY_ANGLE_SENSOR.read_u16()))
        sleep(1)

##execute
main()