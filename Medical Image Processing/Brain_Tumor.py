from tkinter import *
from tkinter import PhotoImage




def needTodo():
    print("Your talking to the wrong person!!")


root = Tk()
root.title('Medical Image Processing')

# ******** MAIN MENU  ******** #

menu = Menu(root)
root.config(menu=menu)
root.minsize(1280, 720)
root.geometry("1300x750")

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Insert Tumor", command=needTodo)
subMenu.add_command(label="Scan Tumor", command=needTodo)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=quit)

# *********** Toolbar ************ #

toolbar = Frame(root, bg="blue")

insertBar = Button(toolbar, text="Scan Tumor", command=needTodo)
insertBar.pack(side=RIGHT, padx=2, pady=2)

insertBar = Button(toolbar, text="Insert Tumor File", command=needTodo)
insertBar.pack(side=RIGHT, padx=2, pady=2)

insertBar = Button(toolbar, text="HOME", command=needTodo)
insertBar.pack(side=LEFT, padx=2, pady=2)


toolbar.pack(side=TOP, fill=X)



# ********* IMAGE BACKGROUND ************ #

canvas = Canvas(root, width=699, height=837, bg='white')
canvas.pack()
gif1 = PhotoImage(file='D:\\background.png')
canvas.create_image(0, 0, image=gif1, anchor=NW)



# ********* STATUS BAR ************ #

status = Label(root, text="It is ready to work....", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
