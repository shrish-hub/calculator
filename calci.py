from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
root=Tk()

menubar = Menu(root)
root.config(menu=menubar)
menubar.add_cascade(label="Exit ", command=root.destroy)

root.geometry("490x450")
root.resizable(0,0)
root.title("Calculator")
root.iconbitmap(r'calci.ico')

#Global Variable
data=StringVar()
value=""
A=0
operator=""

# When button clicked for operation

#when button 1st is clicked

def btn1_clicked():
    global value
    value=value+"1"
    data.set(value)

#when button 2nd is clicked

def btn2_clicked():
    global value
    value=value+"2"
    data.set(value)

#when button 3rd is clicked

def btn3_clicked():
    global value
    value=value+"3"
    data.set(value)

#when button 4th is clicked

def btn4_clicked():
    global value
    value=value+"4"
    data.set(value)

#when button 5th is clicked

def btn5_clicked():
    global value
    value=value+"5"
    data.set(value)

#when button 6th is clicked

def btn6_clicked():
    global value
    value=value+"6"
    data.set(value)


#when button 7th is clicked

def btn7_clicked():
    global value
    value=value+"7"
    data.set(value)


#when button 8th is clicked

def btn8_clicked():
    global value
    value=value+"8"
    data.set(value)


#when button 9th is clicked

def btn9_clicked():
    global value
    value=value+"9"
    data.set(value)



#when button 0th is clicked

def btn0_clicked():
    global value
    value=value+"0"
    data.set(value)

    #when  the operations done


#When the addation done

def btnadd():
    global A
    global operator
    global value
    A=int(value)
    operator="+"
    value=value+"+"
    data.set(value)

#When the subtraction done

def btnsub():
    global A
    global operator
    global value
    A=int(value)
    operator="-"
    value=value+"-"
    data.set(value)

#When the multiplication done

def btnmulti():
    global A
    global operator
    global value
    A=int(value)
    operator="*"
    value=value+"*"
    data.set(value)

#When the devide done

def btndiv():
    global A
    global operator
    global value
    A=int(value)
    operator="/"
    value=value+"/"
    data.set(value)
    
#When c is pressed

def btnclear():
    global A
    global operator
    global value
    value=""
    A=0
    operator=""
    data.set(value)


#When = is pressed

def btnequals():
	global A
	global operator
	global value
	value2=value

	#For + calculation
	if operator == "+":
		x = int((value2.split("+")[1]))
		c = A+x
		data.set(c)
		value = int(c)

	#For - calculation
	elif operator == "-":
		x = int((value2.split("-")[1]))
		c = A-x
		data.set(c)
		value = int(c)

	#For * calculation
	elif operator == "*":
		x = int((value2.split("*")[1]))
		c = A*x
		data.set(c)
		value = int(c)
	#For / calculation
	elif operator == "/":
		x = float((value2.split("/")[1]))
		if x == 0:
			messagebox.showerror("Error","Cannot divide by zero 0")
			A=""
			value=""
			data.set(value)
		else:
			c = float(A/x)
			data.set(c)
			value = float(c)			

#For label

lbl=Label(
	root,
	text="Label",
	anchor=SE,
	font=("Verdana",20),
	background="yellow",
	foreground="#000000",
	textvariable=data,
)
lbl.pack(expand = True, fill="both",)

#For button row one

btnrow1 = Frame(root)
btnrow1.pack(expand = True, fill = "both",)

#For button row two

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both",)

#For button row three

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both",)

#For button row four

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both",)


#BUTTON ROW 1

#For button 1 in btnrow1

btn7 = Button(
	btnrow1,
	text = "7",
	font=("Verdana",20),
	relief=GROOVE,
	border=3,
	command=btn7_clicked,
        foreground="red",
        background="black"
)
btn7.pack(side=LEFT, expand=True,fill="both",)


#For button 2 in btnrow1

btn8 = Button(
	btnrow1,
	text = "8",
	font=("Verdana",20),
	relief=GROOVE,
	border=3,
	command=btn8_clicked,
        foreground="red",
        background="black"
)
btn8.pack(side=LEFT, expand=True,fill="both",)

#For button 3 in btnrow1

btn9 = Button(
	btnrow1,
	text = "9",
	font=("Verdana",20),
	relief=GROOVE,
	border=3,
	command=btn9_clicked,
        foreground="red",
        background="black"
)
btn9.pack(side=LEFT, expand=True,fill="both",)

#For button 4 in btnrow1

btndiv = Button(
	btnrow1,
	text = " /",
	font=("Verdana",20),
	relief=GROOVE,
	border=3,
	command=btndiv,
	foreground="white",
        background="black"

)
btndiv.pack(side=LEFT, expand=True,fill="both",)

#BUTTON ROW 2


#For button 1 in btnrow2

btn4 = Button(
	btnrow2,
	text = "4",
	font=("Verdana",20),
	relief=GROOVE,
	border=3,
	command=btn4_clicked,
        foreground="red",
        background="black"

)
btn4.pack(side=LEFT, expand=True,fill="both",)

#For button 2 in btnrow2

btn5 = Button(
	btnrow2,
	text = "5",
	font=("Verdana",20),
	relief=GROOVE,
	border=3,
	command=btn5_clicked,
        foreground="red",
        background="black"
)
btn5.pack(side=LEFT, expand=True,fill="both",)

#For button 3 in btnrow2

btn6 = Button(
	btnrow2,
	text = "6",
	font=("Verdana",20),
	relief=GROOVE,
	border=3,
	command=btn6_clicked,
        foreground="red",
        background="black"
)
btn6.pack(side=LEFT, expand=True,fill="both",)

#For button 4 in btnrow2

btnmulti = Button(
	btnrow2,
	text = "*",
	font=("Verdana",20),
	relief=GROOVE,
	border=3,
	command=btnmulti,
	foreground="white",
        background="black"
)
btnmulti.pack(side=LEFT, expand=True,fill="both",)

#BUTTON ROW 3


#For button 1 in btnrow3

btn1 = Button(
	btnrow3,
	text = "1",
	font=("Verdana",20),
	relief=GROOVE,
	border=3,
	command=btn1_clicked,
        foreground="red",
        background="black"
)
btn1.pack(side=LEFT, expand=True,fill="both",)

#For button 2 in btnrow3

btn2 = Button(
	btnrow3,
	text = "2",
	font=("Verdana",20),
	relief=GROOVE,
	border=3,
	command=btn2_clicked,
        foreground="red",
        background="black"
)
btn2.pack(side=LEFT, expand=True,fill="both",)

#For button 3 in btnrow3

btn3 = Button(
	btnrow3,
	text = "3",
	font=("Verdana",20),
	relief=GROOVE,
	border=3,
	command=btn3_clicked,
        foreground="red",
        background="black"
)
btn3.pack(side=LEFT, expand=True,fill="both",)

#For button 4 in btnrow3

btnsub = Button(
	btnrow3,
	text = "-",
	font=("Verdana",20),
	relief=GROOVE,
	border=3,
	command=btnsub,
	foreground="white",
        background="black"
)
btnsub.pack(side=LEFT, expand=True,fill="both",)



#BUTTON ROW 4


#For button 1 in btnrow4
btnclear = Button(
	btnrow4,
	text = "C",
	font=("Verdana",20),
	relief=GROOVE,
	border=3,
	command=btnclear,
        foreground="white",
        background="black"
)
btnclear.pack(side=LEFT, expand=True,fill="both",)

#For button 2 in btnrow4

btn0 = Button(
	btnrow4,
	text = "0",
	font=("Verdana",20),
	relief=GROOVE,
	border=3,
	command=btn0_clicked,
	foreground="red",
        background="black"
)
btn0.pack(side=LEFT, expand=True,fill="both",)

#For button 3 in btnrow4

btnequals = Button(
	btnrow4,
	text = "=",
	font=("Verdana",20),
	relief=GROOVE,
	border=3,
	command=btnequals,
	foreground="white",
        background="black"
)
btnequals.pack(side=LEFT, expand=True ,fill="both",)

#For button 4 in btnrow4

btnadd = Button(
	btnrow4,
	text = "+",
	font=("Verdana",20),
	relief=GROOVE,
	border=3,
	command=btnadd,
	foreground="white",
        background="black"
)
btnadd.pack(side=LEFT, expand=True ,fill="both",)


root.mainloop()



