import keyboard

def motor_f():
  print("motor going forward")

def motor_b():
  print("motor going backward")

def motor_l():
  print("wheels turning left")

def motor_r():
  print("wheels turning right")

def main():
  while True:
    print(keyboard.read_key())
    if keyboard.read_key() == 'w':
       motor_f()
    if keyboard.read_key() == 's':
      motor_b()
    if keyboard.read_key() == 's':
      motor_l()
    if keyboard.read_key() == 's':
      motor_r()

if __name__ == '__main__':
  main()
