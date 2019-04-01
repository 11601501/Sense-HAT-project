from sense_emu import SenseHat
from time import sleep
sense = SenseHat()
y = [255, 255, 255]
e = [0, 0, 0]
O = [0, 0, 255]
A = 0
B = 0
path = [
  y,y,y,e,e,e,e,e,
  e,e,y,e,e,e,e,e,
  e,e,y,e,e,e,e,e,
  e,e,y,y,y,y,y,e,
  e,e,e,e,e,e,y,e,
  e,e,e,e,e,e,y,e,
  e,e,e,e,y,y,y,e,
  e,e,e,e,y,e,e,e
]
while 1:
  sense.set_pixels(path)
  sense.set_pixel(A, B, O)
  pitch = sense.get_orientation()['pitch']
  roll = sense.get_orientation()['roll']
  print('Pitch:', pitch)
  print('Roll:', roll)
  if 270 < pitch < 315 and A < 7:
    A += 1
  if 45 < pitch < 90 and A > 0:
    A -= 1
  if 45 < roll < 90 and B < 7:
    B += 1
  if 270 < roll < 315 and B > 0:
    B -= 1
  current = sense.get_pixel(A,B)
  if current == e:
    A = 0
    B = 0
  sleep(0.5)
