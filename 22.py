from tkinter import *

root=Tk()

menubar=Menu(root)

a1=Menu(menubar,tearoff=0)
a1.add_command(label="opton1",accelerator="@",command=lambda :print("Hello"))

menubar.add_cascade(label="a1",menu=a1)

root.config(menu=menubar)

root.mainloop()
