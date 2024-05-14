def get_todo(filepath="todos.txt"):
    with open(filepath, 'r') as file:
        todos = file.readlines()
        return todos


def write_todo(todos_arg, filepath="todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

