import Function
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

sg.theme("Black")
clock = sg.Text('', key='clock')
label = sg.Text("Type in the ToDo")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_btn = sg.Button(size=10, image_source="add.png", key="Add")
list_box = sg.Listbox(values=Function.get_todo(), key='todos',
                      enable_events=True, size=[45, 10])
edit_btn = sg.Button("Edit")
complete_btn = sg.Button(size=10, image_source="complete.png", key="Complete")
exit_btn = sg.Button("Exit")
window = sg.Window('ToDo_App',
                   layout=[[clock],
                           [label],
                           [input_box, add_btn],
                           [list_box, edit_btn], [complete_btn],
                           [exit_btn]],
                   font= ("Helvetica", 12))
while True:
    event, values = window.read(timeout=100)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = Function.get_todo()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            Function.write_todo(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_edit = values['todos'] [0]
                new_todo = values['todo']
                todos = Function.get_todo()
                index = todos.index(todo_edit)
                todos[index] = new_todo
                Function.write_todo(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Select an item!", font=("Arial", 12))

        case "Complete":
            try:
                todo_complete = values['todos'][0]
                todos = Function.get_todo()
                todos.remove(todo_complete)
                Function.write_todo(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Select and item!", font=("Arial", 12))

        case "Exit":
            break

        case "todos":
            window['todo'].update(value=['todos'][0])

        case sg.WIN_CLOSED:
            break


window.close()