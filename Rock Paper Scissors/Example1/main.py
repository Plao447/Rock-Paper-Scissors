import random
from itertools import count

rock = "👊 👊 👊"

paper = "🤚 🤚 🤚"

scissors = "✌️ ✌️ ✌️"

win, lose = 0, 0
count = 0

while True:
    image = [rock, paper, scissors]

    print("What do you choose? \n(0) Rock (1) Paper (2) Scissors")
    user = int(input("Enter your choice: "))
    print(image[user])
    count += 1

    com = random.randint(0,2)
    print("Computer Choose: ")
    print(image[com])


    if user == com:
      print("It's a draw\n")
    elif user == 0 and com == 2:
      print("You win!\n")
      win += 1
    elif user == 1 and com == 0:
      print("You win!\n")
      win += 1
    elif user == 2 and com == 1:
      print("You win!\n")
      win += 1
    else:
      print("You lose\n")
      lose += 1

    print(f"YOU {win} : COM {lose}\n--------")

    if count == 5:
        ply_again = input("Play again? (y/n) : ").lower()
        if ply_again == 'y':
            count = 0
        else:
            print("---------")
            print("Thank for playing!")
            break