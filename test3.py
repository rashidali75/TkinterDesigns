from tkinter import*
from tkinter import ttk
import os 
import datetime
window = Tk()
window.title("Pharmacy Management")
window.geometry("1700x700+0+0")
window.config(bg="powder blue")
## Label ##
Label(window, text="School Management System", bg="royal blue",bd=5, fg="white",font="verdana 20 bold").pack(fill=X)
## Navigation frame1 ##
f1=Frame(window, bg="white")
f1.place(x=0, y=54, height=30, width=1500)
## Navigate frame1 button ## 
b1=Button(f1, text="New Student", bg="white", fg="black", font="lucida ")
b1.grid( row=0, column=1, padx=20)

b2=Button(f1, text="Old Student", bg="white", fg="black", font="lucida ")
b2.grid( row=0, column=2, padx=20)

b3=Button(f1, text="Courses", bg="white", fg="black", font="lucida ")
b3.grid( row=0, column=3, padx=20)

b4=Button(f1, text="Teachers", bg="white", fg="black", font="lucida ")
b4.grid( row=0, column=4, padx=20)

b5=Button(f1, text="Prospectus", bg="white", fg="black", font="lucida ")
b5.grid( row=0, column=5, padx=20)


##big frame f2 ##
f2=Frame(window, bg="light gray", bd=5, relief=GROOVE)
f2.place(x=10, y=90, height=500, width=550)
### Frame f5 big second frame ####
f6=Frame(window, bg="light gray", bd=5, relief=GROOVE)
f6.place(x=600, y=90, height=500, width=490)

## Frame f3 ####
f3=Frame(f2, bg="light gray")
f3.place(x=30,y=30, height=230, width=420)

## Label in big Frame f3 ##
name=Label(f3, text="  Name:", bg="light gray", fg="black", font="lucida")
name.grid( row=0, column=0,padx=10, pady=10)

roll=Label(f3, text="Roll No:", bg="light gray", fg="black", font="lucida")
roll.grid( row=1, column=0,padx=20, pady=10)

id=Label(f3, text="   ID No:", bg="light gray", fg="black", font="lucida")
id.grid( row=2, column=0,padx=20, pady=10)


address=Label(f3, text="Adress:", bg="light gray", fg="black", font="lucida")
address.grid( row=3, column=0,padx=20, pady=10)

gender=Label(f3, text=" Gender:", bg="light gray", fg="black", font="lucida")
gender.grid( row=4, column=0,padx=20, pady=10)

####Entry
name_entry=Entry(f3, font="lucida 20 bold",textvariable=name)
name_entry.grid( row=0, column=1)

roll_entry=Entry(f3, font="lucida 20 bold",textvariable=roll)
roll_entry.grid( row=1, column=1)

id_entry=Entry(f3, font="lucida 20 bold", textvariable=id)
id_entry.grid( row=2, column=1)


address_entry=Entry(f3, font="lucida 20 bold")
address_entry.grid( row=3, column=1)

gender_entry=ttk.Combobox(f3, font="lucida 20 bold", values=["Male","Female","Other"],state="readonly", textvariable=gender)
gender_entry.grid( row=4, column=1)
##frame f4 in f2 ###
f4=Frame(f2, bg="light gray")
f4.place(x=150,y=300, height=43, width=250)
##button in frame f4
button=Button(f4, text="Registration",bg="white", fg="black",font="lucida 10 bold", bd=5, relief=GROOVE )
button.grid(row=0, column=1,padx=5,pady=5)

button=Button(f4, text="Submit",bg="white", fg="black",font="lucida 10 bold", bd=5, relief=GROOVE )
button.grid(row=0, column=2,padx=5,pady=5)

button=Button(f4, text="Reset",bg="white", fg="black",font="lucida 10 bold", bd=5, relief=GROOVE )
button.grid(row=0, column=3,padx=5,pady=5)



#### small frame in f2 frame ###
f5=Frame(window, bg="light gray")
f5.place(x=90, y=520, height=40, width=360)
#### clsses and button####
classes=Label(f5, text=" Classes:", bg="light gray", fg="black", font="lucida")
classes.grid( row=0, column=0,padx=2, pady=2)
#button
open=Button(f5, text="Open",bg="white", fg="black",font="lucida 10 bold")
open.grid(row=0, column=5, padx=5,pady=2)
### entry'
classes_entry=ttk.Combobox(f5, font="lucida", values=["9th","10th","FA","I com","11th","12th"],state="readonly", textvariable=classes)
classes_entry.grid( row=0, column=3, padx=2,pady=2)

scroll=Scrollbar(f6,orient=HORIZONTAL)
scroll1=Scrollbar(f6,orient=VERTICAL)



tree=ttk.Treeview(f6, columns=("name","rollno","class"),xscrollcommand=scroll.set,yscrollcommand=scroll1.set)
scroll.pack(side=BOTTOM,fill=X)
scroll1.pack(side=RIGHT,fill=Y)
scroll.config(command=tree.xview)
scroll1.config(command=tree.yview)
tree.pack(fill=BOTH,expand=1)

tree.heading("name",text="Name")
tree.heading("rollno",text="Roll/No")
tree.heading("class",text="Class")

tree.column("name",width=50)
tree.column("rollno",width=50)
tree.column("class",width=50)
tree['show']='headings'


















window.mainloop()