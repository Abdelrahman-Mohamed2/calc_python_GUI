import math
from tkinter import *

#creating the window
root = Tk()
root.title("Calculator")

# Global variables 
first_operand = None
current_operation = None
op_bool = False
result = None


#function to print the number in the entry after clicking it
def add_num(num):
    global first_operand, current_operation, op_bool
    now = en.get()
    en.delete(0, END)
    if op_bool:
        op_bool = False
        en.delete(0, END)
        en.insert(0, num)
    else:
        if now == '0':
            en.insert(0, num)
        else:
            en.insert(0, now + num)


#function for del button
def delete():
    current_text = en.get()
    if current_text:
        en.delete(len(current_text) - 1)
        if len(current_text) == 1:
            en.insert(0, '0')


#function to make the operation after clicking it
def operation(op):
    global first_operand, current_operation, op_bool, result
    if op == 'C':
        en.delete(0, END)
        first_operand = None
        current_operation = None
        en.insert(0, '0')
    elif op in ('+', '-', 'x', '/', '='):
        if current_operation is not None:
            second = float(en.get())
            if current_operation == '+':
                result = first_operand + second
            elif current_operation == '-':
                result = first_operand - second
            elif current_operation == 'x':
                result = first_operand * second
            elif current_operation == '/':
                # Check for division by zero
                if second != 0:
                    result = first_operand / second
                else:
                    en.delete(0, END)
                    en.insert(0, "Error")
                    return
            result = int(result) if result == int(result) else result
            result = str(result)
            en.delete(0, END)
            en.insert(0, result)

        if op == '=':
            current_operation = None
            first_operand = None
        else:
            current_operation = op
            first_operand = float(en.get())
        op_bool = True

#creating entry field
en = Entry(root, width=22, borderwidth=5, background="#B9B9B9", fg="black", font="bold")
en.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
en.insert(0, '0')

# create numbers buttons
numbers_buttons = []
number_positions = [(3, 0), (3, 1), (3, 2), (2, 0), (2, 1), (2, 2), (1, 0), (1, 1), (1, 2)]
for i in range(1, 10):
    numbers_buttons.append(Button(root, text=str(i), padx=30, pady=15, borderwidth=3,
                                  background="#4A4A4A", fg="white", font="bold",
                                  command=lambda num=i: add_num(str(num))).
                           grid(row=number_positions[i - 1][0], column=number_positions[i - 1][1]))
# Adding zero(0)
numbers_buttons.append(Button(root, text='0', padx=30, pady=15, borderwidth=3,
                              background="#4A4A4A", fg="white", font="bold",
                              command=lambda: add_num('0')).
                       grid(row=4, column=0))

# create special buttons
operations_signs = ['+', '-', 'x', '/', '=']
operations = []
operations_positions = [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
for i in range(5):
    operations.append(Button(root, text=operations_signs[i], padx=25, pady=15, borderwidth=3,
                             background="#DF8100", fg="white", font="bold",
                             command=lambda op=operations_signs[i]: operation(op)).
                      grid(row=operations_positions[i][0], column=operations_positions[i][1]))
#clear button 
clear = Button(root, text='C', padx=30, pady=15, borderwidth=3,
               background="#B1B1B1", fg="black", font="bold",
               command=lambda: operation('C'))
clear.grid(row=4, column=1)

#delete button
dl = Button(root, text='Del', padx=20, pady=15, borderwidth=3,
            background="#B1B1B1", fg="black", font="bold",
            command=delete)
dl.grid(row=4, column=2)

root.mainloop()
