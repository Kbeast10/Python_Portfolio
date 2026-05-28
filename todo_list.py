#Karis
#todo_list.py
'''1. Add an item to the to-do list
2. Remove a task from the to-do list
3. Clear the list (Remove all items)
4. Exit the program

The user should regularly be shown how many items they have to-do and the items themselves.
'''

#funcs
def main():
    todo_list = []
    completed = []
    with open('lists.txt', 'r') as data:
        for line in data:
            todo_list.append(line)
    for x in range(len(todo_list)):
        todo_list[x] = todo_list[x].replace('\n', '')

    while True:
        print("TO-DO LIST:")
        for x in range(len(todo_list)):
            print(f"{x+1}: {todo_list[x]}")
        print()
        print("a) Add an item to your list\nb) Complete an item from your list\nc) Clear your list\nd) View completed items\ne) Quit")
        choice = input("Choose an option: (a/b/c/d/e): ").lower().strip()
        if choice == 'a':
            item = input("Item to add to list: ")
            if item == '':
                print("Sorry, this does not belong in your list.")
            else:
                todo_list.append(item)
            continue
        elif choice == 'b':
            if len(todo_list) > 0:
                try:
                    item = int(input("Item number to complete: "))
                    completed.append(todo_list[item-1])
                    todo_list.pop(item-1)
                    print("Item completed.")
                except:
                    print("Sorry, we are unable to complete this request.")
            else:
                print("There are no items in your list to complete!")
            continue
        elif choice == 'c':
            clear = input("Are you sure you'd like to permanately clear your list? (y/n): ").lower().strip()
            if clear != 'y':
                print("List will not be cleared at this time.")
                continue
            else:
                todo_list = []
                print("List cleared!")
                continue
        elif choice == 'e':
            print("Bye!")
            with open('lists.txt', 'w') as data:
                for x in range(len(todo_list)):
                    data.write(todo_list[x])
                    data.write('\n')
            exit()
        elif choice == 'd':
            if not completed:
                print("Sorry, you have not completed any items yet.")
                continue
            else:
                print(f"Here are all the items you have completed: ")
                for x in completed:
                    print(x)
        else:
            print("Sorry, this is not one of our options. Please enter a correct input next time!")
            continue
#main
main()
