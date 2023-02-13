import streamlit as st
import functions
todos = functions.get_todos()

#Create a function to use in st.text_input. 
def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")


for index,todo in enumerate(todos):
    #Store all checkboxes as a variable
    #Printing checkbox will print state ("True/False") of all the todo items
    checkbox = st.checkbox(todo, key= f'checkbox_{index}')
    #Check if checkbox == True and if so then remove it from the todos list based on its index
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f'checkbox_{index}']
        st.experimental_rerun()

st.text_input(label="Enter a todo:", placeholder="Add new todo...", on_change=add_todo, key='new_todo')


