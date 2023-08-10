# calculator
from tkinter import *
from tkinter import Tk

wi = Tk()


e = Entry(wi, width=50, fg="black", justify="right")
e.grid(row=0, column=0, columnspan=4, ipady=10)


def oc(num):
    x = e.get()
    e.delete(0, END)
    e.insert(0, str(x) + str(num))


def clear():
    e.delete(0, END)


def add():
    global a, z
    z = "+"
    a = e.get()
    e.delete(0, END)


def sub():
    global a, z
    z = "-"
    a = e.get()
    e.delete(0, END)


def mul():
    global a, z
    z = "*"
    a = e.get()
    e.delete(0, END)


def div():
    global a, z
    z = "/"
    a = e.get()
    e.delete(0, END)


def equal():
    second = e.get()
    if z == "+":
        result = float(a) + float(second)
    elif z == "-":
        result = float(a) - float(second)
    elif z == "*":
        result = float(a) * float(second)

    elif z == "/":
        result = float(a) / float(second)

    e.delete(0, END)
    e.insert(0, result)


b1 = Button(
    wi,
    text="1",
    padx=45,
    pady=10,
    fg="red",
    command=lambda: oc(1),
)
b2 = Button(
    wi,
    text="2",
    padx=45,
    pady=10,
    fg="red",
    command=lambda: oc(2),
)
b3 = Button(
    wi,
    text="3",
    padx=45,
    pady=10,
    fg="red",
    command=lambda: oc(3),
)
b4 = Button(
    wi,
    text="4",
    padx=45,
    pady=10,
    fg="red",
    command=lambda: oc(4),
)
b5 = Button(
    wi,
    text="5",
    padx=45,
    pady=10,
    fg="red",
    command=lambda: oc(5),
)
b6 = Button(
    wi,
    text="6",
    padx=45,
    pady=10,
    fg="red",
    command=lambda: oc(6),
)
b7 = Button(
    wi,
    text="7",
    padx=45,
    pady=10,
    fg="red",
    command=lambda: oc(7),
)
b8 = Button(
    wi,
    text="8",
    padx=45,
    pady=10,
    fg="red",
    command=lambda: oc(8),
)
b9 = Button(
    wi,
    text="9",
    padx=45,
    pady=10,
    fg="red",
    command=lambda: oc(9),
)
b0 = Button(
    wi,
    text="0",
    padx=45,
    pady=10,
    fg="red",
    command=lambda: oc(0),
)

ba = Button(
    wi,
    text="+",
    padx=45,
    pady=10,
    fg="red",
    command=add,
)
bs = Button(
    wi,
    text="-",
    padx=45,
    pady=10,
    fg="red",
    command=sub,
)
bm = Button(
    wi,
    text="*",
    padx=45,
    pady=10,
    fg="red",
    command=mul,
)
bd = Button(
    wi,
    text="/",
    padx=45,
    pady=10,
    fg="red",
    command=div,
)
be = Button(
    wi,
    text="=",
    padx=45,
    pady=10,
    fg="red",
    command=equal,
)
bc = Button(
    wi,
    text="C",
    padx=45,
    pady=10,
    fg="red",
    command=clear,
)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
b0.grid(row=4, column=1)

ba.grid(row=1, column=4)
bs.grid(row=2, column=4)
bm.grid(row=3, column=4)
bd.grid(row=4, column=4)
be.grid(row=4, column=0)
bc.grid(row=4, column=2)
wi.mainloop()
