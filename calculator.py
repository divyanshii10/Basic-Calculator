from tkinter import *
root = Tk()
root.geometry('353x479')
root.title('Calculator')
root.wm_iconbitmap('cal.ico')
root.config(background='black')

def click(event):
    global scval 
    text = event.widget.cget('text')
    if text == '=': 
        if scVal.get().isdigit():
            val = int(scVal.get())
        else:
           val = eval(screen.get())
        scVal.set(val)
        screen.update()

    elif text == 'C':
        scVal.set('')
        screen.update()

    else: 
        scVal.set(scVal.get() + text)
        screen.update()

# entry widget for output
scVal = StringVar()
scVal.set('')
screen = Entry(root,textvariable=scVal, font='Lucida 30 bold')
screen.pack(fill=X,pady=10,padx=5)

# buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('-', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('/', 4, 2), ('=', 4, 3),
]
# frame for buttons
frame = Frame(root,background='black')
frame.pack()

for (text,row,col) in buttons:
    b = Button(frame, text=text, padx=10, pady=10,font='Lucida 25 bold')
    b.grid(row=row, column=col, padx=5, pady=5)
    b.bind('<Button-1>',click)

root.mainloop()