e = None
iint = None
value = None
root = None
from single import Single
def printtext():
    global e
    global root
    global iint

    iint = e.get()
    label2 = Label(root, text='Invalid')
    label2.pack(anchor='center')


    if iint.isdigit():
        Single.value=iint
        root.destroy()
    else:
        label2.configure(text='invalid')
        label2.update()
        label2.pack(anchor='center')



from tkinter import *
def window():
    global root
    root =Tk()
    global e
    global iint
    root.geometry('300x300')
    root.title('Tez Parking(Null Pointer Exception)')
    e = Entry(root)
    e.pack()
    e.focus_set()
    txtlabel  = Label(root,text = "Enter Time for Parking in minute")
    txtlabel.pack(side=TOP)
    b = Button(root,text='okay',command=printtext)
    b.pack(side='bottom')
    root.mainloop()
