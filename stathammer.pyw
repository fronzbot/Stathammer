#!/usr/bin/python

version = "3.0a"

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import random
import os
import GUI

# Method to properly round float to int
def round_int(num):
    if (num > 0):
        return int(num+.5)
    else:
        return int(num-.5)

# Method used to return window to previous state (on last close)
def load_init():
    f = open('.init', 'r')
    data = f.readlines()
    data[0] = data[0].split(" ")
    data[1] = data[1].split(" ")
    f.close()
 
    Shotval.set(data[0][0])
    BSval.set(data[0][1])
    WSval.set(data[0][2])
    Sval.set(data[0][3])

    Enemyval.set(data[1][0])
    WSOval.set(data[1][1])
    Tval.set(data[1][2])
    SVval.set(data[1][3])
   
# Saves window state for re-initialization
def save_init():
    attacker = str(Shotval.get())+" "+str(BS_box.get())+" "+str(WS_box.get())+" "+str(S_box.get())
    enemy = str(Enemyval.get())+" "+str(WSO_box.get())+" "+str(T_box.get())+" "+str(SV_box.get())
    f = open('.init', 'w')
    f.write(attacker+" \n"+enemy)
    f.close
    root.destroy()

# Save attacker profile
def save_attacker():
    if not os.path.exists('profiles'):
        os.mkdir('profiles')
    types = [('Attacker Profile', '.at'),('All Files', '.*')]
    saveFile = filedialog.asksaveasfilename(defaultextension='.at', initialdir='profiles',
                                            filetypes=types)
    if saveFile != '':
        save = open(saveFile, 'w')
        save.write(str(Shotval.get())+" "+str(BS_box.get())+" "+str(WS_box.get())+" "+str(S_box.get()))
        save.close()

# Save enemy profile
def save_enemy():
    if not os.path.exists('profiles'):
        os.mkdir('profiles')
    types = [('Enemy Profile', '.op'),('All Files', '.*')]
    saveFile = filedialog.asksaveasfilename(defaultextension='.op', initialdir='profiles',
                                            filetypes=types)
    if saveFile != '':
        save = open(saveFile, 'w')
        save.write(str(Enemyval.get())+" "+str(WSO_box.get())+" "+str(T_box.get())+" "+str(SV_box.get()))
        save.close()

# Load attacker profile
def load_attacker():
    types = [('Attacker Profile', '.at'),('All Files', '.*')]
    loadFile = filedialog.askopenfilename(initialdir='profiles',
                                            filetypes=types)
    if loadFile[-3:] != '.at':
        messagebox.showinfo(message='ERROR', detail='Invalid File Type!', icon='error', default='ok',parent=root)
    else:
        load = open(loadFile, 'r')
        data = load.readline().split(" ")
        load.close()
        
        Shotval.set(data[0])
        BSval.set(data[1])
        WSval.set(data[2])
        Sval.set(data[3])
        root.update()

def load_enemy():
    types = [('Enemy Profile', '.op'),('All Files', '.*')]
    loadFile = filedialog.askopenfilename(initialdir='profiles',
                                            filetypes=types)
    if loadFile[-3:] != '.op':
        messagebox.showinfo(message='ERROR', detail='Invalid File Type!', icon='error', default='ok',parent=root)
    else:
        load = open(loadFile, 'r')
        data = load.readline().split(" ")
        load.close()
        
        Enemyval.set(data[0])
        WSOval.set(data[1])
        Tval.set(data[2])
        SVval.set(data[3])
        root.update()


# Monte_carlo algorithm   
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

# Method to create probability distribution
def create_distribution(data):
    try:
        attacks = int(Shotval.get())
        enemies = int(Enemyval.get())
        if attacks > enemies:
            attacks = enemies
        if attacks < 5:
            attacks = 5
    except ValueError:
        Shotval.set(1)
        attacks = 5

    # Sort Data from 0 -> inf
    data.sort()
    probdict = {}
    for val in data:
        if val > attacks:
            val = attacks
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
    
    for i in range(0, attacks+1):
        x_mark = 50 + (i * 400/attacks)
        
            
        # Create x-axis in intervals of 5
        if attacks >=50:
            if i % 5 == 0:
                graphframe.create_line(x_mark,300,x_mark,295, width=2)
        # Create x-axis in intervals of 1
        else:
            graphframe.create_line(x_mark,300,x_mark,295, width=2)

        # Add x-labels 
        if attacks >= 50:
            if i % 5 == 0:
                graphframe.create_text(x_mark,300, text='%d'% (i), anchor=N)
        elif attacks >= 20:
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
        x_pos = 50 + (key * 400/attacks)
        y_pos = 300 - round((probdict[key]*25000))/largestProb

        if x_pos >= 50:
            graphframe.create_rectangle(x_pos-3, y_pos-3, x_pos+3, y_pos+3, fill='black')
            graphframe.create_line(x_pos, 300, x_pos, y_pos, width=4)

    
    for i in range(0, largestProb):
        y_mark = 300 - (250*i/largestProb)
        
        # Create y-axis in intervals of 10
        if largestProb > 30:
            if i%10 == 0:
                graphframe.create_line(45, y_mark, 55, y_mark)
                graphframe.create_text(20, y_mark, text='%s'% (str(i)+'%'), anchor=W)
       # Create y-axis in intervals of 5 
        elif largestProb > 15:
            if i%5 == 0:
                graphframe.create_line(45, y_mark, 55, y_mark)
                graphframe.create_text(20, y_mark, text='%s'% (str(i)+'%'), anchor=W)
        # Create y-axis in intervals of 1
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

    bs  = int(BS_box.get())
    ws  = int(WS_box.get())
    wso = int(WSO_box.get())
    s   = int(S_box.get())
    t   = int(T_box.get())
    sv  = int(S_box.get())
    attacks = int(Shotval.get())


    # Retrieve score needed to hit
    if attackType.get() == 'shoot':
        if bs > 5:
            bs = 5
        scoreToHit = 7-bs
    else:
        if wso > 2*ws:
            scoreToHit = 5
        elif wso < ws:
            scoreToHit = 3
        else:
            scoreToHit = 4

    # Retrieve score needed to wound
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

    if s > 2*t:
        sv = 0
        
    while(loop_count < iterations):
        PBAR.step(1.0)
        root.update()
        
        
        try:
            dice = monte_carlo(attacks)
        except ValueError:
            Shotval.set(1)
            dice = monte_carlo(1)
            
        hit_prob = 0
        
        for i in range(scoreToHit-1,6):
            hit_prob += dice[i]

                
        hits = round_int(hit_prob*attacks)
        
        

        dice = monte_carlo(hits)
        wound_prob = 0
        for i in range(scoreToWound-1, 6):
            wound_prob += dice[i]
        
        wounds = round_int(wound_prob*hits)

        if sv: 
            dice = monte_carlo(wounds)
            save_prob = 0
            for i in range(sv-1, 6):
                save_prob += dice[i]
            kills = round_int((1-save_prob)*wounds)

        else:
            kills = wounds

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
root.wm_iconbitmap('staticon.ico')
root.protocol('WM_DELETE_WINDOW', save_init)



#=============#
#   Frames    #  
#=============#
mainframe = GUI.frame_create(root, 0, 0)
statframe = GUI.frame_create(mainframe, 0, 0)
sideframe = GUI.frame_create(mainframe, 0, 1)

atstatframe = GUI.label_frame_create(statframe, 'Attacker', 1, 0)
atsvldframe = GUI.frame_create(atstatframe, 1, 0)
attackframe = GUI.frame_create(atstatframe, 0, 0)

opstatframe = GUI.label_frame_create(statframe, 'Enemy', 2, 0)
enemyframe = GUI.frame_create(opstatframe, 0, 0)
opsvldframe = GUI.frame_create(opstatframe, 1, 0)

probframe = GUI.label_frame_create(sideframe, 'Results', 2, 1)

barframe = GUI.label_frame_create(statframe, 'Simulation Control', 3, 0)

graphframe = GUI.canvas_create(sideframe, 1, 1, [500, 350])


#=============#
#   Entries   #  
#=============#
Shotval = StringVar()
Shot_box = GUI.input_create(attackframe, 'entry', Shotval, 4, [1, 1, (W)], [0])
Shotval.set(1)

BSval = StringVar()
BS_box = GUI.input_create(attackframe, 'spinbox', BSval, 4, [2, 1, (W)], [1, 12])

WSval = StringVar()
WS_box = GUI.input_create(attackframe, 'spinbox', WSval, 4, [3, 1, (W)], [1, 10])

Sval = StringVar()
S_box = GUI.input_create(attackframe, 'spinbox', Sval, 4, [4, 1, (W)], [1, 10])

Enemyval = StringVar()
Enemy_box = GUI.input_create(enemyframe, 'entry', Enemyval, 4, [0, 1, (W)], [0])
Enemyval.set(1)

WSOval = StringVar()
WSO_box = GUI.input_create(enemyframe, 'spinbox', WSOval, 4, [1, 1, (W)], [1, 12])

Tval = StringVar()
T_box = GUI.input_create(enemyframe, 'spinbox', Tval, 4, [2, 1, (W)], [1, 10])

SVval = StringVar()
SV_box = GUI.input_create(enemyframe, 'spinbox', SVval, 4, [3, 1, (W)], [2, 6])

IterVal = StringVar()
IterSlide = GUI.input_create(barframe, 'slider', IterVal, 120, [0, 0, (W, E)], [10.0, 50000.0])
IterSlide.set(2500.0)

#=============#
#   Buttons   #  
#=============#
calculate = ttk.Button(probframe, text='Calculate', command=shooting)
calculate.grid(column=0, row=0, sticky=(W, E))

saveAttack = ttk.Button(atsvldframe, text = 'Save', command=save_attacker)
saveAttack.grid(column=1, row=0, sticky=(W, E, N, S))

loadAttack = ttk.Button(atsvldframe, text = 'Load', command=load_attacker)
loadAttack.grid(column=0, row=0, sticky=(W, E, N, S))

saveEnemy = ttk.Button(opsvldframe, text = 'Save', command=save_enemy)
saveEnemy.grid(column=1, row=0, sticky=(W, E, N, S))

loadEnemy = ttk.Button(opsvldframe, text = 'Load', command=load_enemy)
loadEnemy.grid(column=0, row=0, sticky=(W, E, N, S))

attackType = StringVar()
shooting = ttk.Radiobutton(attackframe, text='Shooting', variable=attackType, value='shoot')
shooting.grid(column=0, row=0, sticky=(W,E,N,S))
assault  = ttk.Radiobutton(attackframe, text='Assault', variable=attackType, value='assault')
assault.grid(column=1, row=0, sticky=(W,E,N,S))
attackType.set('shoot')
#=============#
#   Labels    #  
#=============#
SHOT_label = ttk.Label(attackframe, text='# Attacks')
SHOT_label.grid(column=0, row=1, sticky=(W, E), ipady=5)

BS_label = ttk.Label(attackframe, text='BS')
BS_label.grid(column=0, row=2, sticky=(W, E), ipady=5)

WS_label = ttk.Label(attackframe, text='WS')
WS_label.grid(column=0, row=3, sticky=(W, E), ipady=5)

S_label = ttk.Label(attackframe, text='S')
S_label.grid(column=0, row=4, sticky=(W, E), ipady=5)


ENEMY_label = ttk.Label(enemyframe, text="# Enemies")
ENEMY_label.grid(column=0, row=0, sticky=(W, E), ipady=5)


WSO_label = ttk.Label(enemyframe, text='WS')
WSO_label.grid(column=0, row=1, sticky=(W, E), ipady=5)

T_label = ttk.Label(enemyframe, text='T')
T_label.grid(column=0, row=2, sticky=(W, E), ipady=5)

SV_label = ttk.Label(enemyframe, text='SV')
SV_label.grid(column=0, row=3, sticky=(W, E), ipady=5)

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

PBAR = ttk.Progressbar(barframe, orient=HORIZONTAL, length=120, mode='determinate')
PBAR.grid(column=0, row=1, sticky=(W,E,N))
PBAR['value']=0

#=============#
#   Graph     #  
#=============#
graphframe.create_line(50,300,450,300, width=2)  # X-axis
graphframe.create_line(50,300,50,50, width=2)    # Y-axis

root.bind('<Return>', shooting)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


try:
    load_init()
except:
    pass

root.mainloop()
