#!/usr/bin/python

version = "1.0a"

from tkinter import *
from tkinter import ttk
import random

def round_int(num):
    if (num > 0):
        return int(num+.5)
    else:
        return int(num-.5)
    
def monte_carlo(iters):
    cnt = 0
    if iters == 0:
        return [0, 0, 0, 0, 0, 0]
    rollProb = [0, 0, 0, 0, 0, 0]
    while(cnt < iters):
        roll = random.randint(1,6)
        rollProb[roll-1] += 1
        cnt += 1

    for i in range(len(rollProb)):
        rollProb[i] /= iters

    return rollProb

def create_distribution(data):
    try:
        enemies = int(Enemyval.get())
    except ValueError:
        Enemyval.set(1)
        enemies = 1

    data.sort()
    probdict = {}
    for val in data:
        if val > enemies:
            val = enemies
        try:
            probdict[val] += 1
        except KeyError:
            probdict[val] = 1

    totalPoints = len(probdict)
    keyNum = 0
    graphframe.delete(ALL)
    root.update()
    graphframe.create_line(50,300,450,300, width=2)  # X-axis
    graphframe.create_line(50,300,50,50, width=2)    # Y-axis
    
    for i in range(0, enemies+1):
        x_mark = 50 + (i * 400/enemies)
        if enemies >=50:
            if i % 5 == 0:
                graphframe.create_line(x_mark,300,x_mark,295, width=2)
        else:
            graphframe.create_line(x_mark,300,x_mark,295, width=2)
        if enemies >= 50:
            if i % 5 == 0:
                graphframe.create_text(x_mark,300, text='%d'% (i), anchor=N)
        elif enemies >= 20:
            if i % 2 == 0:
                graphframe.create_text(x_mark,300, text='%d'% (i), anchor=N)
        else:
            graphframe.create_text(x_mark,300, text='%d'% (i), anchor=N)
    probs = []
    total = 0
    for key in probdict:
        probdict[key] /= len(data)
        probs.append(probdict[key])

    probs = sorted(probs)	 	
    largestProb = int(probs.pop()*100)+10
    
    for key in probdict:
        x_pos = 50 + (key * 400/enemies)
        y_pos = 300 - round((probdict[key]*25000))/largestProb
        graphframe.create_rectangle(x_pos-3, y_pos-3, x_pos+3, y_pos+3, fill='black')
        graphframe.create_line(x_pos, 300, x_pos, y_pos, width=4)
        
    
    for i in range(0, largestProb):
        y_mark = 300 - (250*i/largestProb)
        if largestProb > 30:
            if i%10 == 0:
                graphframe.create_line(45, y_mark, 55, y_mark)
                graphframe.create_text(20, y_mark, text='%s'% (str(i)+'%'), anchor=W)
        elif largestProb > 15:
            if i%5 == 0:
                graphframe.create_line(45, y_mark, 55, y_mark)
                graphframe.create_text(20, y_mark, text='%s'% (str(i)+'%'), anchor=W)
        else:
            graphframe.create_line(45, y_mark, 55, y_mark)
            graphframe.create_text(20, y_mark, text='%s'% (str(i)+'%'), anchor=W)
    	        
    root.update()
        
def shooting(*args):
    iterations = int(IterSlide.get())
    if iterations == 0:
        iterations = 1
    PBAR['maximum'] = iterations
    
    MeanHit    = 0
    MeanWound  = 0
    MeanKill   = 0
    kill_list  = []
    loop_count = 0
    while(loop_count < iterations):
        PBAR.step(1.0)
        root.update()
        bs = int(BS_box.get())
        s  = int(S_box.get())
        t  = int(T_box.get())
        sv = int(S_box.get())
        if bs > 5:
            bs = 5
        
        scoreToHit = 7-bs
        try:
            dice = monte_carlo(int(Shotval.get()))
        except ValueError:
            Shotval.set(1)
            dice = monte_carlo(1)
            
        hit_prob = 0
        for i in range(scoreToHit-1,6):
            hit_prob += dice[i]

        hits = round_int(hit_prob*int(Shotval.get()))
        
        if s == t:
            scoreToWound = 4
        elif s < t:
            scoreToWound = 4 + (t-s)
            if scoreToWound > 6:
                scoreToWound = 7
        elif s > t:
            scoreToWound = 4 - (s-t)
            if scoreToWound < 2:
                scoreToWound = 2

        dice = monte_carlo(hits)
        wound_prob = 0
        for i in range(scoreToWound-1, 6):
            wound_prob += dice[i]

        wounds = round_int(wound_prob*hits)

        dice = monte_carlo(wounds)
        save_prob = 0
        for i in range(sv-1, 6):
            save_prob += dice[i]

        saves = round_int(save_prob*wounds)

        kills = wounds - saves
        kill_list.append(kills)
        MeanHit += hits
        MeanWound += wounds
        MeanKill += kills

        loop_count += 1


    MeanHit /= iterations
    MeanWound /= iterations
    MeanKill /= iterations


    HitVal.set(round_int(MeanHit))
    WoundVal.set(round_int(MeanWound))
    KillVal.set(round_int(MeanKill))

    create_distribution(kill_list)
    
'''
    GUI Setup
'''
root = Tk()
root.title("Stathammer "+version)


#=============#
#   Frames    #  
#=============#

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

attackframe = ttk.Frame(mainframe, padding="3 3 12 12")
attackframe.grid(column=0, row=0, stick=(N, W, E, S))
attackframe.columnconfigure(0, weight=1)
attackframe.rowconfigure(0, weight=1)

statframe = ttk.Labelframe(mainframe, padding="3 3 12 12", text='Stats')
statframe.grid(column=0, row=1, sticky=(N, W, E, S))
statframe.columnconfigure(0, weight=1)
statframe.rowconfigure(1, weight=1)
statframe['borderwidth'] = 2
statframe['relief'] = 'groove'


calcframe = ttk.Frame(mainframe, padding="3 3 12 12")
calcframe.grid(column=1, row=0, sticky=(N, W, E, S))
calcframe.columnconfigure(1, weight=1)
calcframe.rowconfigure(0, weight=1)

probframe = ttk.Labelframe(mainframe, padding="3 3 12 12", text='Results')
probframe.grid(column=1, row=2, sticky=(N, W, E, S))
probframe.columnconfigure(2, weight=1)
probframe.rowconfigure(1, weight=1)

barframe = ttk.Labelframe(mainframe, padding="3 3 12 12", text='Simulation Control')
barframe.grid(column=0, row=2, sticky=(N,W,E,S))
barframe.columnconfigure(0, weight=1)
barframe.rowconfigure(2, weight=1)

graphframe = Canvas(mainframe, width=500, height=350, bg='white')
graphframe.grid(column=1, row=1, sticky=(N, W, E, S))
graphframe.columnconfigure(1, weight=1)
graphframe.rowconfigure(1, weight=1)
graphframe['borderwidth'] = 5
graphframe['relief'] = 'ridge'

#=============#
#   Entries   #  
#=============#
Shotval = StringVar()
Shot_box = ttk.Entry(statframe, textvariable=Shotval, width=4)
Shot_box.grid(column=1, row=1, sticky=(W))
Shotval.set(1)

BSval = StringVar()
BS_box = Spinbox(statframe, from_=1, to=12, textvariable=BSval, width=4)
BS_box.grid(column=1, row=2, sticky=(W))

WSval = StringVar()
WS_box = Spinbox(statframe, from_=1, to=10, textvariable=WSval, width=4)
WS_box.grid(column=1, row=3, sticky=(W))

Sval = StringVar()
S_box = Spinbox(statframe, from_=1, to=10, textvariable=Sval, width=4)
S_box.grid(column=1, row=4, sticky=(W))

Enemyval = StringVar()
Enemy_box = ttk.Entry(statframe, textvariable=Enemyval, width=4)
Enemy_box.grid(column=1, row=6, sticky=(W))
Enemyval.set(1)

WSOval = StringVar()
WSO_box = Spinbox(statframe, from_=1, to=12, textvariable=WSOval, width=4)
WSO_box.grid(column=1, row=7, sticky=(W))

Tval = StringVar()
T_box = Spinbox(statframe, from_=1, to=10, textvariable=Tval, width=4)
T_box.grid(column=1, row=8, sticky=(W))

SVval = StringVar()
SV_box = Spinbox(statframe, from_=2, to=6, textvariable=SVval, width=4)
SV_box.grid(column=1, row=9, sticky=(W))

IterVal = StringVar()
IterSlide = ttk.Scale(barframe, orient=HORIZONTAL, length=200, from_=1.0, to=50000.0, variable=IterVal)
IterSlide.grid(column=0, row=0, sticky=(W,E))
IterSlide.set(4000.0)

#=============#
#   Buttons   #  
#=============#
calculate = ttk.Button(probframe, text='Calculate', command=shooting)
calculate.grid(column=0, row=0, sticky=(W, E))


#=============#
#   Labels    #  
#=============#
SHOT_label = ttk.Label(statframe, text='# Attacks')
SHOT_label.grid(column=0, row=1, sticky=(W, E), ipady=5)

YOU_label = ttk.Label(statframe, text='You', justify='center')
YOU_label.grid(column=1, row=0, sticky=(W, E), ipady=5)

BS_label = ttk.Label(statframe, text='BS')
BS_label.grid(column=0, row=2, sticky=(W, E), ipady=5)

WS_label = ttk.Label(statframe, text='WS')
WS_label.grid(column=0, row=3, sticky=(W, E), ipady=5)

S_label = ttk.Label(statframe, text='S')
S_label.grid(column=0, row=4, sticky=(W, E), ipady=5)

OP_label = ttk.Label(statframe, text='Enemy', justify='center')
OP_label.grid(column=1, row=5, sticky=(W, E), ipady=5)

ENEMY_label = ttk.Label(statframe, text='# Enemies')
ENEMY_label.grid(column=0, row=6, sticky=(W, E), ipady=5)

WSO_label = ttk.Label(statframe, text='WS')
WSO_label.grid(column=0, row=7, sticky=(W, E), ipady=5)

T_label = ttk.Label(statframe, text='T')
T_label.grid(column=0, row=8, sticky=(W, E), ipady=5)

SV_label = ttk.Label(statframe, text='SV')
SV_label.grid(column=0, row=9, sticky=(W, E), ipady=5)

HIT_label = ttk.Label(probframe, text='Average Hits')
HIT_label.grid(column=0, row=1, sticky=(N, W, E), ipadx=10)

WOUND_label = ttk.Label(probframe, text='Average Wounded')
WOUND_label.grid(column=0, row=2, sticky=(N, W, E), ipadx=10)

KILL_label = ttk.Label(probframe, text='Average Killed')
KILL_label.grid(column=0, row=3, sticky=(N, W, E), ipadx=10)

HitVal = StringVar()
HITNUM_label = ttk.Label(probframe, textvariable=HitVal)
HITNUM_label.grid(column=1, row=1, sticky=(N, W, E))
HitVal.set('0')

WoundVal = StringVar()
WOUNDNUM_label = ttk.Label(probframe, textvariable=WoundVal)
WOUNDNUM_label.grid(column=1, row=2, sticky=(N, W, E))
WoundVal.set('0')

KillVal = StringVar()
KILLNUM_label = ttk.Label(probframe, textvariable=KillVal)
KILLNUM_label.grid(column=1, row=3, sticky=(N, W, E))
KillVal.set('0')

PBAR = ttk.Progressbar(barframe, orient=HORIZONTAL, length=200, mode='determinate')
PBAR.grid(column=0, row=1, sticky=(W,E,N))
PBAR['value']=0

#=============#
#   Graph     #  
#=============#
graphframe.create_line(50,300,450,300, width=2)  # X-axis
graphframe.create_line(50,300,50,50, width=2)    # Y-axis

root.bind('<Return>', shooting)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


root.mainloop()
