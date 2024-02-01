
import os


if __name__ == '__main__':
 print("Welcome to Robospeaker 1.1 created by Anshuman")
 while True:
  x = input("Enter what you want me to speak")
  if x == "quit":
   os.system("say 'Bye Bye'")
   break
  command = f"say {x}"
  os.system(command)


