#from functions import get_todos, write_todos

from modules import functions

import time

tid = time.strftime("%d %b %Y, %H:%M:%S")
print(f"it is {tid}")

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()


    if user_action.startswith("add"):
        todo = user_action[4:]

       # file_reader = open("todos.txt", "r")
        #Todos = file_reader.readlines()
        #file_reader.close()


        Todos= functions.get_todos()

        Todos.append(todo+"\n")

        functions.write_todos()

       # file_writer = open("todos.txt", "w")
       #file_writer.writelines(Todos)
       #file_writer.close()

    elif user_action.startswith("show"):

        Todos= functions.get_todos()
        # new_todo = [item.strip("\n") for item in Todos]
        # the line above shows the usage of list comprehension to edit the list

        for i, item in enumerate(Todos):
            item =item.strip("\n")
            f=f"{i+1}-{item}"
            print(f)
    elif user_action.startswith("edit"):
        try:

            number = int(user_action[5:])
            number = number -1

            Todos = functions.get_todos()

            new_todo = input("Enter a new to do: ")
            Todos[number] = new_todo + "\n"

            functions.write_todos()
        except ValueError:
            print("Value error, try again")
            continue

    elif user_action.startswith("complete") or user_action.startswith("delete"):
        try:


            number =int(user_action[9:])

            Todos = functions.get_todos()
            index =number-1

            todo_to_remove = Todos[index].strip("\n")

            Todos.pop(number-1)

            functions.write_todos()

            message = f"Todo {todo_to_remove} is completed"
            print(message)
        except IndexError:
            print("Valgt tall eksisterer ikke")
            continue


    elif "exit" in user_action:
        break
    else:
        print("The command is not valid!")

print("Bye!")