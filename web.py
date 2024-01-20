import streamlit as st
import functions



def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ''


def remove_todo(index_to_remove):
    todos.pop(index_to_remove)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(label=todo, key=index)
    if checkbox:
        remove_todo(index)
        st.experimental_rerun()

st.text_input("Enter a new todo:", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
