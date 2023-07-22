import modules.functions
import PySimpleGUI as ps

label = ps.Text("Type in a todo: ")
input_box = ps.InputText(tooltip ="Enter todo", key ="todo")

add_button = ps.Button("Add")

window = ps.Window("My Todo App",
                   layout=[[label] , [input_box, add_button]],
                   font=("Helvetica", 20))

while True:
    event,values = window.read()
    match event:
        case "Add":
            todos = modules.functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            modules.functions.write_todos(todos)
        case ps.WIN_CLOSED:
            break


window.close()