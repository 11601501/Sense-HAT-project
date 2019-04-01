from sense_hat import *
#import maze
rooms = {
         'Blue' : { 
                  'south' : 'Red',
                  'west'  : 'Yellow',
                },        

            'Red' : { 
                  'north' : 'Blue',
                },
                
            'Yellow' : { 
                  'east'  : 'Blue',
                  'south' : 'Green',
                },
                
            'Green' : {    
                }

         }
         
colours = { 'Blue' : [0, 0, 255], 
            'Red' : [255, 0, 0],
            'Yellow' : [255, 255, 0],
            'Green' : [0, 255, 0] 
          }

def start():
  
  print('GREEN ROOM GAME')
  Status()

def Status():
   print( currentRoom + ' room')
    if(currentRoom != 'Green'):
    print("Exits: ")
    print(*rooms[currentRoom].keys(), sep=', ')
def Colour():
  return colours[currentRoom]
currentRoom = 'Blue'
def walk(dir):
  global currentRoom
  if dir in rooms[currentRoom]:
    currentRoom = rooms[currentRoom][dir]
    print("You walk", dir)
  
  else:
    print('wrong way')
    
  Status()
  
  return currentRoom
  
def escaped():
  return currentRoom == 'Green'


start()
sense = SenseHat()
sense.clear()

sense.set_rotation(90)
           
while True:
    
  heading = sense.get_compass()

  if heading < 45 or heading > 315:
    dir = 'north'
  elif heading < 135:
    dir = 'east'
  elif heading < 225:
    dir = 'south'
  else:
    dir = 'west'
    
  sense.show_letter(dir[0].upper(), text_colour=getColour())
  
  for e in sense.stick.get_events():
    if e.action == ACTION_PRESSED and e.direction == DIRECTION_MIDDLE:
      maze.walk(dir)
      
  if maze.escaped():
    sense.clear(0, 255, 0)
    break;
