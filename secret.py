#Karis
#secret.py
#Asks the player to guess a secret number

#init
import random

#funcs

def main():
    difficulty = input("Would you like Easy, Medium, or Hard difficulty? (E/M/H): ").lower()
    if difficulty == 'e':
        secret_num = random.randint(0, 10)
        print("Your range is 0 - 10")
        high_dist = 5
        med_dist = 3
    elif difficulty == 'm':
        secret_num = random.randint(0, 500)
        print("Your range is 0 - 500")
        high_dist = 250
        med_dist = 100
    elif difficulty == 'h':
        secret_num = random.randint(0, 1000)
        print("Your range is 0 - 1000")
        high_dist = 500
        med_dist = 200
    for x in range(0, 5):
        num = int(input('Guess the secret number: '))
        if num == secret_num:
            print("YOU GOT IT!")
            break
        else:
            print("Wrong!")

        dist = abs(secret_num - num)
        if dist > high_dist:
            print("Cold")
        elif dist < high_dist and dist >= med_dist:
            print("Warm")
        elif dist < med_dist:
            print("HOT")

        if x == 4:
            print(f"YOU LOST! The number was {secret_num}")

#main
main()
