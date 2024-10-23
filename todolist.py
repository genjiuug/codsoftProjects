import tkinter as tk                    
from tkinter import ttk                 
from tkinter import messagebox          
import sqlite3 as sql                   
  #importing all first
def add_task():  
    otaskstring = taskfield.get()  
    if len(otaskstring) == 0:  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:  
        tasks.append(otaskstring)  
        the_cursor.execute('insert into tasks values (?)', (otaskstring,))  
        list_update()  
        taskfield.delete(0, 'end')  
  #to update the list
def list_update():  
    clear_list()  
    for task in tasks:  
        tasklistbox.insert('end', task)  
  #to delete the tak
def delete_task():  
    try:  
        othevalue = tasklistbox.get(tasklistbox.curselection())  
        if othevalue in tasks:  
            tasks.remove(othevalue)  
            list_update()  
            the_cursor.execute('Please delete from tasks where title = ?', (othevalue,))  
    except:  
        messagebox.showinfo('Error', 'AS No Task Selected. Cannot Delete the tasks.')        
  #to delete all the task
def delete_all_tasks():  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    if message_box == True:  
        while len(tasks) != 0:  
            tasks.pop()  
        the_cursor.execute('delete from tasks')  
        list_update()  
  #to clear list
def clear_list():  
    tasklistbox.delete(0, 'end')  
  #to close
def close():  
    print(tasks)  
    guiWindow.destroy()  
  #to retrieve database
def retrieve_database():  
    while len(tasks) != 0:  
        tasks.pop()  
    for row in the_cursor.execute('select title from tasks'):  
        tasks.append(row[0])  
  #to create GUI
if __name__ == "__main__":  
    guiWindow = tk.Tk()  
    guiWindow.title("To-Do List Manager")  
    guiWindow.geometry("500x450+750+250")  
    guiWindow.resizable(0, 0)  
    guiWindow.configure(bg="#FF0000")  
  
    the_connection = sql.connect('listOfTasks.db')  
    the_cursor = the_connection.cursor()  
    the_cursor.execute('create table if not exists tasks (title text)')  
  
    tasks = []  
  
    headerframe = tk.Frame(guiWindow, bg="#a3ccc9")  
    functionsframe = tk.Frame(guiWindow, bg="#a3ccc9")  
    listboxframe = tk.Frame(guiWindow, bg="#a3ccc9")  
  
    headerframe.pack(fill="both")  
    functionsframe.pack(side="left", expand=True, fill="both")  
    listboxframe.pack(side="right", expand=True, fill="both")  
  
    headerlabel = ttk.Label(headerframe, text="The To-Do List", font=("Brush Script MT", "30"), background="#e7f705", foreground="#000000")  
    headerlabel.pack(padx=20, pady=20)  
  
    tasklabel = ttk.Label(functionsframe, text="Enter the Task:", font=("Consolas", "11", "bold"), background="#e7f705", foreground="#000000")  
    tasklabel.place(x=30, y=40)  
  
    taskfield = ttk.Entry(functionsframe, font=("Consolas", "12"), width=18, background="#FFF8DC", foreground="#A52A2A")  
    taskfield.place(x=30, y=80)  
  
    addthe_button = ttk.Button(functionsframe, text="1.Add Task", width=24, command=add_task)  
    delthe_button = ttk.Button(functionsframe, text="2.Delete Task", width=24, command=delete_task)  
    delallthe_button = ttk.Button(functionsframe, text="3.Delete All Tasks", width=24, command=delete_all_tasks)  
    exitthe_button = ttk.Button(functionsframe, text="4.Exit", width=24, command=close)  

    addthe_button.place(x=30, y=120)  
    delthe_button.place(x=30, y=160)  
    delallthe_button.place(x=30, y=200)  
    exitthe_button.place(x=30, y=240)  
  
    tasklistbox = tk.Listbox(listboxframe, width=26, height=13, selectmode='SINGLE', background="#FFFFFF", foreground="#000000", selectbackground="#CD853F", selectforeground="#FFFFFF")  
    tasklistbox.place(x=10, y=20)  
  
    retrieve_database()  
    list_update()  
    guiWindow.mainloop()  
  
    the_connection.commit()  
    the_cursor.close()  
