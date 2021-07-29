from tkinter import *
from tkinter import messagebox
import time
from datetime import datetime

welcome_message = 'Welcome to your ULTIMATE TO-DO LIST...'
print (welcome_message)
name = input('What is your name?')
print (name)
print(input('How do you plan to use this app?'))

class User:
  def __init__(self,name,use):
    self.name = name
    self.use = use

user1 = User("Natalie", 'Educational and Personal Use')

print(user1.name)
print(user1.use)

verification= input('Is this correct? Please type yes or no')
print(verification)

if 'yes' in verification:
  verification_answer = "Great...let\'s continue"
else:
  verification_answer = "This can be changed later in settings based on your preferences."

print (verification_answer)

print('Thank you for your feedback, let\'s get started!')

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)
    
ws = Tk()
ws.geometry('500x450+500+200')
ws.title('THE ULTIMATE TO-DO LIST')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    'Complete MOSTEC assignments',
    'workout for an hour',
    'Study for the SAT',
    'Send that email',
    'Order your school supplies',
    'take a nap',
    'Write in your blog',
    'Read 3 chapters'
    ]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
    )

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='New Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Complete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


ws.mainloop()



