#!/usr/bin/python

version = 0.04

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import random
import os
import GUI
import simulation

# Method used to return window to previous state (on last close)
def load_init():
    f = open('.init', 'r')
    data = f.readlines()
    data[0] = data[0].split(" ")
    data[1] = data[1].split(" ")
    f.close()

    Unitvar.set(" ".join(data[0][0].split("_")))
    Shotval.set(data[0][1])
    WSval.set(data[0][2])
    BSval.set(data[0][3])
    Sval.set(data[0][4])
    TAval.set(data[0][5])
    Wval.set(data[0][6])
    Ival.set(data[0][7])
    Aval.set(data[0][8])
    SVAval.set(data[0][9])

    UnitvarO.set(" ".join(data[1][0].split("_")))
    Enemyval.set(data[1][1])
    WSOval.set(data[1][2])
    BSOval.set(data[1][3])
    SOval.set(data[1][4])
    Tval.set(data[1][5])
    WOval.set(data[1][6])
    IOval.set(data[1][7])
    AOval.set(data[1][8])
    SVval.set(data[1][9])
   
# Saves window state for re-initialization
def save_init():
    na   = "_".join(Unitvar.get().split(" "))
    shot = Shotval.get()
    wsa  = WS_box.get()
    bsa  = BS_box.get()
    sa   = S_box.get()
    ta   = TA_box.get()
    wa   = W_box.get()
    ia   = I_box.get()
    aa   = A_box.get()
    sva  = SVA_box.get()

    ne   = "_".join(UnitvarO.get().split(" "))
    enem = Enemyval.get()
    wso  = WSO_box.get()
    bso  = BSO_box.get()
    so   = SO_box.get()
    to   = T_box.get()
    wo   = WO_box.get()
    io   = IO_box.get()
    ao   = AO_box.get()
    svo  = SV_box.get()
    
    attacker = (str(na)+" "+str(shot)+" "+str(wsa)+" "+str(bsa)+" "+str(sa)
                +" "+str(ta)+" "+str(wa)+" "+str(ia)+" "+str(aa)+" "+str(sva))
    
    enemy = (str(ne)+" "+str(enem)+" "+str(wso)+" "+str(bso)+" "+str(so)
             +" "+str(to)+" "+str(wo)+" "+str(io)+" "+str(ao)+" "+str(svo))
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
        na   = "_".join(Unitvar.get().split(" "))
        shot = Shotval.get()
        wsa  = WS_box.get()
        bsa  = BS_box.get()
        sa   = S_box.get()
        ta   = TA_box.get()
        wa   = W_box.get()
        ia   = I_box.get()
        aa   = A_box.get()
        sva  = SVA_box.get()
        attacker = (str(na)+" "+str(shot)+" "+str(wsa)+" "+str(bsa)+" "+str(sa)
                    +" "+str(ta)+" "+str(wa)+" "+str(ia)+" "+str(aa)+" "+str(sva))
        save = open(saveFile, 'w')
        save.write(attacker)
        save.close()

# Save enemy profile
def save_enemy():
    if not os.path.exists('profiles'):
        os.mkdir('profiles')
    types = [('Enemy Profile', '.op'),('All Files', '.*')]
    saveFile = filedialog.asksaveasfilename(defaultextension='.op', initialdir='profiles',
                                            filetypes=types)
    if saveFile != '':
        ne   = "_".join(UnitvarO.get().split(" "))
        enem = Enemyval.get()
        wso  = WSO_box.get()
        bso  = BSO_box.get()
        so   = SO_box.get()
        to   = T_box.get()
        wo   = WO_box.get()
        io   = IO_box.get()
        ao   = AO_box.get()
        svo  = SV_box.get()
        enemy = (str(ne)+" "+str(enem)+" "+str(wso)+" "+str(bso)+" "+str(so)
                 +" "+str(to)+" "+str(wo)+" "+str(io)+" "+str(ao)+" "+str(svo))
        save = open(saveFile, 'w')
        save.write(enemy)
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
        
        Unitvar.set(" ".join(data[0].split("_")))
        Shotval.set(data[1])
        WSval.set(data[2])
        BSval.set(data[3])
        Sval.set(data[4])
        TAval.set(data[5])
        Wval.set(data[6])
        Ival.set(data[7])
        Aval.set(data[8])
        SVAval.set(data[9])
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
        
        UnitvarO.set(" ".join(data[0].split("_")))
        Enemyval.set(data[1])
        WSOval.set(data[2])
        BSOval.set(data[3])
        SOval.set(data[4])
        TAval.set(data[5])
        WOval.set(data[6])
        IOval.set(data[7])
        AOval.set(data[8])
        SVval.set(data[9])
        root.update()



# Method to create probability distribution
def create_distribution(sh_data, at_data, en_data):
    try:
        attacks = int(Shotval.get())*int(Aval.get())
        enemies = int(Enemyval.get())*int(AOval.get())
        if attacks > enemies:
            attacks = enemies
        if attacks < 5:
            attacks = 5
    except ValueError:
        Shotval.set(1)
        attacks = 5

    # Create probability dict
    sh_prob = simulation.create_prob_dict(sh_data, attacks)
    at_prob = simulation.create_prob_dict(at_data, attacks)
    en_prob = simulation.create_prob_dict(en_data, attacks)

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
            
    sh_probs = []
    at_probs = []
    en_probs = []
    sh_total = 0
    at_total = 0
    en_total = 0
    for key in sh_prob:
        sh_prob[key] /= len(sh_data)
        sh_probs.append(sh_prob[key])
    for key in at_prob:
        at_prob[key] /= len(at_data)
        at_probs.append(at_prob[key])
    for key in en_prob:
        en_prob[key] /= len(en_data)
        en_probs.append(en_prob[key])

    sh_probs = sorted(sh_probs)	 	
    sh_largestProb = int(sh_probs.pop()*100)+10
    at_probs = sorted(at_probs)	 	
    at_largestProb = int(at_probs.pop()*100)+10
    en_probs = sorted(en_probs)	 	
    en_largestProb = int(en_probs.pop()*100)+10

    largestProb = max([sh_largestProb, at_largestProb, en_largestProb])

    # Create legend
    graphframe.create_line(430, 20, 460, 20, fill='DarkOliveGreen', width=4)
    graphframe.create_line(430, 32, 460, 32, fill='RoyalBlue2', width=4)
    graphframe.create_line(430, 44, 460, 44, fill='firebrick3', width=4)
    graphframe.create_text(420, 20, text='%s'%("Shooting Phase"), anchor=E)
    graphframe.create_text(420, 32, text='%s'%("Assault (Attacker)"), anchor=E)
    graphframe.create_text(420, 44, text='%s'%("Assault (Enemy)"), anchor=E)
    
    create_marks(attacks, largestProb, sh_prob, 'DarkOliveGreen', 12)
    create_marks(attacks, largestProb, at_prob, 'RoyalBlue2', 6)
    create_marks(attacks, largestProb, en_prob, 'firebrick3', 3)
    
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

def create_marks(attacks, max_prob, probdict, color, width):
    m = width/2+1
    for key in probdict:
        x_pos = 50 + (key * 400/attacks)
        y_pos = 300 - round((probdict[key]*250*100/max_prob))

        if x_pos >= 50:
            graphframe.create_rectangle(x_pos-m, y_pos-m, x_pos+m, y_pos+m, fill=color)
            graphframe.create_line(x_pos, 300, x_pos, y_pos, width=width, fill=color)
            
    
        
def calculate(*args):
    iterations = int(IterSlide.get())
    if iterations == 0:
        iterations = 1
    PBAR['maximum'] = iterations
    
    Shoot_MeanHit    = 0
    Shoot_MeanWound  = 0
    Shoot_MeanKill   = 0
    Attack_MeanHit   = 0
    Attack_MeanWound = 0
    Attack_MeanKill  = 0
    Enemy_MeanHit    = 0
    Enemy_MeanWound  = 0
    Enemy_MeanKill   = 0
    shoot_kill_list  = []
    enemy_kill_list  = []
    attack_kill_list  = []
    loop_count = 0
    
    numAttack = int(Shotval.get())
    numEnemy  = int(Enemyval.get())
    wsa  = int(WS_box.get())
    bsa  = int(BS_box.get())
    sa   = int(S_box.get())
    ta   = int(TA_box.get())
    wa   = int(W_box.get())
    ia   = int(I_box.get())
    aa   = int(A_box.get())
    sva  = int(SVA_box.get())
    
    wso  = int(WSO_box.get())
    bso  = int(BSO_box.get())
    so   = int(SO_box.get())
    to   = int(T_box.get())
    wo   = int(WO_box.get())
    io   = int(IO_box.get())
    ao   = int(AO_box.get())
    svo  = int(SV_box.get())
    
    shots     = numAttack
    A_attacks = numAttack*aa
    O_attacks = numEnemy*ao

    # Retrieve score needed to hit
    if bsa > 5:
        bsa = 5
    scoreToHit = 7-bsa
    
    if wso > wsa:
        Enemy_ToHit  = 3
        Attack_ToHit = 4
        if wso > 2*wsa:
            Attack_ToHit = 5      
    elif wsa > wso:
        Attack_ToHit = 3
        Enemy_ToHit  = 4
        if wsa > 2*wso:
            Enemy_ToHit = 5
    else:
        Attack_ToHit = 4
        Enemy_ToHit  = 4

    # Retrieve score needed to wound
    if sa == to:
        Attack_ToWound = 4
    elif sa < to:
        Attack_ToWound = 4 + (to-sa)
        if Attack_ToWound > 6:
            Attack_ToWound = 7
    elif sa > to:
        Attack_ToWound = 4 - (sa-to)
        if Attack_ToWound < 2:
            Attack_ToWound = 2
    if so == ta:
        Enemy_ToWound = 4
    elif so < ta:
        Enemy_ToWound = 4 + (ta-so)
        if Enemy_ToWound > 6:
            Enemy_ToWound = 7
    elif so > ta:
        Enemy_ToWound = 4 - (so-ta)
        if Enemy_ToWound < 2:
            Enemy_ToWound = 2

    # Handle Instant Kills on double strength
    if sa > 2*to:
        svo = 0
    if so > 2*ta:
        sva = 0

    if (not shots) or (not A_attacks) or (not O_attacks):
        messagebox.showinfo(message='ERROR', detail='Number of Attackers and Enemies cannot be empty or zero!',
                            icon='error', default='ok',parent=root)
        return
        
    while(loop_count < iterations):
        PBAR.step(1.0)
        root.update()

        #Get hit probability
        shoot_hits  = simulation.to_hit(scoreToHit, shots)
        if ia == io:
            attack_hits = simulation.to_hit(Attack_ToHit, A_attacks)
            enemy_hits  = simulation.to_hit(Enemy_ToHit, O_attacks)
        
        # Get wound probability
        shoot_wounds = simulation.to_wound(Attack_ToWound, shoot_hits)
        if ia == io:
            attack_wounds = simulation.to_wound(Attack_ToWound, attack_hits)
            enemy_wounds  = simulation.to_wound(Enemy_ToWound, enemy_hits)
            
        # Get kill probability
        if ia > io:
            attack_hits   = simulation.to_hit(Attack_ToHit, A_attacks)
            attack_wounds = simulation.to_wound(Attack_ToWound, attack_hits)
            attack_kills  = simulation.kills(attack_wounds, svo)
  
            enemy_hits    = simulation.to_hit(Enemy_ToHit, O_attacks - attack_kills)
            enemy_wounds  = simulation.to_wound(Enemy_ToWound, enemy_hits)
            enemy_kills   = simulation.kills(enemy_wounds, sva)

        elif io > ia:
            enemy_hits    = simulation.to_hit(Enemy_ToHit, O_attacks)
            enemy_wounds  = simulation.to_wound(Enemy_ToWound, enemy_hits)
            enemy_kills   = simulation.kills(enemy_wounds, sva)

            attack_hits   = simulation.to_hit(Attack_ToHit, A_attacks - enemy_kills)
            attack_wounds = simulation.to_wound(Attack_ToWound, attack_hits)
            attack_kills  = simulation.kills(attack_wounds, svo)

        else:
            attack_kills = simulation.kills(attack_wounds, svo)
            enemy_kills  = simulation.kills(enemy_wounds, sva)
            
        shoot_kills = simulation.kills(shoot_wounds, svo)
        
        shoot_kill_list.append(shoot_kills)
        attack_kill_list.append(attack_kills)
        enemy_kill_list.append(enemy_kills)
        
        Shoot_MeanHit   += shoot_hits
        Shoot_MeanWound += shoot_wounds
        Shoot_MeanKill  += shoot_kills

        Attack_MeanHit   += attack_hits
        Attack_MeanWound += attack_wounds
        Attack_MeanKill  += attack_kills

        Enemy_MeanHit   += enemy_hits
        Enemy_MeanWound += enemy_wounds
        Enemy_MeanKill  += enemy_kills

        loop_count += 1


    Shoot_MeanHit /= iterations
    Shoot_MeanWound /= iterations
    Shoot_MeanKill /= iterations

    Attack_MeanHit /= iterations
    Attack_MeanWound /= iterations
    Attack_MeanKill /= iterations

    Enemy_MeanHit /= iterations
    Enemy_MeanWound /= iterations
    Enemy_MeanKill /= iterations

    if shoot_kill_list:
        HitVal.set(simulation.round_int(Shoot_MeanHit))
        WoundVal.set(simulation.round_int(Shoot_MeanWound))
        KillVal.set(simulation.round_int(Shoot_MeanKill))

        create_distribution(shoot_kill_list, attack_kill_list, enemy_kill_list)
    
'''
    GUI Setup
'''
root = Tk()

root.title("Stathammer "+str(version))
if os.name == "posix":
    root.wm_iconbitmap('@staticon.xbm')
else:
    root.wm_iconbitmap('staticon.ico')

root.protocol('WM_DELETE_WINDOW', save_init)



#=============#
#   Frames    #  
#=============#
mainframe = GUI.frame_create(root, 0, 0)
statframe = GUI.frame_create(mainframe, 0, 0)
sideframe = GUI.frame_create(mainframe, 0, 1)

atstatframe = GUI.label_frame_create(statframe, 'Attacker', 1, 0)
atsvldframe = GUI.frame_create(atstatframe, 0, 1)
attackframe = GUI.frame_create(atstatframe, 1, 1)
attackstat  = GUI.frame_create(atstatframe, 1, 0)

opstatframe = GUI.label_frame_create(statframe, 'Enemy', 2, 0)
enemyframe  = GUI.frame_create(opstatframe, 1, 1)
opsvldframe = GUI.frame_create(opstatframe, 0, 1)
enemystat   = GUI.frame_create(opstatframe, 1, 0)

probframe = GUI.label_frame_create(sideframe, 'Results', 2, 1)

barframe = GUI.label_frame_create(statframe, 'Simulation Control', 3, 0)

graphframe = GUI.canvas_create(sideframe, 1, 1, [500, 350])


#=============#
#   Entries   #  
#=============#
Unitvar = StringVar()
Unit_name = GUI.input_create(atstatframe, 'entry', Unitvar, 40, [0, 0, (W, E)], [0])
Unitvar.set('=I= TYPE UNIT NAME =I=')

Shotval = StringVar()
Shot_box = GUI.input_create(attackstat, 'entry', Shotval, 4, [3, 0, (W)], [0])
Shotval.set(1)

WSval = StringVar()
WS_box = GUI.input_create(attackstat, 'spinbox', WSval, 2, [3, 1, (W)], [1, 10])

BSval = StringVar()
BS_box = GUI.input_create(attackstat, 'spinbox', BSval, 2, [3, 2, (W)], [1, 10])

Sval = StringVar()
S_box = GUI.input_create(attackstat, 'spinbox', Sval, 2, [3, 3, (W)], [1, 10])

TAval = StringVar()
TA_box = GUI.input_create(attackstat, 'spinbox', TAval, 2, [3, 4, (W)], [1, 10])

Wval = StringVar()
W_box = GUI.input_create(attackstat, 'spinbox', Wval, 2, [3, 5, (W)], [1, 10])

Ival = StringVar()
I_box = GUI.input_create(attackstat, 'spinbox', Ival, 2, [3, 6, (W)], [1, 10])

Aval = StringVar()
A_box = GUI.input_create(attackstat, 'spinbox', Aval, 2, [3, 7, (W)], [1, 10])

SVAval = StringVar()
SVA_box = GUI.input_create(attackstat, 'spinbox', SVAval, 2, [3, 8, (W)], [2, 6])

# Enemy setup
UnitvarO = StringVar()
Unit_nameO = GUI.input_create(opstatframe, 'entry', UnitvarO, 40, [0, 0, (W,E)], [0])
UnitvarO.set('=I= TYPE UNIT NAME =I=')

Enemyval = StringVar()
Enemy_box = GUI.input_create(enemystat, 'entry', Enemyval, 4, [3, 0, (W)], [0])
Enemyval.set(1)

WSOval = StringVar()
WSO_box = GUI.input_create(enemystat, 'spinbox', WSOval, 2, [3, 1, (W)], [1, 10])

BSOval = StringVar()
BSO_box = GUI.input_create(enemystat, 'spinbox', BSOval, 2, [3, 2, (W)], [1, 10])

SOval = StringVar()
SO_box = GUI.input_create(enemystat, 'spinbox', SOval, 2, [3, 3, (W)], [1, 10])

Tval = StringVar()
T_box = GUI.input_create(enemystat, 'spinbox', Tval, 2, [3, 4, (W)], [1, 10])

WOval = StringVar()
WO_box = GUI.input_create(enemystat, 'spinbox', WOval, 2, [3, 5, (W)], [1, 10])

IOval = StringVar()
IO_box = GUI.input_create(enemystat, 'spinbox', IOval, 2, [3, 6, (W)], [1, 10])

AOval = StringVar()
AO_box = GUI.input_create(enemystat, 'spinbox', AOval, 2, [3, 7, (W)], [1, 10])

SVval = StringVar()
SV_box = GUI.input_create(enemystat, 'spinbox', SVval, 2, [3, 8, (W)], [2, 6])

IterVal = StringVar()
IterSlide = GUI.input_create(barframe, 'slider', IterVal, 120, [0, 0, (W, E)], [10.0, 50000.0])
IterSlide.set(2500.0)

#=============#
#   Buttons   #  
#=============#
calc = ttk.Button(probframe, text='Calculate', command=calculate)
calc.grid(column=0, row=0, sticky=(W, E))

saveAttack = ttk.Button(atsvldframe, text = 'Save', command=save_attacker)
saveAttack.grid(column=1, row=0, sticky=(W, E, N, S))

loadAttack = ttk.Button(atsvldframe, text = 'Load', command=load_attacker)
loadAttack.grid(column=0, row=0, sticky=(W, E, N, S))

saveEnemy = ttk.Button(opsvldframe, text = 'Save', command=save_enemy)
saveEnemy.grid(column=1, row=0, sticky=(W, E, N, S))

loadEnemy = ttk.Button(opsvldframe, text = 'Load', command=load_enemy)
loadEnemy.grid(column=0, row=0, sticky=(W, E, N, S))


#=============#
#   Labels    #  
#=============#
SHOT_label = ttk.Label(attackstat, text='#')
SHOT_label.grid(column=0, row=2, sticky=(W, E))

WS_label = ttk.Label(attackstat, text='WS')
WS_label.grid(column=1, row=2, sticky=(W, E))

BS_label = ttk.Label(attackstat, text='BS')
BS_label.grid(column=2, row=2, sticky=(W, E))

S_label = ttk.Label(attackstat, text='S')
S_label.grid(column=3, row=2, sticky=(W, E))

TA_label = ttk.Label(attackstat, text='T')
TA_label.grid(column=4, row=2, sticky=(W, E))

W_label = ttk.Label(attackstat, text='W')
W_label.grid(column=5, row=2, sticky=(W, E))

I_label = ttk.Label(attackstat, text='I')
I_label.grid(column=6, row=2, sticky=(W, E))

A_label = ttk.Label(attackstat, text='A')
A_label.grid(column=7, row=2, sticky=(W, E))

SVA_label = ttk.Label(attackstat, text='SV')
SVA_label.grid(column=8, row=2, sticky=(W, E))

# Enemy labels
ENEMY_label = ttk.Label(enemystat, text="#")
ENEMY_label.grid(column=0, row=2, sticky=(W, E))

WSO_label = ttk.Label(enemystat, text='WS')
WSO_label.grid(column=1, row=2, sticky=(W, E))

BSO_label = ttk.Label(enemystat, text='BS')
BSO_label.grid(column=2, row=2, sticky=(W, E))

SO_label = ttk.Label(enemystat, text='S')
SO_label.grid(column=3, row=2, sticky=(W, E))

T_label = ttk.Label(enemystat, text='T')
T_label.grid(column=4, row=2, sticky=(W, E))

WO_label = ttk.Label(enemystat, text='W')
WO_label.grid(column=5, row=2, sticky=(W, E))

IO_label = ttk.Label(enemystat, text='I')
IO_label.grid(column=6, row=2, sticky=(W, E))

AO_label = ttk.Label(enemystat, text='A')
AO_label.grid(column=7, row=2, sticky=(W, E))

SV_label = ttk.Label(enemystat, text='SV')
SV_label.grid(column=8, row=2, sticky=(W, E))


# Probability Labels
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

root.bind('<Return>', calculate)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


try:
    load_init()
except:
    pass

root.mainloop()
