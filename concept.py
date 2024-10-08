import keyboard

def motor_f():
  print("motor going forward")

def main():
  while True:
    print(keyboard.read_key())
    if keyboard.read_key() == 'w':
      motor_f()
    if keyboard.read_key() == 'p':
      break

if __name__ == '__main__':
  main()
