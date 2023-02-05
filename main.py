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

#Write your code below this line 👇
compo = [rock , paper, scissors]
player_choice =int( input("Type 0 for Rock 1 for Paper 2 for Scissor "))
computer = random.randint(0,2)
computer_choice = compo[computer]
player_choice = compo[player_choice]
print(f"Your Choice :\n {player_choice}")
print(f"computer Choice :\n {computer_choice}")
if player_choice == computer_choice:
  print("retry")
elif player_choice[0] != computer_choice[1] or player_choice[0] != computer_choice[2]:
  print("You won!!")
elif player_choice[1] != computer_choice[0]:
  print("you won!!")
elif player_choice[1] != computer_choice[2]:
  print("you loose")
elif player_choice[2] != computer_choice[0]:
  print("You loose")
elif player_choice[2] != computer_choice[1]:
  print("You won!!")


