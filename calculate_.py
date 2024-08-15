import tkinter as tk

def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

window = tk.Tk()
window.title('Калькулятор')
window.geometry('400x400')
window.resizable(False, False)
button_add = tk.Button(window, text='+', width=4, height=3, command=add)
button_add.place(x=100, y=250)
button_sub = tk.Button(window, text='-', width=4, height=3, command=sub)
button_sub.place(x=150, y=250)
button_mul = tk.Button(window, text='*', width=4, height=3, command=mul)
button_mul.place(x=210, y=250)
button_div = tk.Button(window, text='/', width=4, height=3, command=div)
button_div.place(x=260, y=250)
number1_entry = tk.Entry(window, width=32)
number1_entry.place(x=100, y=75)
number2_entry = tk.Entry(window, width=32)
number2_entry.place(x=100, y=125)
answer_entry = tk.Entry(window, width=32)
answer_entry.place(x=100, y=175)
number1 = tk.Label(window, text='Введите первое число')
number1.place(x=100, y=50)
number2 = tk.Label(window, text='Введите второе число')
number2.place(x=100, y=100)
answer = tk.Label(window, text='Результат')
answer.place(x=100, y=150)

window.mainloop()

