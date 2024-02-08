import tkinter as tk

def click(value):
    global expression
    if value == '=':
        try: 
            r = str(eval(expression))
            entry_1.delete(0,tk.END)
            entry_1.insert(tk.END,r)
            expression = r
        except Exception as e:
            entry_1.delete(0,tk.END)
            entry_1.insert(tk.END,'Error')
            expression = ''
    else:
        expression += value
        entry_1.insert(tk.END, value)  

def clear():
    global expression
    global list
    expression = ""  
    entry_1.delete(0, tk.END)  
    list = ''

win = tk.Tk()
win.geometry('322x690')
win.title('Калькулятор')

frame = tk.Frame(win)
frame.grid(row=0, column=0, columnspan=4, sticky='nsew')

entry_1 = tk.Entry(frame, width=50)
entry_1.grid(row=0,column=0,columnspan=4)
entry_1.bind('<Key>',lambda e:'break')
entry_1.pack()

car = (
    ('7', '8', '9', '*', '4'),
    ('4', '5', '6', '-', '4'),
    ('1', '2', '3', '+', '4'),       
    ('0', '.', '=', '/', '4')
)

expression = ""
list = ''

button_clear = tk.Button(win, text='C', command=clear)
button_clear.grid(row=1, column=3, sticky='nsew')

for i in range(4):
    for i1 in range(5):
        if car[i][i1] == '=':
            tk.Button(win, width=10, height=10, text=car[i][i1], command=lambda value=car[i][i1]: click(value)).grid(row=i+2, column=i1, sticky='nsew', padx=1, pady=1)
        else:
            tk.Button(win, width=10, height=10, text=car[i][i1], command=lambda value=car[i][i1]: click(value)).grid(row=i+2, column=i1, sticky='nsew', padx=1, pady=1)

win.mainloop()