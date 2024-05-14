import random

# Toss a Coin Program.
rand_integer = random.randint(0, 1)
if rand_integer == 0:
    print("Tails.")
else:
    print("Heads.")

# Random bill payment program.
names = ["Angela", "Ben", "Jenny", "Micheal", "Chloe"]

payer = random.choice(names)
print(f"{payer} is going to pay the bill!")

# Rock, Paper, Scissors game program.
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

my_gesture = int(input("Which do you want to play?\n"))
if my_gesture < 0 or my_gesture >= 3:
    print("Invalid input, Try again.")
else:
    print(game_images[my_gesture])
    comp = random.randint(0, 2)
    print(game_images[comp])

    if my_gesture == 0 and comp == 1:
        print("You Lose!")
    elif my_gesture == 1 and comp == 2:
        print("You Lose!")
    elif my_gesture == 2 and comp == 0:
        print("You Lose!")

    elif my_gesture == 1 and comp == 0:
        print("You Win!")
    elif my_gesture == 2 and comp == 1:
        print("You Win!")
    elif my_gesture == 0 and comp == 2:
        print("You Win!")

    elif my_gesture == 0 and comp == 0:
        print("Its a Draw!")
    elif my_gesture == 1 and comp == 1:
        print("Its a Draw!")
    elif my_gesture == 2 and comp == 2:
        print("Its a Draw!")
