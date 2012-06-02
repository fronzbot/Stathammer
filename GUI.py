'''
Stathammer (c) 2012
Author : Kevin Fronczak
Email  : kfronczak@gmail.com
Source : http://github.com/fronzbot/Stathammer

This file is part of stathammer.pyw.

Stathammer is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Stathammer is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Stathammer.  If not, see <http://www.gnu.org/licenses/>.
'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import webbrowser

# Table class to handle entry widgets in a cell form
class Table(object):
    # Creates table object with a parent window, row number and column number
    def __init__(self, parent, rows, columns):
        self.parent = parent
        self.rows   = rows
        self.cols   = columns
        self.var    = []
        self.boxes  = []
        for i in range(0, self.rows):
            self.var.append([])
            for j in range(0, self.cols):
                self.var[i].append(StringVar())
    # Creates table at row and col position in parent
    def create(self, row, col):
        for i in range(0, self.rows):
            self.boxes.append([])
            for j in range(0, self.cols):
                box = Entry(self.parent, textvariable=self.var[i][j], width=4,
                            state='readonly', justify='center', borderwidth=2)
                box.grid(column=col+j, row=row+i, sticky=(N,W,E))
                self.boxes[i].append(box)
                box['readonlybackground'] = 'snow2'

    def change_width(self, x, y, width):
        self.boxes[x][y].config(width=width)

    def set_background(self, x, y, color):
        self.boxes[x][y]['readonlybackground'] = color

    def set_font_color(self, x, y, color):
        self.boxes[x][y]['foreground'] = color

    def insert(self, x, y, text):
        self.var[x][y].set(text)
               

    def set_font(self, x, y, font):
        if not font:
            raise ValueError("font must not be empty in GUI.Table.set_font method")
        # If the font parameters are not correct, use default
        fontlist = font.split(" ")
        if len(fontlist) < 3:
            if len(fontlist) == 1:
                try:
                    int(fontlist[0])
                    fontlist.append(fontlist[0])
                    fontlist[0] = 'TkTextFont'
                    fontlist.append('normal')
                    font = " ".join(fontlist)
                except ValueError:
                    if fontlist[0] in ('normal', 'bold', 'roman', 'italic', 'underline', 'overstrike'):
                        font = " ".join(['TkTextFont', '8', fontlist[0]])
            else:
                try:
                    int(fontlist[0])
                    if fontlist[1] in ('normal', 'bold', 'roman', 'italic', 'underline', 'overstrike'):
                        font = " ".join(['TkTextFont', fontlist[0], fontlist[1]])
                    else:
                        font = " ".join([fontlist[1], fontlist[0], 'normal'])
                        
                except ValueError:
                    try:
                        int(fontlist[1])
                        if fontlist[0] in ('normal', 'bold', 'roman', 'italic', 'underline', 'overstrike'):
                            font = " ".join(['TkTextFont', fontlist[1], fontlist[0]])
                        else:
                            font = " ".join([fontlist[0], fontlist[1], 'normal'])
                    except ValueError:
                        if fontlist[0] in ('normal', 'bold', 'roman', 'italic', 'underline', 'overstrike'):
                            font = " ".join([fontlist[1], '8', fontlist[0]])
                        else:
                            font = " ".join([fontlist[0], '8', fontlist[1]])
                    
        self.boxes[x][y]['font'] = font

class Link:
    def __init__(self, parent, text, website):
        self.parent = parent
        self.hyperlink = ttk.Label(parent, text=text, font='TkTextFont 8 underline',
                              foreground='SkyBlue2', cursor='hand2')
        self.hyperlink.bind("<1>", lambda event, text=text: self.click_link(event))
        self.website = website
    def click_link(self, event):
        webbrowser.open(self.website)
        self.hyperlink.configure(foreground='magenta3')


def frame_create(root_window, row, col):
    frame = ttk.Frame(root_window, padding="3 3 12 12")
    frame.grid(column=col, row=row, sticky=(N, E, W, S))
    frame.columnconfigure(col, weight=1)
    frame.rowconfigure(row, weight=1)

    return frame

def label_frame_create(root_window, labelName, row, col):
    frame = ttk.Labelframe(root_window, padding="3 3 12 12", text=labelName)
    frame.grid(column=col, row=row, sticky=(N, E, W, S))
    frame.columnconfigure(col, weight=1)
    frame.rowconfigure(row, weight=1)

    return frame 

def canvas_create(root_window, row, col, dims, color):
    frame = Canvas(root_window, width=dims[0], height=dims[1], bg=color, cursor='tcross')
    frame.grid(column=col, row=row, sticky=(N, E, W, S))
    frame.columnconfigure(col, weight=1)
    frame.rowconfigure(row, weight=1)
    frame['borderwidth'] = 4
    frame['relief'] = 'ridge'

    return frame

def input_create(root_window, type_name, var, width, pos, total_range):
    type_name.lower()
    if type_name == 'entry':
        box = ttk.Entry(root_window, textvariable=var, width=width)
        box.grid(column=pos[1], row=pos[0], sticky=pos[2])
    elif type_name == 'spinbox':
        box = Spinbox(root_window, from_=total_range[0], to=total_range[1],
                      textvariable=var, width=width)
        box.grid(column=pos[1], row=pos[0], sticky=pos[2])
        
    elif type_name == 'slider':
        box = ttk.Scale(root_window, orient=HORIZONTAL, length=width,
                        from_=total_range[0], to=total_range[1], variable=var)
        box.grid(column=pos[1], row=pos[0], sticky=pos[2])
                 
    else:
        raise ValueError(type_name+' is not a valid input type')

    return box

def weapon_boxes(root_window, variables, start_row, start_col, width):
    boxList = []
    row = start_row
    col = start_col
    for variable in variables:
        box = ttk.Combobox(root_window, textvariable=variable, width=width)
        box.grid(column=col, row=row, sticky=(W), padx = 2, pady=3)
        boxList.append(box)
        row = row + 1
        col = col

    return boxList

def create_stat_table(table):
    table.create(0, 0)
    table.set_background(0, 0, 'gray50')
    for i in range(0, 4):
        for j in range(0, 5):
            table.change_width(i, j, 8)
    table.insert(  0, 1, 'Average')
    table.set_font(0, 1, 'bold')
    table.insert(  0, 2, 'Std. Dev')
    table.set_font(0, 2, 'bold')
    table.insert(  0, 3, 'Min')
    table.set_font(0, 3, 'bold')
    table.insert(  0, 4, 'Max')
    table.set_font(0, 4, 'bold')
    table.insert(  1, 0, 'Hits')
    table.set_font(1, 0, 'bold')
    table.insert(  2, 0, 'Wounds')
    table.set_font(2, 0, 'bold')
    table.insert(  3, 0, 'Kills')
    table.set_font(3, 0, 'bold')

   
