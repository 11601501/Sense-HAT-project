from sense_emu import SenseHat
import time

sense = SenseHat()
sense.clear()
while 1:
    for i in range(0,10):
        c =str(i)
        sense.show_letter(c)
        
        time.sleep(1)
        continue
    
