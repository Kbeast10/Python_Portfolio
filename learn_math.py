#CREATE TASK
#learn_math.py
#The purpose of this program is to give the user a space to memorize and practice basic arithmetic.

#INIT
import random

#saves data on the questions that were previously gotten wrong by the user
actual_answers = []
wrong_questions = []
wrong_inputs = []

#saves data on the questions that were previously gotten right by the user
correct_answers = []
correct_questions = []

#saves the total amount of questions the user has gotten right and wrong.
total_correct = 0
total_wrong = 0

#FUNCS

# max_num represents the maximum number that could be a term in a problem.
# Amount represents the amount of problems the user wishes to do.
# creates and grades addition problems
def addition(max_num=10, amount=5):
    global actual_answers, wrong_questions, correct_answers, correct_questions, total_correct, total_wrong
    num_correct = 0
    num_wrong = 0
    print("Goodluck!\n")
    for x in range(1, amount+1):
        term1 = random.randint(0, max_num)
        term2 = random.randint(0, max_num)
        print(f"{x})")
        question = f"{term1} + {term2} = "
        while True:
            try:
                guess = int(input(question))
                break
            except ValueError:
                print("Please enter a number next time!")
                continue
        answer = term1 + term2
        if guess == answer:
            print("Correct! :)")
            correct_answers.append(answer)
            correct_questions.append(question)
            num_correct += 1
        else:
            print(f"Incorrect :( it was {answer}.")
            actual_answers.append(answer)
            wrong_questions.append(question)
            wrong_inputs.append(guess)
            num_wrong += 1
    print("\nAll done!")
    print(f"{num_correct}/{amount} correct!")
    total_correct += num_correct
    total_wrong += num_wrong
# max_num represents the maximum number that could be a term in a problem.
# Amount represents the amount of problems the user wishes to do.
# creates and grades subtraction problems

def subtraction(max_num=10, amount=5):
    global actual_answers, wrong_questions, correct_answers
    global correct_questions, total_correct, total_wrong
    num_correct = 0
    num_wrong = 0
    print("Goodluck!\n")
    for x in range(1, amount+1):
        while True:
            term1 = random.randint(0, max_num)
            term2 = random.randint(0, max_num)
            if term2 > term1 or term1 == 0 and term2 == 0:
                continue
            else:
                break
        print(f"{x})")
        question = f"{term1} - {term2} = "
        while True:
            try:
                guess = int(input(question))
                break
            except ValueError:
                print("Please enter a number next time!")
                continue
        answer = term1 - term2
        if guess == answer:
            print("Correct! :)")
            correct_answers.append(answer)
            correct_questions.append(question)
            num_correct += 1
        else:
            print(f"Incorrect :( it was {answer}.")
            actual_answers.append(answer)
            wrong_questions.append(question)
            wrong_inputs.append(guess)
            num_wrong += 1
    print("\nAll done!")
    print(f"{num_correct}/{amount} correct!")
    total_correct += num_correct
    total_wrong += num_wrong

# max_num represents the maximum number that could be a factor in a problem.
# Amount represents the amount of problems the user wishes to do.
# creates and grades multiplication problems
def multiplication(max_num=12, amount=5):
    global actual_answers, wrong_questions, correct_answers, correct_questions, total_correct, total_wrong
    num_correct = 0
    num_wrong = 0
    print("Goodluck!\n")
    for x in range(1, amount+1):
        term1 = random.randint(0, max_num)
        term2 = random.randint(0, max_num)

        print(f"{x})")
        #change to change operation
        question = f"{term1} x {term2} = "
        while True:
            try:
                guess = int(input(question))
                break
            except ValueError:
                print("Please enter a number next time!")
                continue
        #change to change operation
        answer = term1 * term2
        if guess == answer:
            print("Correct! :)")
            correct_answers.append(answer)
            correct_questions.append(question)
            num_correct += 1
        else:
            print(f"Incorrect :( it was {answer}.")
            actual_answers.append(answer)
            wrong_questions.append(question)
            wrong_inputs.append(guess)
            num_wrong += 1
    print("\nAll done!")
    print(f"{num_correct}/{amount} correct!")
    total_correct += num_correct
    total_wrong += num_wrong
# max_num represents the maximum number that could be the dividend or divisor in a problem.
# Amount represents the amount of problems the user wishes to do.
# creates and grades division problems
def division(max_num=12, amount=5):
    global actual_answers, wrong_questions, correct_answers, correct_questions, total_correct, total_wrong
    num_correct = 0
    num_wrong = 0
    print("Goodluck!\n")
    for x in range(1, amount+1):
        while True:
            term1 = random.randint(0, max_num)
            term2 = random.randint(1, max_num)
            if term2 == 0 or term1 < term2 or (term1%term2) != 0 :
                continue
            else:
                break
        question = f"{term1} ÷ {term2} = "
        print(f"{x})")
        while True:
            try:
                guess = int(input(question))
                break
            except ValueError:
                print("Please enter a number next time!")
                continue
        answer = term1 / term2
        if guess == answer:
            print("Correct! :)")
            correct_answers.append(answer)
            correct_questions.append(question)
            num_correct += 1
        else:
            print(f"Incorrect :( it was {int(answer)}.")
            actual_answers.append(answer)
            wrong_questions.append(question)
            wrong_inputs.append(guess)
            num_wrong += 1
    print("\nAll done!")
    total_correct += num_correct
    total_wrong += num_wrong
    print(f"{num_correct}/{amount} correct!")

# amount represents the amount of questions the user would like to do.
# allows the user to re-attempt questions they previously got incorrect.
def retry_q():
    global actual_answers, wrong_questions, correct_answers, correct_questions, total_correct, total_wrong
    num_correct = 0
    num_wrong = 0
    filter = []
    if wrong_questions:
        print(f"You have {len(wrong_questions)} questions to do.")
        print("Goodluck!\n")
        for x in range(len(wrong_questions)):
            print(f"{x+1})")

            while True:
                try:
                    guess = int(input(wrong_questions[x]))
                    break
                except ValueError:
                    print("Please enter a number next time!")
                    continue
            if guess == actual_answers[x]:
                print("Correct!")
                num_correct += 1
                correct_answers.append(actual_answers[x])
                correct_questions.append(wrong_questions[x])
                filter.append(x)
            else:
                print(f"Incorrect it was {actual_answers[x]}.")
                num_wrong += 1

        print("\nAll done!")
        print(f"{len(filter)}/{len(wrong_questions)}")
        total_correct += num_correct
        total_wrong += num_wrong
        print("\nYou have re-tried all questions you previously got wrong!")

        filter.sort(reverse=True)

        for x in range(len(filter)):
            try:
                wrong_questions.pop(filter[x])
                actual_answers.pop(filter[x])
            except:
                continue
        filter.clear()
    else:
        print("\nYou have no wrong questions to retry!")

# calls the main menu. Takes user input and calls the correct function on the basis of the input.
def main():
    global actual_answers, wrong_questions, correct_answers, correct_questions, total_correct, total_wrong
    print("\nWelcome to the Math Trainer!")
    print("Here we can assist with basic arithmetic memorization! Ex: Memorizing your times tables.")
    while True:
        print("\n=== MENU ===")
        print("\na) Addition\nb) Subtraction\nc) Multiplication\nd) Division\ne) Practice Questions Gotten Wrong"\
        "\nf) View Overall Score\ng) Quit")
        choice = input("What would you like to practice/do? (a/b/c/d/e/f/g): ").strip().lower()
        #addition
        if choice == 'a':
            choice = input("what is the largest number you would like to practice with? (enter a number or leave blank): ").strip()
            quantity = input("How many problems would you like to do? (enter a number or leave blank): ").strip()
            try:
                if choice and quantity:
                    addition(int(choice), int(quantity))
                elif choice and not quantity:
                    addition(int(choice))
                elif not choice and quantity:
                    addition(amount=int(quantity))
                else:
                    addition()
            except ValueError:
                print("Please enter numbers next time!")
                continue
        #subtraction
        elif choice == 'b':
            choice = input("what is the largest number you would like to practice with? (enter a number or leave blank): ").strip()
            quantity = input("How many problems would you like to do? (enter a number or leave blank): ").strip()
            try:
                if choice and quantity:
                    subtraction(int(choice), int(quantity))
                elif choice and not quantity:
                    subtraction(int(choice))
                elif not choice and quantity:
                    subtraction(amount=int(quantity))
                else:
                    subtraction()
            except ValueError:
                print("Please enter numbers next time!")
                continue

        #multiplication
        elif choice == 'c':
            choice = input("what is the largest number you would like to practice with? (enter a number or leave blank): ").strip()
            quantity = input("How many problems would you like to do? (enter a number or leave blank): ").strip()
            try:
                if choice and quantity:
                    multiplication(int(choice), int(quantity))
                elif choice and not quantity:
                    multiplication(int(choice))
                elif not choice and quantity:
                    multiplication(amount=int(quantity))
                else:
                    multiplication()
            except ValueError:
                print("Please enter numbers next time!")
                continue
        #division
        elif choice == 'd':
            choice = input("what is the largest number you would like to practice with? (enter a number or leave blank): ").strip()
            quantity = input("How many problems would you like to do? (enter a number or leave blank): ").strip()
            try:
                if choice and quantity:
                    division(int(choice), int(quantity))
                elif choice and not quantity:
                    division(int(choice))
                elif not choice and quantity:
                    division(amount=int(quantity))
                else:
                    division()
            except ValueError:
                print("Please enter numbers next time!")
                continue
        #retry questions
        elif choice == 'e':
            retry_q()
        elif choice == 'f':
            try:
                percent = total_correct / (total_correct + total_wrong) * 100
                print(f"\n{total_correct}/{(total_correct+total_wrong)} correct overall which is ~{round(percent)}% correct!")
            except ZeroDivisionError:
                print("\nYou have not done any problems yet! Check back later.")
        elif choice == 'g':
            print("Thank you for practicing with us!")
            print("Goodbye!")
            exit()
        else:
            print("Sorry, we don't recognize this input. Please try again.")

#MAIN
main()
