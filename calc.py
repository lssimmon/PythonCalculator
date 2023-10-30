# let's see how this goes

from tkinter import *

# Control

def add(a, b):

    return (float(a) + float(b))

def sub(a, b):
    return (float(a) - float(b))

def div(a, b):
    return (float(a) / float(b))

def mult(a, b):
    return (float(a) * float(b))


# used PEMDAS
def eval(input):
    input.append(numString)

    while len(input) > 1:

        if "*" in input:
            index = input.index("*")
            val1 = input[index - 1]
            val2 = input[index + 1]
            print(val1)
            print(val2)
            val = mult(val1, val2)
            input.pop(index+1)
            input.pop(index)
            input.pop(index-1)
            input.insert(index-1,val )
            print(input)

        
        
        elif "/" in input:
            index = input.index("/")
            val1 = input[index - 1]
            val2 = input[index + 1]
            print(val1)
            print(val2)
            val = div(val1, val2)
            input.pop(index+1)
            input.pop(index)
            input.pop(index-1)
            input.insert(index-1,val )
            print(input)


        elif "+" in input:
            index = input.index("+")
            val1 = input[index - 1]
            val2 = input[index + 1]
            print(val1)
            print(val2)
            addedVal = add(val1, val2)
            input.pop(index+1)
            input.pop(index)
            input.pop(index-1)
            input.insert(index-1,addedVal )
            print(input)

        elif "-" in input:
            index = input.index("-")
            val1 = input[index - 1]
            val2 = input[index + 1]
            print(val1)
            print(val2)
            val = sub(val1, val2)
            input.pop(index+1)
            input.pop(index)
            input.pop(index-1)
            input.insert(index-1,val )
            print(input)

        else:
            # do nothing
            print()

        e.delete(0,END)
        e.insert(0, input[0])

def clear():
    global clicks
    global numString
    global expression
    global canOp
    e.delete(0,END)

    clicks = 0
    numString = ""
    expression = []
    canOp = False
    



# makes window appear
root = Tk()
# adds title in top bar



# not sure what this does
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
e.insert(0, "Enter Expression")
clicks = 0
numString = ""
expression = []
canOp = False

root.title("Calculator")

def buttonClick(value):
    global clicks
    global numString
    global expression
    global canOp
    
    opString = "*/+-"
    if clicks == 0:
        e.delete(0,END)
        
    
    if value in opString:
        if canOp == False:
            return
        expression.append(numString)
        expression.append(value)
        print(expression)
        numString = ""
        canOp = False
    
    else:
        numString = numString + value
        canOp = True
        

    
    e.insert(clicks, value)
    clicks = clicks + 1

#def enter():


# define button
button1 = Button(root, text="1", padx=40, pady=20, command= lambda: buttonClick("1"))
button2 = Button(root, text="2", padx=40, pady=20, command= lambda: buttonClick("2"))
button3 = Button(root, text="3", padx=40, pady=20, command= lambda: buttonClick("3"))
button4 = Button(root, text="4", padx=40, pady=20, command= lambda: buttonClick("4"))
button5 = Button(root, text="5", padx=40, pady=20, command= lambda: buttonClick("5"))
button6 = Button(root, text="6", padx=40, pady=20, command= lambda: buttonClick("6"))
button7 = Button(root, text="7", padx=40, pady=20, command= lambda: buttonClick("7"))
button8 = Button(root, text="8", padx=40, pady=20, command= lambda: buttonClick("8"))
button9 = Button(root, text="9", padx=40, pady=20, command= lambda: buttonClick("9"))
button0 = Button(root, text="0", padx=40, pady=20, command= lambda: buttonClick("0"))

buttonAdd = Button(root, text="+", padx=40, pady=20, command= lambda: buttonClick("+"))
buttonMult = Button(root, text="*", padx=40, pady=20, command= lambda: buttonClick("*"))
buttonDiv = Button(root, text="/", padx=40, pady=20, command= lambda: buttonClick("/"))
buttonSub = Button(root, text="-", padx=40, pady=20, command= lambda: buttonClick("-"))

buttonEnter = Button(root, text="=", padx=40, pady=20, command= lambda: eval(expression))
buttonClear = Button(root, text="C", padx=40, pady=20, command= lambda: clear())
buttonNeg = Button(root, text="+/-", padx=35, pady=20, command= lambda: clear())



# puts buttons on the screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)

buttonAdd.grid(row=1, column=4)
buttonMult.grid(row=2, column=4)
buttonDiv.grid(row=3, column=4)
buttonSub.grid(row=4, column=4)

buttonEnter.grid(row=4, column=4)
buttonClear.grid(row=4, column=2)
buttonNeg.grid(row=4, column=1)







root.mainloop()

