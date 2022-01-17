from mblock import event
# initialize variables
speed = 1.5
@event.keypressed('up arrow')
def on_keypressed():
  for count in range(10):
    sprite.y = sprite.y + sprite.get_variable('speed')

@event.keypressed('down arrow')
def on_keypressed1():
  for count2 in range(10):
    sprite.y = sprite.y + sprite.get_variable('speed') * -1
