import random

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

#computer is player1, human is player2
#Generate player1 hand
player1 = random.randint(0,2)

#ask for input
player2 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

#print player1 choice

if player1 == 0:
    print(f"Computer chose rock:")
    print(rock)
elif player1 == 1:
    print(f"Computer chose paper:")
    print(paper)
else:
    print(f"Computer chose scissors:")
    print(scissors)

print("------------------------------")
#print player2 choice
if player2 == 0:
    print(f"You chose rock:")
    print(rock)
elif player2 == 1:
    print(f"You chose paper:")
    print(paper)
elif player2 == 2:
    print("you chose scissors")
    print(scissors)
else:
    print("not in bound, dummy")

#compare hand
if player1 == player2:
    print("Draw")
elif player1==0 and player2==2:
    print("Computer Wins")
elif player1==1 and player2==0:
    print("Computer Wins")
elif player1==3 and player2==1:
    print("Computer Wins")
elif player2 >=3:
    print("dumb dumb dumb")
else:
    print("You win!")
