from Function import get_todo, write_todo
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("Current time: ")
print(now)
while True:  # condition as it'll be true so it'll be executing
    action = input("Add, show edit or exit: ")  # take input()
    action = action.strip()  # to take both upper and lower or number postion
    # another codition from the action input
    if action.startswith('add'):
        todo = action[4:]

        '''
        file = open('todos.txt', 'r')
        todos = file.readlines()
        file.close()
        '''

        todos = get_todo()

        todos.append(todo + '\n')  # list out all the input

        write_todo(todos)
        '''
        file = open('todos.txt', 'w')                    #open the file in write mode
        file.writelines(todos)                           #write the content in the todos.txt
        file.close()                                     #after operation done close the file
        '''

    elif action.startswith('show'):
        '''
        file = open('todos.txt', 'r')      we can write this code also bt it's a    bit lengthy so we are using another
        todos = file.readlines()            code that is less in space and work as same
        file.close()
        '''

        todos = get_todo()

        new_todos = [item.strip('\n') for item in todos]  # new_todos to store input line by line

        for index, item in enumerate(new_todos):  # index position and the item inserted will be listed
            row = f"{index + 1}-{item}"  # to show index position from 1 along with item
            print(row)
    elif action.startswith('edit'):
        try:
            number = int(action[5:])
            print(number)
            number = number - 1

            todos = get_todo()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            write_todo(todos)
        except ValueError:
            print("Invalid Command!")
            continue


    elif action.startswith('complete'):
        try:
            number = int(action[9:])

            todos = get_todo()

            index = number - 1
            todo_remove = todos[index].strip('\n')
            todos.pop(index)

            todos.pop(number - 1)
            write_todo(todos)

            msg = f"Todo: {todo_remove} was moved from the list."
            print(msg)
        except IndexError:
            print("Invalid Input")
            continue

    elif action.startswith('exit'):
        break

    else:
        print("Invalid command!")

print("bye!")
