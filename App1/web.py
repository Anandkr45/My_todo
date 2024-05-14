import streamlit as st
import Function

todos = Function.get_todo()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    Function.write_todo(todos)


st.title("My Todo App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        Function.write_todo(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=" ", placeholder="Add a todo here....",
              on_change=add_todo, key='new_todo')