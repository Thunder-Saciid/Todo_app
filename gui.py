import modules.functions
import PySimpleGUI as ps

label = ps.Text("Type in a todo: ")
input_box = ps.InputText(tooltip ="Enter todo")

add_button = ps.Button("Add")

window = ps.Window("My Todo App", layout=[[label, input_box, add_button]])
window.read()
window.close()