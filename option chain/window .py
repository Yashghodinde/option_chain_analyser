from tkinter import *

root = Tk()

root.geometry("700x600")
root.minsize(200,100)
root.title("pcr")
f1 = Frame(root , bg="grey", borderwidth=6 , relief=RIDGE)
f1.pack(side=LEFT)

l = Label(f1, text="project pcr")
l.pack(pady=142)

root.mainloop()