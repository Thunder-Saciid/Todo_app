import modules.functions
import PySimpleGUI as ps

label = ps.Text("Type in a todo: ")
input_box = ps.InputText(tooltip ="Enter todo", key ="todo")

add_button = ps.Button("Add")
list_box = ps.Listbox(values= modules.functions.get_todos(), key="todos",enable_events=True, size=[45,10])

edit_button = ps.Button("Edit")

window = ps.Window("My Todo App",
                   layout=[[label] , [input_box, add_button], [ list_box,edit_button]],
                   font=("Helvetica", 20))

while True:
    event,values = window.read()
    match event:
        case "Add":
            todos = modules.functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            modules.functions.write_todos(todos)

            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = modules.functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            modules.functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value = values["todos"][0])

        case ps.WIN_CLOSED:
            break


window.close()