#Rock Paper Scissors
#Karis
#Play Rock Paper Scissors against the computer

#init
import random

#funcs
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
def rps():
    player_wins = 0
    computer_wins = 0
    god_mode = False
    while True:

        choice = input("Choose: (Rock/Paper/Scissors): ").lower()
        if choice == 'karisisthebest':
            print("You have entered God mode.")
            god_mode = True
            print("Please choose again!")
            continue

        if choice != 'rock' and choice != 'paper' and choice != 'scissors':
            print("Please enter a correct input next time!")
            continue
        if not god_mode:
            computer_choice = random.randint(1, 3)
        #1 = rock, 2 = paper, 3 = scissors
        if computer_choice == 1:
            computer_choice = 'rock'
            print(rock)
        elif computer_choice == 2:
            computer_choice = 'paper'
            print(paper)
        elif computer_choice == 3:
            computer_choice = 'scissors'
            print(scissors)
        if god_mode == True:
            if choice == 'paper':
                computer_choice = 'rock'
                print(rock)
            elif choice == 'scissors':
                computer_choice = 'paper'
                print(paper)
            elif choice == 'rock':
                computer_choice = 'scissors'
                print(scissors)



            print(f"The computer chose: {computer_choice}")
            print("Player wins!")
            player_wins += 1
        else:
            print(f"The computer chose: {computer_choice}")
            if computer_choice == choice:
                print("Draw.")

            elif computer_choice == 'rock' and choice == 'paper':
                print("Player wins!")
                player_wins += 1

            elif computer_choice == 'rock' and choice == 'scissors':
                print("Computer wins!")
                computer_wins += 1

            elif computer_choice == 'paper' and choice == 'rock':
                print("Computer wins!")
                computer_wins += 1

            elif computer_choice == 'paper' and choice == 'scissors':
                print("Player wins!")
                player_wins += 1

            elif computer_choice == 'scissors' and choice == 'paper':
                print("Computer wins!")
                computer_wins += 1

            elif computer_choice == 'scissors' and choice == 'rock':
                print("Player wins!")
                player_wins += 1

            else:
                print("You somehow broke the game, please try again next time!")

        print(f"Player wins: {player_wins}. Commputer wins: {computer_wins}.")
        play = input("Would you like to keep playing? (yes/no): ")
        if play == 'yes':
            continue
        else:
            exit()

#main
rps()
