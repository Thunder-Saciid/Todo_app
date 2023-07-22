FILEPATH ="todos.txt"

def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of
    todo items
    :param filepath:
    :return:
    """
    with open(filepath, "r") as file:
        Todos = file.readlines()
    return Todos

def write_todos(Todos, filepath=FILEPATH):
    """
    writes a list to a text file
    :param filepath:
    :return:
    """
    with open(filepath,"w") as file:
        file.writelines(Todos)

