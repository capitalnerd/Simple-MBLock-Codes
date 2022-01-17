from mblock import event
import random
import time
# initialize variables
ball_speed

@event.received('game start')
def on_received():
  sprite.set_variable('ball-speed', 2)
  sprite.x = 0
  sprite.y = 0
  sprite.direction = random.randint(-180, 180)
  time.sleep(1)
  while True:
    sprite.forward(sprite.get_variable('ball-speed'))
    sprite.bounce()
    if sprite.touching('mouse') or sprite.touching('mouse'):
      sprite.direction = sprite.direction * -1

    if sprite.x > 230 or sprite.x < -230:
      sprite.broadcast(str('game start'))

@event.greenflag
def on_greenflag():
  sprite.rotation_mode("no-rotate")
  sprite.broadcast(str('game start'))
