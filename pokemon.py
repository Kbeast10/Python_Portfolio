#Karis
#pokemon.py
'''
Pokemon Evolution is a Python program where players simulate raising their own Pokémon by training, battling, and evolving it over time.

Using a menu-driven system, players choose actions that boost their Pokémon’s stats, unlock new evolution stages, and face off against opponents to test their progress.
'''

#init
import random
name = input("What is your name? ")
poke_name = 'Charmander'
level = 0
day = 1
health = 5
max_health = 5
victory = False
mood = 'indifferent'
wins = 0
losses = 0


#funcs
def main():
    global name, level, day, mood, wins, losses, poke_name, health, victory
    input(f"Hello {name} and {poke_name}!")
    read_data()
    while True:
        print(f"It's day {day}")
        print("Your options are: \na) Train\nb) Rest\nc) Battle Wild\nd) Gym Battle\ne) Final Boss\nf) Quit")
        action = input("What would you like to do? (a/b/c/d/e/f): ").lower().strip()
        if action == 'train' or action == 'a':
            train()
        elif action == 'rest' or action == 'b':
            rest()
        elif action == 'battle wild' or action == 'c':
            wild_battle()
        elif action == 'gym battle' or action == 'd':
            gym_battle()
        elif action == 'final boss' or action == 'e':
            final_boss()
            if victory == True:
                input("You fought hard, but...")
                print("YOU WON!!")
                level += 10
                input(f"Your {poke_name} leveled up to level {level}!")
                evolve()
                save()
            else:
                input("You fought hard, but...")
                input("You lost...")
                input(f"Game over {name}, better luck next time..")
                save()
                exit()
        elif action == 'quit' or action == 'f':
            save()
            exit()
        else:
            print("Please enter one of the options next time!")
        day += 1
def print_stage1():
    print((r"             _.--\"\"`-.."))
    print((r"           ,'          `."))
    print((r"         ,'          __  `."))
    print((r"        /|          \" __   \\"))
    print((r"       , |           / |.   ."))
    print((r"       |,'          !_.'|   |"))
    print((r"     ,'             '   |   |"))
    print((r"    /              |`--'|   |"))
    print((r"   |                `---'   |"))
    print((r"    .   ,                   |                       ,\"."))
    print((r"     ._     '           _'  |                    , ' \\ `"))
    print((r" `.. `.`-...___,...---\"\"    |       __,.        ,`\"   L,|"))
    print((r" |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \\"))
    print((r"-:..     `. `-..--_.,.<       `\"      / `.        `-/ |   ."))
    print((r" `,         \"\"\"\"'     `.              ,'         |   |  ',,"))
    print((r"   `.      '            '            /          '    |'. |/"))
    print((r"     `.   |              \\       _,-'           |       ''"))
    print((r"       `._'               \\   '\"\\                .      |"))
    print((r"          |                '     \\                `._  ,'"))
    print((r"          |                 '     \\                 .'|"))
    print((r"          |                 .      \\                | |"))
    print((r"          |                 |       L              ,' |"))
    print((r"          `                 |       |             /   '"))
    print((r"           \\                |       |           ,'   /"))
    print((r"         ,' \\               |  _.._ ,-..___,..-'    ,'"))
    print((r"        /     .             .      `!             ,j'"))
    print((r"       /       `.          /        .           .'/"))
    print((r"      .          `.       /         |        _.'.'"))
    print((r"       `.          7`'---'          |------\"'_.'"))
    print((r"      _,.`,_     _'                ,''-----\"'"))
    print((r"  _,-_    '       `.     .'      ,\\"))
    print((r"  -\" /`.         _,'     | _  _  _.|"))
    print((r"   \"\"--'---\"\"\"\"\"'        `' '! |! /"))
    print((r"                           `\" \" -' mh"))
    print(("\n"))
    print(("\n"))
def print_stage2():
    print((r"                     ,-'`\\"))
    print((r"                 _,\"'    j"))
    print((r"          __....+       /               ."))
    print((r"      ,-'\"             /               ; `-._.'."))
    print((r"     /                (              ,'       .'"))
    print((r"    |            _.    \\             \\   ---._ `-."))
    print((r"    ,|    ,   _.'  Y    \\             `- ,'   \\   `.`."))
    print((r"    l'    \\ ,'._,\\ `.    .              /       ,--. l"))
    print((r" .,-        `._  |  |    |              \\       _   l ."))
    print((r"/              `\"--'    /              .'       ``. |  )"))
    print((".\\    ,                 |                .        \\ `. '"))
    print(("`.                .     |                '._  __   ;. \\'"))
    print((r" `-..--------...'       \\                  `'  `-\"'.  \\"))
    print((r"     `......___          `._                        |  \\"))
    print((r"              /`            `..                     |   ."))
    print((r"             /|                `-.                  |    L"))
    print((r"            / |               \\   `._               .    |"))
    print((r"          ,'  |,-\"-.   .       .     `.            /     |"))
    print((r"        ,'    |     '   \\      |       `.         /      |"))
    print((r"      ,'     /|       \\  .     |         .       /       |"))
    print((r"    ,'      / |        \\  .    +          \\    ,'       .'"))
    print((r"   .       .  |         \\ |     \\          \\_,'        / j"))
    print((r"   |       |  L          `|      .          `        ,' '"))
    print((r"   |    _. |   \\          /      |           .     .' ,'"))
    print((r"   |   /  `|    \\        .       |  /        |   ,' .'"))
    print((r"   |   ,-..\\     -.     ,        | /         |,.' ,'"))
    print((r"   `. |___,`    /  `.   /`.       '          |  .'"))
    print((r"     '-`-'     j     ` /.\"7-..../|          ,`-'"))
    print((r"               |        .'  / _/_|          ."))
    print((r"               `,       `\"'/\"'    \\          `."))
    print((r"                 `,       '.       `.         |"))
    print((r"            __,.-'         `.        \\'       |"))
    print((r"           /_,-'\\          ,'        |        _."))
    print((r"            |___.---.   ,-'        .-':,-\"`\\,' ."))
    print((r"                 L,.--\"'           '-' |  ,' `-.\\"))
    print((r"                                       `.' mh"))
def print_stage3():
    print((r"                .\"-,.__"))
    print((r"                `.     `.  ,"))
    print((r"             .--'  .._,'\"-' `."))
    print((r"            .    .'         `'"))
    print((r"            `.   /          ,'"))
    print((r"              `  '--.   ,-\"'"))
    print((r"               `\"`   |  \\"))
    print((r"                  -. \\, |"))
    print((r"                   `--Y.'      ___."))
    print((r"                        \\     L._, \\"))
    print((r"              _.,        `.   <  <\\                _"))
    print((r"            ,' '           `, `.   | \\            ( `"))
    print((r"         ../, `.            `  |    .\\`.           \\ \\_"))
    print((r"        ,' ,..  .           _.,'    ||\\l            )  '\"."))
    print((r"       , ,'   \\           ,'.-.`-._,'  |           .  _._`."))
    print((r"     ,' /      \\ \\        `' ' `--/   | \\          / /   ..\\"))
    print((r"   .'  /        \\ .         |\\__ - _ ,'` `        / /     `.`."))
    print((r"   |  '          ..         `-...-\"  |  `-'      / /        . `."))
    print((r"   | /           |L__           |    |          / /          `. `."))
    print((r"  , /            .   .          |    |         / /             ` `"))
    print((r" / /          ,. ,`._ `-_       |    |  _   ,-' /               ` \\"))
    print((r"/ .           \\\"`_/. `-_ \\_,.  ,'    +-' `-'  _,        ..,-.    \\`."))
    print((r".  '         .-f    ,'   `    '.       \\__.---'     _   .'   '     \\ \\"))
    print((r"' /          `.'    l     .' /          \\..      ,_|/   `.  ,'`     L`"))
    print((r"|'      _.-\"\"` `.    \\ _,'  `            \\ `.___`.'\"`-.  , |   |    | \\"))
    print((r"||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|"))
    print((r"||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||"))
    print((r"|| '              V      / /           `   | `   ,'   ,' '.    !  `. ||"))
    print((r"||/            _,-------7 '              . |  `-'    l         /    `||"))
    print((r". |          ,' .-   ,' ||               | .-.        `.      .'     ||"))
    print((r"`'        ,'    `\".'    |               |    `.        '. -.'       `'"))
    print((r"         /      ,'      |               |,'    \\-.._,.'/'"))
    print((r"         .     /        .               .       \\    .''"))
    print((r"       .`.    |         `.             /         :_,'.'"))
    print((r"         \\ `...\\   _     ,'-.        .'         /_.-'"))
    print((r"          `-.__ `,  `'   .  _.>----''.  _  __  /"))
    print((r"               .'        /\"'          |  \"'   '_"))
    print((r"              /_|.-'\\ ,\".             '.'`__'-( \\"))
    print((r"                / ,\"'\"\\,'               `/  `-.|\" mh"))

def print_current_stage():
    global level
    if level < 10:
        print_stage1()
    elif level >= 10 and level <20:
        print_stage2()
    elif level >= 20:
        print_stage3()
def evolve():
    global name, level, day, mood, wins, losses, poke_name, health, victory, max_health
    if level >= 10 and level < 20 and poke_name != 'Charmeleon':
        poke_name = 'Charmeleon'
        print(f"Your pokemon is evolving into {poke_name}!")

        print_stage2()
        max_health += 10
    elif level >= 20 and poke_name != 'Charizard':
        poke_name = 'Charizard'
        print(f"Your pokemon is evolving into {poke_name}!")
        print_stage3()
        max_health += 20
def train():
    global name
    global level
    global day
    global poke_name
    global health
    level += 1
    print(f"{poke_name} is training hard!")
    evolve()


def attack():
    global level
    if level <= 5:
        attack = random.randint(1, 5)
    elif level <= 10:
        attack = random.randint(5, 20)
    elif level <= 15:
        attack == random.randint(20, 30)
    return attack
def wild_battle():
    global name, level, day, mood, wins, losses, poke_name, health, victory, max_health
    fighting = True
    if level < 5:

        e_health = 10
        print("You walk into the bush and see a wild Eevee!")
        print("You wish to battle Eevee!")
        while fighting:
            input(f"The enemy has {e_health} health and you have {health} health.")
            move = input("Do you choose to run or attack? ")
            if move == 'run':
                chance = random.randint(0, 1)
                if chance:
                    print("You got away safely")
                    break
                elif not chance:
                    print("You are forced to attack")

            hit_points = attack()
            input(f"Your snivy charges up andddddd...")
            input(f"Aaaandddddd...")
            input(f"Your Snivy attacks with {hit_points} hit points!")
            e_health -= hit_points
            if e_health <= 0:
                input("The enemy pokemon fainted!!")
                input("You win and Snivy levels up!")
                wins += 1
                level += 1
                evolve()
                break
            e_attack = random.randint(0, 2)
            input("But the enemy bounces back and.....")
            input(f"The enemy attacks with {e_attack} hit points!")
            health -= e_attack

            if health <= 0:
                input("Your pokemon fainted...")
                losses += 1
                break
    else:
        print("These wild pokemon are too weak for you.. You instantly win!")
        wins += 1
        level += 1
def gym_battle():
    global name, level, day, mood, wins, losses, poke_name, health
    odds = random.randint(1, 100)
    chance_win = 50

    diff = wins - losses
    if diff < 0:
        mood = "sad"
    elif diff > 0:
        mood = 'happy'

    if level <= 10:
        if mood == 'sad':
            chance_win = 30
        else:
            chance_win = 50
    elif level > 10 and level < 20:
        if mood == 'sad':
            chance_win = 60
        else:
            chance_win = 70
    else:
        if mood == 'happy':
            chance_win = 85
        else:
            chance_win = 80

    if odds <= chance_win:
        print("YOU WON!!")
        level += 2
        print(f"Your {poke_name} leveled up to level {level}!")
        evolve()
        wins += 1
    else:
        print("You lost..")
        losses += 1

def final_boss():
    global name, level, day, mood, wins, losses, poke_name, health, victory
    input("You are facing the final boss...")
    input("She will not go easy on you....")
    odds = random.randint(1, 100)

    diff = wins - losses
    if diff < 0:
        mood = "sad"
    elif diff > 0:
        mood = 'happy'
    elif diff == 0:
        mood = "indifferent"

    if level <= 10 or mood == 'sad':
        if odds <= 10:
            victory = True
            return
    elif level >= 15 and level < 20:
        if odds <= 40:
            victory = True
            return
    elif level >= 20 and mood == 'happy':
        if odds <= 80:
            victory = True
            return
    else:
        if odds <= 50:
            victory = True
            return

def rest():
    global name, level, day, mood, wins, losses, poke_name, health, victory, max_health
    print_current_stage()
    diff = wins - losses
    if diff < 0:
        mood = "sad"
    elif diff > 0:
        mood = 'happy'
    print(f"Your health has been healed up to {max_health}!")
    print(f"Your {poke_name} is level {level}!")
    print(f"{poke_name} is feeling {mood}")
    print(f"You have {wins} wins and {losses} losses.")

def save():
    global name, level, day, mood, wins, losses, poke_name, health, victory, max_health
    with open('save_data.txt', 'a') as f:
        f.write((f"name: {name} day: {day} mood: {mood} wins: {wins} losses: {losses} poke_name: {poke_name} health: {health} victory: {victory}  max_health: {max_health} \n"))

def read_data():
    global name, level, day, mood, wins, losses, poke_name, health, victory, max_health
    with open('save_data.txt', 'r') as f:
        saves = f.read()
    saves = saves.split('\n')
    print(saves)
    for x in range((len(saves)) -1, 1, -1):
        if x == len(saves):
            continue
        current_save = []
        values = []
        current_save = saves[x].split(' ')
        for y in range(len(current_save), 0, -1):

            if y % 2 == 0:
                continue
            elif y == len(current_save):
                pass
            else:
                values.append(current_save[y])

            if values:
                if values[0] == name:
                    print("Found your save!")
                    name, day, mood, wins, losses, poke_name, health, victory, max_health = values
                    return
                else:
                    continue


    print("Looks like you don't have a previous account! Not to worry, we are starting one for you right now!")

#main
main()

