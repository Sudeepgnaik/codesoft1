import string
import random
from tkinter import*

root= Tk()
root.title(" password generator")
root.geometry("600x600")

label_title = Label(root,text="Choose the Strength of your password",fg='White',bg='blue',font=('Times New Roman', 26 ))
label_title.pack()

def selection():
    selection=choice.get()


choice = IntVar()
rb1 = Radiobutton(root,text="Poor password",variable=choice,font=("times new roman",30) ,value=1,command=selection)
rb1.pack()
rb2 = Radiobutton(root,text="Average password",font=("times new roman",30) ,variable=choice,value=2,command=selection)
rb2.pack()
rb3 = Radiobutton(root,text="Strong password",font=("times new roman",30) ,variable=choice,value=3,command=selection)
rb3.pack()
label_space=Label(root)
label_space.pack()
label_password=Label(root,text="Choose the strength of your password",fg='White',bg='black',font=("times new roman",22))
label_password.pack()

val=IntVar()
spinlength=Spinbox(root,from_=8,to_=30,textvariable=val,width=30)
spinlength.place(x=50,y=100,height=500)

spinlength.pack(pady=20)

def callback():
    result.config(text=passgen())

button_submit=Button(root,text="Generate password",fg='White',bg='black',font=("times new roman",15) ,command=callback)
button_submit.pack(pady=10)

result=Message(root,text="",relief=RAISED,width=200,font=(30))
result.place(x=100,y=500,height=40,width=400)

poor=string.ascii_uppercase+string.ascii_lowercase
average=string.ascii_uppercase+string.ascii_lowercase+string.digits
strong=string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation

def passgen():
    if choice.get()==1:
        return"".join(random.sample(poor,val.get()))
    elif choice.get()==2:
        return"".join(random.sample(average,val.get()))
    elif choice.get()==3:
        return"".join(random.sample(average,val.get()))


root.mainloop()












