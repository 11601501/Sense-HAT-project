from sense_emu import *
from time import sleep

sense = SenseHat()

while 1:
  f1 = open('weather.txt', 'a')
  f1.write(str(sense.get_temperature()))
  f1.write('\n')
  f1.close()
  sleep(5)

