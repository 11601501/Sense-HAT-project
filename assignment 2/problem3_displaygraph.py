import pygal

temp = []

file = open('weather.txt', 'r')

for line in file.read().splitlines():
  if line:
    temp.append( float(line) )
file.close()

chart = pygal.Line()
chart.title = 'Weather'
chart.x_labels = range(1, len(temp) + 1)
chart.add('temp', temp)
chart.render()

