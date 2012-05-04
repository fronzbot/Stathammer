#!/usr/bin/python

version = "0.01a"

from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Stathammer "+version)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

BS_entry = ttk.Entry(mainframe, width=7)
BS_entry.grid(column=2, row=1, sticky=(W,E))

ttk.Label(mainframe).grid(column=2, row=2, sticky=(W,E))
ttk.Button(mainframe, text="Calculate").grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

BS_entry.focus()

root.mainloop()
