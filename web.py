import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo_ in enumerate(todos):
    check_box = st.checkbox(todo_, key=todo_)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo_]
        st._rerun()

st.text_input(label="", placeholder="Add new todo", on_change=add_todo, key="new_todo")


