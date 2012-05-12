from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

    
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

def canvas_create(root_window, row, col, dims):
    frame = Canvas(root_window, width=dims[0], height=dims[1], bg='white')
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
