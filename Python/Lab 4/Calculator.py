from tkinter import *
from tkinter.ttk import Style

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")
 
if __name__ == "__main__":
    gui = Tk()
    gui.configure(background=('#88d4b4'))
    gui.title("Calculator")
    gui.geometry("263x150")
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)

    clear_btn = Button(gui, text=' CLS ', fg='black', command=clear, height=1, width=7 )
    clear_btn.grid(row=1,column=0)
    back_btn = Button(gui, text=' Back ', fg='black', command=clear, height=1, width=7 )
    back_btn.grid(row=1,column=1)
    blank_btn = Button(gui, text='  ', fg='black', command=clear, height=1, width=7 )
    blank_btn.grid(row=1,column=2)
    close_btn = Button(gui, text=' Close ', fg='black', command=clear, height=1, width=7 )
    close_btn.grid(row=1,column=3)
    seven_btn = Button(gui, text=' 7 ', fg='black', command=lambda: press(7), height=1, width=7 )
    seven_btn.grid(row=2,column=0)
    eight_btn = Button(gui, text=' 8 ', fg='black', command=lambda: press(8), height=1, width=7 )
    eight_btn.grid(row=2,column=1)
    nine_btn = Button(gui, text=' 9 ', fg='black', command=lambda: press(9), height=1, width=7 )
    nine_btn.grid(row=2,column=2)
    div_btn = Button(gui, text=' / ', fg='black', command=lambda: press('/'), height=1, width=7 )
    div_btn.grid(row=2,column=3)
    four_btn = Button(gui, text=' 4 ', fg='black', command=lambda: press(4), height=1, width=7 )
    four_btn.grid(row=3,column=0)
    five_btn = Button(gui, text=' 5 ', fg='black', command=lambda: press(5), height=1, width=7 )
    five_btn.grid(row=3,column=1)
    six_btn = Button(gui, text=' 6 ', fg='black', command=lambda: press(6), height=1, width=7 )
    six_btn.grid(row=3,column=2)
    mul_btn = Button(gui, text=' * ', fg='black', command=lambda: press('*'), height=1, width=7 )
    mul_btn.grid(row=3,column=3)
    one_btn = Button(gui, text=' 1 ', fg='black', command=lambda: press(1), height=1, width=7 )
    one_btn.grid(row=4,column=0)
    two_btn = Button(gui, text=' 2 ', fg='black', command=lambda: press(2), height=1, width=7 )
    two_btn.grid(row=4,column=1)
    three_btn = Button(gui, text=' 3 ', fg='black', command=lambda: press(3), height=1, width=7 )
    three_btn.grid(row=4,column=2)
    minus_btn = Button(gui, text=' - ', fg='black', command=lambda: press('-'), height=1, width=7 )
    minus_btn.grid(row=4,column=3)
    zero_btn = Button(gui, text=' 0 ', fg='black', command=lambda: press(0), height=1, width=7 )
    zero_btn.grid(row=5,column=0)
    dot_btn = Button(gui, text=' . ', fg='black', command=lambda: press('.'), height=1, width=7 )
    dot_btn.grid(row=5,column=1)
    equal_btn = Button(gui, text=' = ', fg='black', command=lambda: press('='), height=1, width=7 )
    equal_btn.grid(row=5,column=2)
    plus_btn = Button(gui, text=' + ', fg='black', command=lambda: press('+'), height=1, width=7 )
    plus_btn.grid(row=5,column=3)
# start the GUI
gui.mainloop()