from tkinter import *
from tkinter import PhotoImage
 
import Alzheimer
import Brain_Tumor
import Fetus
import Kidney_Stone
 
def needTodo():
    subMenu.add_command(label="Go", command=File1.alz)
     
def det1():
    Alzheimer
def det2():
    File1.alz()
 
root = Tk()
root.title('........')
 
# ******** MAIN MENU  ******** #
 
menu = Menu(root)
root.config(menu=menu)
root.minsize(600, 650)
root.geometry("600x650")
 
subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
 
subMenu.add_command(label="Tumor", command=needTodo)
subMenu.add_command(label="Fetus", command=needTodo)
subMenu.add_command(label="Alzheimer", command=needTodo)
subMenu.add_command(label="Kidney Stone", command=needTodo)

subMenu.add_separator()
subMenu.add_command(label="Exit", command=quit)
 
# *********** Toolbar ************ #
 
toolbar = Frame(root, bg="silver")

insertBar = Button(toolbar, text="Tumor", command=needTodo)
insertBar.pack(side=LEFT, padx=2, pady=2)

insertBar = Button(toolbar, text="Alzheimer", command=needTodo)
insertBar.pack(side=LEFT, padx=2, pady=2)

insertBar = Button(toolbar, text="Kidney Stone", command=needTodo)
insertBar.pack(side=RIGHT, padx=2, pady=2)

insertBar = Button(toolbar, text="Fetus", command=needTodo)
insertBar.pack(side=RIGHT, padx=2, pady=2)


toolbar.pack(side=TOP, fill=X)
 
btn2 = Button(toolbar, text="Go", command=det2)
btn2.pack(side=LEFT, padx=2, pady=2)
 
toolbar.pack(side=TOP, fill=X)
 
 
 
# ********* IMAGE BACKGROUND ************ #
 
canvas = Canvas(root, width=699, height=837, bg='white')
canvas.pack()
gif1 = PhotoImage(file='/home/bot/Desktop/environments/my_env/background.gif')
canvas.create_image(0, 0, image=gif1, anchor=NW)
 
 
 
# ********* STATUS BAR ************ #
 
status = Label(root, text="It is ready to work....", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
 
root.mainloop()
