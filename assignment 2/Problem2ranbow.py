from sense_emu import SenseHat
sense = SenseHat()
sense.clear()
W = (255,255,255)
V = (247, 2, 157)
I = (12, 0, 255)
B = (0, 194, 224)
G = (255, 0, 4)
Y = (255, 250, 0)
O = (255, 97, 0)
R = (255, 0, 4)

RAINBOW = [ R,R,R,R,R,R,R,R,
           R,O,O,O,O,O,O,O,
           R,O,Y,Y,Y,Y,Y,Y,
           R,O,Y,G,G,G,G,G,
           R,O,Y,G,B,B,B,B,
           R,O,Y,G,B,I,I,I,
           R,O,Y,G,B,I,V,V,
           R,O,Y,G,B,I,V,W,
           ]
RAIN = [W,W,W,W,W,W,W,W,
        W,B,W,B,W,B,W,B,
        B,W,B,W,B,W,B,W,
        W,B,W,B,W,B,W,B,
        B,W,B,W,B,W,B,W,
        W,B,W,B,W,B,W,B,
        G,G,G,G,G,G,G,G,
        G,G,G,G,G,G,G,G,
        ]
SUNSHINE = [Y,Y,Y,Y,Y,Y,Y,Y,
            Y,Y,Y,Y,Y,Y,Y,Y,
            Y,Y,Y,Y,Y,Y,Y,Y,
            Y,Y,Y,Y,Y,Y,Y,Y,
            Y,Y,Y,Y,Y,Y,Y,Y,
            Y,Y,Y,Y,Y,Y,Y,Y,
            G,G,G,G,G,G,G,G,
            G,G,G,G,G,G,G,G,
            ]
SNOW = [W,W,W,W,W,W,W,W,
        W,W,W,W,W,W,W,W,
        W,W,W,W,W,W,W,W,
        W,W,W,W,W,W,W,W,
        W,W,W,W,W,W,W,W,
        W,W,W,W,W,W,W,W,
        G,G,G,G,G,G,G,G,
        G,G,G,G,G,G,G,G,
        ]
while 1:
    temp =sense.get_temperature()
    humidity=sense.get_humidity()
    print(temp)
    print(humidity)
    if temp > 20 and humidity >80 :
        sense.set_pixels(RAINBOW)
        continue
    elif (temp > 20 and temp <25) and (humidity >60 and humidity <80):
        sense.set_pixels(RAIN)
        continue
    elif (temp > 30 and temp <50) and (humidity >40 and humidity <60):
        sense.set_pixels(SUNSHINE)
        continue
    else :
        sense.set_pixels(SNOW)
        continue
