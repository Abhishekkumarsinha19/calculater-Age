from tkinter import *
from datetime import date

root=Tk()
root.iconbitmap("calculator age.icon.ico")

root.geometry("800x600")
root.resizable(False,False)
root.title("Age Calculator")

image_path = r"C:\Users\hp\Desktop\gui\Calculator Age\calculator age.icon.jpg"
myimage = Label(image=PhotoImage(file=image_path))
myimage.pack(padx=15,pady=15)

def calculateAge():
    today=date.today()
    birthDate=date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get()))
    age=today.year-birthDate.year-((today.month,today.day)<(birthDate.month,birthDate.day))
    Label(text=f"{namevalue.get()}your age is{age}",font=30).place(x=300,y=500)

Label(text="Name",font=23).place(x=200,y=250)
Label(text="Year",font=23).place(x=200,y=300)
Label(text="Month",font=23).place(x=200,y=350)
Label(text="Day",font=23).place(x=200,y=400)

namevalue=StringVar()
yearvalue=StringVar()
monthvalue=StringVar()
dayvalue=StringVar()

nameEntry=Entry(root,textvariable=namevalue,width=30,bd=3,font=20)
nameEntry.place(x=300,y=250)

yearEntry=Entry(root,textvariable=yearvalue,width=30,bd=3,font=20)
yearEntry.place(x=300,y=300)

monthEntry=Entry(root,textvariable=monthvalue,width=30,bd=3,font=20)
monthEntry.place(x=300,y=350)

dayEntry=Entry(root,textvariable=dayvalue,width=30,bd=3,font=20)
dayEntry.place(x=300,y=400)

Button(text="calculate Age",font=20,bg="black",fg="white",width=11,height=2,command=calculateAge).place(x=300,y=450)



root.mainloop()