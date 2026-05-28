#Karis
#adventure.py
#A mini adventure based on user input

#Funcs
def adventure():
    input("Welcome! If you would like to see the next line, press enter, and to answer questions, please type when prompted.")
    move = input("You are standing in an open field, to your right you see a table filled with food, and to your left you see a little raccoon. \nWhere would you like to go? (table/raccoon) ")
    if move == 'raccoon':
        input("You approach the little raccoon. You notice it's beautiful fur and really really wanna pet it.")
        pet = input("Do you? (yes/no): ")
        if pet == 'yes':
            input('You slowly move towards it, smiling to show how friendly you are.')
            input("You reach out your hand...")
            input("AHH! Before you can even pet it, it bites you. Your hand is now bleeding.")
        if pet == 'no':
            input('You resist the urge. You still walk towards it slowly though')
            input("You sit down next to it, while still giving it room")
            input("It looks to you and from behind it's back... it pulls out a....")
            input("MANGOOOO")
    elif move == 'table':
        input("You slowly approach the table.")
        input("Oh mannnn that food looks good... and when was the last time you ate?")
        eat = input("You are really hungry... do you eat some of the food? (yes/no) ")
        if eat == 'yes':
            input("YES!!!!!! You eat some mac and cheese, apple pie, rice, warm bread every single thing you love.")
            input("When you finally are satisfied, you lay down in the grass, but you start to feel something..")
            input("You start to feel an extreme pain in your stomach and your vision begins to fade..")
        elif eat == 'no':
            input("AW MAN. Instead of eating it, you stand and just stare at the food, mouth watering")
            input("As you're staring at the most delicious muffin you've ever seen, you notice something...")
            input("Is that.. MOLD?!!?!?! The small spot you saw begins to grow rapidly and soon every single piece of food is covered in it.")
            input("You are so glad you didn't eat any of that food.")


#Main
adventure()
