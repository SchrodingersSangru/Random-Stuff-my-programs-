
from tkinter import *
from tkinter.messagebox import *

window = Tk()

window.title("AUTOFOCUS TELESCOPE")

window.geometry('350x200')

lbl = Label(window, text="WELCOME TO AUTOFOCUS MECHANISM", font=("Arial Bold", 36))

lbl.grid(column=0, row=0)



btn1 = Button(window, text="RESET", width = 20,  font=("Arial Bold", 18)) #,command= )

btn1.grid(column=10, row=300 )


btn4 = Button(window, text=" ", width = 0,  font=("Arial Bold", 18)) #,command =)

btn4.grid(column=10, row= 400)


btn2 = Button(window, text="AUTOFOCUS", width =20,  font=("Arial Bold", 18)) #,command =)

btn2.grid(column=10, row=500)


btn4 = Button(window, text=" ", width = 0,  font=("Arial Bold", 18)) #,command =)

btn4.grid(column=10, row= 600)


btn3 = Button(window, text="ENTER", width =20,  font=("Arial Bold", 18)) #,command =)

btn3.grid(column=10, row= 700)



def show_answer():

    Entry(main,  text = "%s" %(ans) ).grid(row=2, column=1)


main = ()
Label(main, text = "variance").grid(row=0)

num1 = Entry(main)
num1.grid(row=800, column=10)


window.mainloop()
