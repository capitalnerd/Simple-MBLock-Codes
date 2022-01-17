from mblock import event
@event.greenflag
def on_greenflag():
  while True:
    sprite.y = sprite.mousey * 1.5
