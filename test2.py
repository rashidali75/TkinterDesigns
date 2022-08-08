from tkinter import*
from tkinter import ttk

def exite():
  root.destroy()


root=Tk()
root.geometry("1750x700+0+0")
root.config(bg="light gray")
root.title("Pharmacy Managment System")
Label(root, text="Pharmacy Managment System", bg="midnight blue", fg="white",font="lucida 20 bold").pack(fill=X)
########## menu frame #####

############FRame bnany hain#####
f1=Frame(root, bg="cadet blue", bd=15, relief=GROOVE)
f1.place(x=20, y=90, width=550, height=600)

f2=Frame(root, bg="cadet blue", bd=15, relief=GROOVE)
f2.place(x=600, y=90, width=750, height=600)
#####label####
name=Label(f1, text="  Name:", bg="cadet blue", fg="white", font="lucida 20 bold")
name.grid( row=0, column=0,padx=10, pady=10)

roll=Label(f1, text="Roll No:", bg="cadet blue", fg="white", font="lucida 20 bold")
roll.grid( row=1, column=0,padx=10, pady=10)

id=Label(f1, text="   ID No:", bg="cadet blue", fg="white", font="lucida 20 bold")
id.grid( row=2, column=0,padx=10, pady=10)

gender=Label(f1, text=" Gender:", bg="cadet blue", fg="white", font="lucida 20 bold")
gender.grid( row=3, column=0,padx=10, pady=10)

address=Label(f1, text="Adress:", bg="cadet blue", fg="white", font="lucida 20 bold")
address.grid( row=4, column=0,padx=10, pady=10)
##############variable########
name=StringVar()
id=StringVar()
gender=StringVar()
address=StringVar()
roll=StringVar()

####Entry
name_entry=Entry(f1, font="lucida 20 bold", textvariable=name)
name_entry.grid( row=0, column=1)

roll_entry=Entry(f1, font="lucida 20 bold",textvariable=roll)
roll_entry.grid( row=1, column=1)

id_entry=Entry(f1, font="lucida 20 bold", textvariable=id)
id_entry.grid( row=2, column=1)

gender_entry=ttk.Combobox(f1, font="lucida 20 bold", values=["Male","Female","Other"],state="readonly", textvariable=gender)
gender_entry.grid( row=3, column=1)

address_entry=Entry(f1, font="lucida 20 bold")
address_entry.grid( row=4, column=1)
####botton##########
f3=Frame(f1, bg="cadet blue")
f3.place(x=20, y=400, width=400, height=100)



add=Button(f3, text="Submit", bg="cadet blue", fg="black", font="lucida 15", bd=10, relief=GROOVE)
add.grid( row=5, column=0, padx=10)

delete=Button(f3, text="Delete", bg="cadet blue", fg="black", font="lucida 15", bd=10, relief=GROOVE)
delete.grid( row=5, column=1, padx=10)

exite=Button(f3, text="Exite", bg="cadet blue", fg="black", font="lucida 15", bd=10, relief=GROOVE, command=exite)
exite.grid( row=5, column=2, padx=10)


root.mainloop()
