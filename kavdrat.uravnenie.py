from tkinter import *

def lahenda():
    if (a.get()!=""and b.get()!=""and c.get()!=""):
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        D=b_*b_-4*a_*c_
        if D>0:
            x1_=round((-1*b_+sqrt(D))/(2*a_),2)
            x2_=round((-1*b_-sqrt(D))/(2*a_),2)
            t=f"X1={x1_}, \nX2={x2_}"
        elif D==0:
            x1_=round((-1*b_)/(2*a_),2)
            t=f"X1={x1_}"
        else:
            t="Корней нет"
        vastus.configure(text=f"D={D}\n{t}")
        a.configure(bg="lightblue")
        b.configure(bg="lightblue")
        c.configure(bg="lightblue")
    else:
        if a.get()=="":
            a.configure(bg="red")
        elif b.get()=="":
            b.configure(bg="red")
        elif c.get()=="":
            c.configure(bg="red")

def text_to_lbl(event):
    text=ent.get()
    lbl.configure(text=text)

aken=Tk()
aken.title("Tkinter_app")

lbl=Label(aken,text="Решение квадратный уравнений",borderwidth=5,
height=2,width=35,relief="groove",font="Arial 20") #raised,sunken,flat,ridge,solid
lbl.pack()

a=Entry(aken,borderwidth=16,width=3,font="Arial 20")
a.bind("<Return>",text_to_lbl) #Enter
a.pack(side=LEFT)

lbl=Label(aken,text="x**2+",borderwidth=5,
height=2,width=5,relief="groove",font="Arial 20")
lbl.pack(side=LEFT)

b=Entry(aken,borderwidth=16,width=3,font="Arial 20")
b.bind("<Return>",text_to_lbl) #Enter
b.pack(side=LEFT)

lbl=Label(aken,text="x+",borderwidth=5,
height=2,width=5,relief="groove",font="Arial 20")
lbl.pack(side=LEFT)

c=Entry(aken,borderwidth=16,width=3,font="Arial 20")
c.bind("<Return>",text_to_lbl) #Enter
c.pack(side=LEFT)

lbl=Label(aken,text="=0",borderwidth=5,
height=2,width=5,relief="groove",font="Arial 20")
lbl.pack(side=LEFT)

btn=Button(aken,text="Решить",borderwidth=5,
height=2,width=35,relief="groove",font="Arial 20",command=lambda:lahenda())
#raised,sunken,flat,ridge,solid
btn.pack(side=LEFT)

vastus=Label(aken,text="Решение",borderwidth=5,
height=2,width=35,relief="groove",font="Arial 20") 
#raised,sunken,flat,ridge,solid
vastus.pack(side=TOP)

aken.mainloop()