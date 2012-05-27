#!/usr/bin/python

version = 0.09

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import random
import os
import GUI
import simulation
import WCreate

# Class for units.  Allows for creation of multiple
# attackers and enemies with a minimal increase in code
class Unit(object):
    def __init__(self):
        self.name    = StringVar()
        self.attacks = StringVar()
        self.WS      = StringVar()
        self.BS      = StringVar()
        self.S       = StringVar()
        self.T       = StringVar()
        self.W       = StringVar()
        self.I       = StringVar()
        self.A       = StringVar()
        self.SV      = StringVar()
        self.INV     = StringVar()
        
    def set_values(self, unitStats):
        self.name.set(unitStats[0])
        self.attacks.set(unitStats[1])
        self.WS.set(unitStats[2])
        self.BS.set(unitStats[3])
        self.S.set(unitStats[4])
        self.T.set(unitStats[5])
        self.W.set(unitStats[6])
        self.I.set(unitStats[7])
        self.A.set(unitStats[8])
        self.SV.set(unitStats[9])
        self.INV.set("0")

    # Method returns all values for a unit
    def get_values(self):
        return [self.name.get(), self.attacks.get(), self.WS.get(),
                self.BS.get(), self.S.get(), self.T.get(), self.W.get(),
                self.I.get(), self.A.get(), self.SV.get()]

    # Method returns all values and converts number strings into ints
    def get_int_values(self):
        return [self.name.get(), int(self.attacks.get()), int(self.WS.get()),
                int(self.BS.get()), int(self.S.get()), int(self.T.get()), int(self.W.get()),
                int(self.I.get()), int(self.A.get()), int(self.SV.get())]

            

# Method used to return window to previous state (on last close)
def load_init():
    f = open('.init', 'r')
    data = f.readlines()
    f.close()

    #Attackers
    data[0] = data[0].split(" ")
    data[1] = data[1].split(" ")
    data[2] = data[2].split(" ")

    #Enemies
    data[3] = data[3].split(" ")
    data[4] = data[4].split(" ")
    data[5] = data[5].split(" ")

    #Set variables
    Unitvar.set(" ".join(data[0][0].split("_")))
    UnitvarO.set(" ".join(data[3][0].split("_")))
    
    attacker_1.set_values([data[1][0], data[1][1], data[1][2], data[1][3],
                           data[1][4], data[1][5], data[1][6], data[1][7],
                           data[1][8], data[1][9]])
    
    attacker_2.set_values([data[2][0], data[2][1], data[2][2], data[2][3],
                           data[2][4], data[2][5], data[2][6], data[2][7],
                           data[2][8], data[2][9]])

    
    enemy_1.set_values([data[4][0], data[4][1], data[4][2], data[4][3],
                        data[4][4], data[4][5], data[4][6], data[4][7],
                        data[4][8], data[4][9]])
    
    enemy_2.set_values([data[5][0], data[5][1], data[5][2], data[5][3],
                        data[5][4], data[5][5], data[5][6], data[5][7],
                        data[5][8], data[5][9]])
   
# Saves window state for re-initialization
def save_init():

    ua   = "_".join(Unitvar.get().split(" "))
    ue   = "_".join(UnitvarO.get().split(" "))
    
    attacker = (str(ua)+" \n"+
                " ".join(attacker_1.get_values())+" \n"+
                " ".join(attacker_2.get_values()))
    
    enemy = (str(ue)+" \n"+
             " ".join(enemy_1.get_values())+" \n"+
             " ".join(enemy_2.get_values()))
             
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
        ua   = "_".join(Unitvar.get().split(" "))
        attacker = (str(ua)+" \n"+
                    " ".join(attacker_1.get_values())+" \n"+
                    " ".join(attacker_2.get_values()))
                    
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
        ue   = "_".join(UnitvarO.get().split(" "))
        enemy = (str(ue)+" \n"+
                 " ".join(enemy_1.get_values())+" \n"+
                 " ".join(enemy_2.get_values()))
                 
        save = open(saveFile, 'w')
        save.write(enemy)
        save.close()

# Load attacker profile
def load_attacker():
    types = [('Attacker Profile', '.at'),('All Files', '.*')]
    loadFile = filedialog.askopenfilename(initialdir='profiles',
                                            filetypes=types)
    if loadFile[-3:] != '.at':
        messagebox.showerror(message='ERROR', detail='Invalid File Type!', icon='error', default='ok',parent=root)
    else:
        load = open(loadFile, 'r')
        data = load.readlines()
        load.close()
        data[0] = data[0].split()
        data[1] = data[1].split()
        data[2] = data[2].split()
        
        Unitvar.set(" ".join(data[0][0].split("_")))
        attacker_1.set_values([data[1][0], data[1][1], data[1][2], data[1][3],
                               data[1][4], data[1][5], data[1][6], data[1][7],
                               data[1][8], data[1][9]])
        attacker_2.set_values([data[2][0], data[2][1], data[2][2], data[2][3],
                               data[2][4], data[2][5], data[2][6], data[2][7],
                               data[2][8], data[2][9]])
        
        root.update()

def load_enemy():
    types = [('Enemy Profile', '.op'),('All Files', '.*')]
    loadFile = filedialog.askopenfilename(initialdir='profiles',
                                            filetypes=types)
    if loadFile[-3:] != '.op':
        messagebox.showerror(message='ERROR', detail='Invalid File Type!', icon='error', default='ok',parent=root)
    else:
        load = open(loadFile, 'r')
        data = load.readlines()
        load.close()
        data[0] = data[0].split()
        data[1] = data[1].split()
        data[2] = data[2].split()
        
        UnitvarO.set(" ".join(data[0][0].split("_")))
        enemy_1.set_values([data[1][0], data[1][1], data[1][2], data[1][3],
                            data[1][4], data[1][5], data[1][6], data[1][7],
                            data[1][8], data[1][9]])
        enemy_2.set_values([data[2][0], data[2][1], data[2][2], data[2][3],
                            data[2][4], data[2][5], data[2][6], data[2][7],
                            data[2][8], data[2][9]])
        
        root.update()

# Disable/Enable extra attacker        
def addAttacker(*args):
    numberToAdd = int(ExAtVal.get())
    
    if numberToAdd == 0:
        nameA1_box.config(state=DISABLED)
        numa1_box.config(state=DISABLED)
        wsa1_box.config(state=DISABLED)
        bsa1_box.config(state=DISABLED)
        sa1_box.config(state=DISABLED)
        ta1_box.config(state=DISABLED)
        wa1_box.config(state=DISABLED)
        ia1_box.config(state=DISABLED)
        aa1_box.config(state=DISABLED)
        sva1_box.config(state=DISABLED)
        inv1_box.config(state=DISABLED)

    elif numberToAdd == 1:
        nameA1_box.config(state=NORMAL)
        numa1_box.config(state=NORMAL)
        wsa1_box.config(state=NORMAL)
        bsa1_box.config(state=NORMAL)
        sa1_box.config(state=NORMAL)
        ta1_box.config(state=NORMAL)
        wa1_box.config(state=NORMAL)
        ia1_box.config(state=NORMAL)
        aa1_box.config(state=NORMAL)
        sva1_box.config(state=NORMAL)
        inv1_box.config(state=NORMAL)

# Disable/Enable extra enemy 
def addEnemy(*args):
    numberToAdd = int(ExOpVal.get())
    
    if numberToAdd == 0:
        nameO1_box.config(state=DISABLED)
        numo1_box.config(state=DISABLED)
        wso1_box.config(state=DISABLED)
        bso1_box.config(state=DISABLED)
        so1_box.config(state=DISABLED)
        to1_box.config(state=DISABLED)
        wo1_box.config(state=DISABLED)
        io1_box.config(state=DISABLED)
        ao1_box.config(state=DISABLED)
        svo1_box.config(state=DISABLED)
        invo1_box.config(state=DISABLED)

    elif numberToAdd == 1:
        nameO1_box.config(state=NORMAL)
        numo1_box.config(state=NORMAL)
        wso1_box.config(state=NORMAL)
        bso1_box.config(state=NORMAL)
        so1_box.config(state=NORMAL)
        to1_box.config(state=NORMAL)
        wo1_box.config(state=NORMAL)
        io1_box.config(state=NORMAL)
        ao1_box.config(state=NORMAL)
        svo1_box.config(state=NORMAL)
        invo1_box.config(state=NORMAL)

# Refreshes weapon list
def refresh_weapons(*args):
    gunList = ['No Weapon Selected']
    for key in weaponCreator.guns:
        gunList.append(key)

    ccList = ['Default']
    for key in weaponCreator.cc:
        ccList.append(key)

    # Update Guns
    l = [at1Gun, at2Gun, at3Gun, at4Gun, at5Gun, atex1Gun, atex2Gun]
    for box in l:
        box['values'] = tuple(gunList)
        box.set('No Weapon Selected')

    # Update CC Weapons
    l = [at1CC, at2CC, at3CC, at4CC, at5CC, atex1CC, atex2CC,
         op1CC, op2CC, op3CC, op4CC, op5CC, opex1CC, opex2CC]
    for box in l:
        box['values'] = tuple(ccList)
        box.set('Default')
    
        
# Method to create probability distribution
def create_distribution(sh_data, at_data, en_data):
    try:
        attacks  = int(attacker_1.attacks.get())*int(attacker_1.A.get())
        attack_w = int(attacker_1.attacks.get())*int(attacker_1.W.get())
        enemies  = int(enemy_1.attacks.get())*int(enemy_1.A.get())
        enemy_w  = int(enemy_1.attacks.get())*int(enemy_1.W.get())
        attacks  = min([attacks, enemies, attack_w, enemy_w])
            
        if attacks < 5:
            attacks = 5
    except ValueError:
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
    iterations = int(IterVar.get())
    if iterations == 0:
        iterations = 1
    PBAR['maximum'] = iterations

    # Initialize Data Structures
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

    # Get Parameters
    [name, numAttack, wsa, bsa, sa, ta, wa, ia, aa, sva] = attacker_1.get_int_values()
    [name, numEnemy,  wso, bso, so, to, wo, io, ao, svo] = enemy_1.get_int_values()
    
    shots     = numAttack
    A_attacks = numAttack*aa
    O_attacks = numEnemy*ao
    A_wounds  = numAttack*wa
    O_wounds  = numEnemy*wo

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
        messagebox.showerror(message='ERROR', detail='Number of Attackers and Enemies cannot be empty or zero!',
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
    root.wm_iconbitmap('@staticon.xbm') # For non-windows systems (works on linux, not sure about OSX)
else:
    root.wm_iconbitmap('staticon.ico')  # For windows

root.protocol('WM_DELETE_WINDOW', save_init)
#root.minsize(480, 640)
#root.maxsize(1024, 768)

#================#
# Weapon Creator #
#================#
weaponCreator = WCreate.WWindow(root)


#=============#
#   Frames    #  
#=============#

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.pack()

topframe = ttk.Notebook(mainframe)
topframe.grid(column=0, row=0)
statframe = ttk.Frame(topframe)
sideframe = ttk.Frame(topframe)
topframe.add(statframe, text='Unit Stats')
topframe.add(sideframe, text='Results')


graphpage   = GUI.label_frame_create(sideframe, 'Distribution', 0, 0)
probframe   = GUI.label_frame_create(sideframe, 'Statistics', 0, 1)
graphpage.grid(padx=7)
probframe.grid(padx=7)

# TABLE
tableframe  = GUI.frame_create(probframe, 99, 99)
statTable = GUI.Table(tableframe, 3, 5)
statTable.create(0, 0)

for row in range(0, statTable.rows):
    statTable.change_width(row, 0, 15)


atstatframe = GUI.label_frame_create(statframe, 'Attacker', 0, 0)
atstatframe.grid(padx=7)
atnameframe = GUI.frame_create(atstatframe, 0, 0)
atsvldframe = GUI.frame_create(atnameframe, 0, 1)
attackstat  = GUI.frame_create(atstatframe, 1, 0)

opstatframe = GUI.label_frame_create(statframe, 'Enemy', 0, 1)
opstatframe.grid(padx=7)
opnameframe  = GUI.frame_create(opstatframe, 0, 0)
opsvldframe = GUI.frame_create(opnameframe, 0, 1)
enemystat   = GUI.frame_create(opstatframe, 1, 0)

atweaponframe = ttk.Notebook(atstatframe)
atweaponframe.grid(column=0, row=3)
opweaponframe = ttk.Notebook(opstatframe)
opweaponframe.grid(column=0, row=3)
primat = ttk.Frame(atweaponframe)
primop = ttk.Frame(opweaponframe)
extrat = ttk.Frame(atweaponframe)
extrop = ttk.Frame(opweaponframe)
atweaponframe.add(primat, text='Primary Unit')
opweaponframe.add(primop, text='Primary Unit')
atweaponframe.add(extrat, text='Secondary Unit')
opweaponframe.add(extrop, text='Secondary Unit')

primatsh = GUI.label_frame_create(primat, 'Shooting', 0, 0)
primatcc = GUI.label_frame_create(primat, 'Assault',  0, 1)
extratsh = GUI.label_frame_create(extrat, 'Shooting', 0, 0)
extratcc = GUI.label_frame_create(extrat, 'Assault',  0, 1)
primopcc = GUI.label_frame_create(primop, 'Assault',  0, 0)
extropcc = GUI.label_frame_create(extrop, 'Assault',  0, 0)

barframe = GUI.frame_create(mainframe, 1, 0)

graphframe = GUI.canvas_create(graphpage, 0, 0, [500, 350])


attackex_one = ttk.Frame(atstatframe, padding="3 3 12 12")
attackex_one.grid(column=0, row=2, sticky=(N, E, W, S))
attackex_one.columnconfigure(0, weight=1)
attackex_one.rowconfigure(2, weight=1)

enemyex_one = ttk.Frame(opstatframe, padding="3 3 12 12")
enemyex_one.grid(column=0, row=2, sticky=(N, E, W, S))
enemyex_one.columnconfigure(0, weight=1)
enemyex_one.rowconfigure(2, weight=1)


#=============#
#     Menu    #  
#=============#
root.option_add('*tearOff', FALSE)
menubar = Menu(root)

#Top Menus
filemenu = Menu(menubar, tearoff=0)
optmenu  = Menu(menubar, tearoff=0)
helpmenu = Menu(menubar, tearoff=0)

#Sub Menus
itermenu = Menu(optmenu, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Options", menu=optmenu)
menubar.add_cascade(label="Help", menu=helpmenu)

# File ->
filemenu.add_command(label="New Weapon", command=weaponCreator.show)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=save_init)

# Options ->
optmenu.add_command(label="Refresh Weapon List", command=refresh_weapons)

IterVar = StringVar()
optmenu.add_cascade(label="Iterations", menu=itermenu)
itermenu.add_radiobutton(label="100", variable=IterVar, value="100")
itermenu.add_radiobutton(label="1000", variable=IterVar, value="1000")
itermenu.add_radiobutton(label="2500", variable=IterVar, value="2500")
itermenu.add_radiobutton(label="5000", variable=IterVar, value="5000")
itermenu.add_radiobutton(label="10000", variable=IterVar, value="10000")
IterVar.set("2500")
root.config(menu=menubar)



#=============#
#   Entries   #  
#=============#

# Attackers
Unitvar = StringVar()
Unit_name = GUI.input_create(atnameframe, 'entry', Unitvar, 40, [0, 0, (W, E)], [0])
Unitvar.set('=I= TYPE UNIT NAME =I=')

attacker_1  = Unit()
UnitA_name  = GUI.input_create(attackstat, 'entry', attacker_1.name,    15, [3, 0, (W, E)], [0])
Shot_box    = GUI.input_create(attackstat, 'entry', attacker_1.attacks, 4,  [3, 1, (W)], [0])
WS_box      = GUI.input_create(attackstat, 'spinbox', attacker_1.WS,    2,  [3, 2, (W)], [1, 10])
BS_box      = GUI.input_create(attackstat, 'spinbox', attacker_1.BS,    2,  [3, 3, (W)], [1, 10])
S_box       = GUI.input_create(attackstat, 'spinbox', attacker_1.S,     2,  [3, 4, (W)], [1, 10])
TA_box      = GUI.input_create(attackstat, 'spinbox', attacker_1.T,     2,  [3, 5, (W)], [1, 10])
W_box       = GUI.input_create(attackstat, 'spinbox', attacker_1.W,     2,  [3, 6, (W)], [1, 10])
I_box       = GUI.input_create(attackstat, 'spinbox', attacker_1.I,     2,  [3, 7, (W)], [1, 10])
A_box       = GUI.input_create(attackstat, 'spinbox', attacker_1.A,     2,  [3, 8, (W)], [1, 10])
SVA_box     = GUI.input_create(attackstat, 'spinbox', attacker_1.SV,    2,  [3, 9, (W)], [2,  6])
INV_box     = GUI.input_create(attackstat, 'spinbox', attacker_1.INV,   2,  [3, 10,(W)], [0,  6])
attacker_1.name.set('UNIT NAME')
attacker_1.attacks.set(1)

attacker_2 = Unit()
nameA1_box = GUI.input_create(attackex_one, 'entry', attacker_2.name,   15, [0, 0, (W,E)], [0])
numa1_box  = GUI.input_create(attackex_one, 'entry', attacker_2.attacks, 4, [0, 1, (W)], [0])
wsa1_box   = GUI.input_create(attackex_one, 'spinbox', attacker_2.WS,    2, [0, 2, (W)], [1, 10])
bsa1_box   = GUI.input_create(attackex_one, 'spinbox', attacker_2.BS,    2, [0, 3, (W)], [1, 10])
sa1_box    = GUI.input_create(attackex_one, 'spinbox', attacker_2.S,     2, [0, 4, (W)], [1, 10])
ta1_box    = GUI.input_create(attackex_one, 'spinbox', attacker_2.T,     2, [0, 5, (W)], [1, 10])
wa1_box    = GUI.input_create(attackex_one, 'spinbox', attacker_2.W,     2, [0, 6, (W)], [1, 10])
ia1_box    = GUI.input_create(attackex_one, 'spinbox', attacker_2.I,     2, [0, 7, (W)], [1, 10])
aa1_box    = GUI.input_create(attackex_one, 'spinbox', attacker_2.A,     2, [0, 8, (W)], [1, 10])
sva1_box   = GUI.input_create(attackex_one, 'spinbox', attacker_2.SV,    2, [0, 9, (W)], [2,  6])
inv1_box   = GUI.input_create(attackex_one, 'spinbox', attacker_2.INV,   2, [0, 10,(W)], [0,  6])
attacker_2.name.set('UNIT NAME')
attacker_2.attacks.set(1)
      
# Enemies
UnitvarO = StringVar()
Unit_nameO = GUI.input_create(opnameframe, 'entry', UnitvarO, 40, [0, 0, (W,E)], [0])
UnitvarO.set('=I= TYPE UNIT NAME =I=')

enemy_1     = Unit()
UnitO_name  = GUI.input_create(enemystat, 'entry', enemy_1.name,   15, [3, 0, (W, E)], [0])
Enemy_box   = GUI.input_create(enemystat, 'entry', enemy_1.attacks, 4, [3, 1, (W)], [0])
WSO_box     = GUI.input_create(enemystat, 'spinbox', enemy_1.WS,    2, [3, 2, (W)], [1, 10])
BSO_box     = GUI.input_create(enemystat, 'spinbox', enemy_1.BS,    2, [3, 3, (W)], [1, 10])
SO_box      = GUI.input_create(enemystat, 'spinbox', enemy_1.S,     2, [3, 4, (W)], [1, 10])
T_box       = GUI.input_create(enemystat, 'spinbox', enemy_1.T,     2, [3, 5, (W)], [1, 10])
WO_box      = GUI.input_create(enemystat, 'spinbox', enemy_1.W,     2, [3, 6, (W)], [1, 10])
IO_box      = GUI.input_create(enemystat, 'spinbox', enemy_1.I,     2, [3, 7, (W)], [1, 10])
AO_box      = GUI.input_create(enemystat, 'spinbox', enemy_1.A,     2, [3, 8, (W)], [1, 10])
SV_box      = GUI.input_create(enemystat, 'spinbox', enemy_1.SV,    2, [3, 9, (W)], [2,  6])
INVO_box    = GUI.input_create(enemystat, 'spinbox', enemy_1.INV,   2, [3, 10,(W)], [0,  6])
enemy_1.name.set('UNIT NAME')
enemy_1.attacks.set(1)

enemy_2     = Unit()
nameO1_box  = GUI.input_create(enemyex_one, 'entry', enemy_2.name,   15, [0, 0, (W,E)], [0])
numo1_box   = GUI.input_create(enemyex_one, 'entry', enemy_2.attacks, 4, [0, 1, (W)], [0])
wso1_box    = GUI.input_create(enemyex_one, 'spinbox', enemy_2.WS,    2, [0, 2, (W)], [1, 10])
bso1_box    = GUI.input_create(enemyex_one, 'spinbox', enemy_2.BS,    2, [0, 3, (W)], [1, 10])
so1_box     = GUI.input_create(enemyex_one, 'spinbox', enemy_2.S,     2, [0, 4, (W)], [1, 10])
to1_box     = GUI.input_create(enemyex_one, 'spinbox', enemy_2.T,     2, [0, 5, (W)], [1, 10])
wo1_box     = GUI.input_create(enemyex_one, 'spinbox', enemy_2.W,     2, [0, 6, (W)], [1, 10])
io1_box     = GUI.input_create(enemyex_one, 'spinbox', enemy_2.I,     2, [0, 7, (W)], [1, 10])
ao1_box     = GUI.input_create(enemyex_one, 'spinbox', enemy_2.A,     2, [0, 8, (W)], [1, 10])
svo1_box    = GUI.input_create(enemyex_one, 'spinbox', enemy_2.SV,    2, [0, 9, (W)], [2,  6])
invo1_box    = GUI.input_create(enemyex_one, 'spinbox', enemy_2.INV,   2, [0, 10,(W)], [0,  6])
enemy_2.name.set('UNIT NAME')
enemy_2.attacks.set(1)

# Extra unit check buttons
ExAtVal = StringVar()
ExAt_box = ttk.Checkbutton(attackstat, text='Extra Unit', variable=ExAtVal, command=addAttacker, onvalue='1', offvalue='0')
ExAt_box.grid(column=0, row=1, sticky=(W, E))
ExAtVal.set('0')

ExOpVal = StringVar()
ExOp_box = ttk.Checkbutton(enemystat, text='Extra Unit', variable=ExOpVal, command=addEnemy, onvalue='1', offvalue='0')
ExOp_box.grid(column=0, row=1, sticky=(W, E))
ExOpVal.set('0')

addAttacker()
addEnemy()

# Weapon entrys
primAtWep1 = StringVar()
primAtWep2 = StringVar()
primAtWep3 = StringVar()
primAtWep4 = StringVar()
primAtWep5 = StringVar()
pAtWep1Box = GUI.input_create(primatsh, 'entry', primAtWep1, 3, [1, 0, ()], [0])
pAtWep2Box = GUI.input_create(primatsh, 'entry', primAtWep2, 3, [2, 0, ()], [0])
pAtWep3Box = GUI.input_create(primatsh, 'entry', primAtWep3, 3, [3, 0, ()], [0])
pAtWep4Box = GUI.input_create(primatsh, 'entry', primAtWep4, 3, [4, 0, ()], [0])
pAtWep5Box = GUI.input_create(primatsh, 'entry', primAtWep5, 3, [5, 0, ()], [0])

primAtCC1 = StringVar()
primAtCC2 = StringVar()
primAtCC3 = StringVar()
primAtCC4 = StringVar()
primAtCC5 = StringVar()
pAtCC1Box = GUI.input_create(primatcc, 'entry', primAtCC1, 3, [1, 0, ()], [0])
pAtCC2Box = GUI.input_create(primatcc, 'entry', primAtCC2, 3, [2, 0, ()], [0])
pAtCC3Box = GUI.input_create(primatcc, 'entry', primAtCC3, 3, [3, 0, ()], [0])
pAtCC4Box = GUI.input_create(primatcc, 'entry', primAtCC4, 3, [4, 0, ()], [0])
pAtCC5Box = GUI.input_create(primatcc, 'entry', primAtCC5, 3, [5, 0, ()], [0])

extrAtWep1 = StringVar()
extrAtWep2 = StringVar()
eAtWep1Box = GUI.input_create(extratsh, 'entry', extrAtWep1, 3, [1, 0, ()], [0])
eAtWep2Box = GUI.input_create(extratsh, 'entry', extrAtWep2, 3, [2, 0, ()], [0])

extrAtCC1 = StringVar()
extrAtCC2 = StringVar()
eAtCC1Box = GUI.input_create(extratcc, 'entry', extrAtCC1, 3, [1, 0, ()], [0])
eAtCC2Box = GUI.input_create(extratcc, 'entry', extrAtCC2, 3, [2, 0, ()], [0])

primOpCC1 = StringVar()
primOpCC2 = StringVar()
primOpCC3 = StringVar()
primOpCC4 = StringVar()
primOpCC5 = StringVar()
pOpCC1Box = GUI.input_create(primopcc, 'entry', primOpCC1, 3, [1, 0, ()], [0])
pOpCC2Box = GUI.input_create(primopcc, 'entry', primOpCC2, 3, [2, 0, ()], [0])
pOpCC3Box = GUI.input_create(primopcc, 'entry', primOpCC3, 3, [3, 0, ()], [0])
pOpCC4Box = GUI.input_create(primopcc, 'entry', primOpCC4, 3, [4, 0, ()], [0])
pOpCC5Box = GUI.input_create(primopcc, 'entry', primOpCC5, 3, [5, 0, ()], [0])

extrOpCC1 = StringVar()
extrOpCC2 = StringVar()
eOpCC1Box = GUI.input_create(extropcc, 'entry', extrOpCC1, 3, [1, 0, ()], [0])
eOpCC2Box = GUI.input_create(extropcc, 'entry', extrOpCC2, 3, [2, 0, ()], [0])

#=============#
#   Buttons   #  
#=============#
calc = ttk.Button(barframe, text='Calculate', command=calculate, width=20)
calc.grid(column=0, row=0, ipady=5, pady=10)

saveAttack = ttk.Button(atsvldframe, text = 'Save', command=save_attacker, width=10)
saveAttack.grid(column=1, row=0, sticky=(W))

loadAttack = ttk.Button(atsvldframe, text = 'Load', command=load_attacker, width=10)
loadAttack.grid(column=0, row=0, sticky=(W))

saveEnemy = ttk.Button(opsvldframe, text = 'Save', command=save_enemy, width=10)
saveEnemy.grid(column=1, row=0, sticky=(W))

loadEnemy = ttk.Button(opsvldframe, text = 'Load', command=load_enemy, width=10)
loadEnemy.grid(column=0, row=0, sticky=(W))



#=============#
#  Comboboxes #
#=============#
gunList = ['No Weapon Selected']
for key in weaponCreator.guns:
    gunList.append(key)

ccList = ['Default']
for key in weaponCreator.cc:
    ccList.append(key)

at1GunVar = StringVar()
at2GunVar = StringVar()
at3GunVar = StringVar()
at4GunVar = StringVar()
at5GunVar = StringVar()
varlist = [at1GunVar, at2GunVar,at3GunVar, at4GunVar, at5GunVar]
l = [at1Gun, at2Gun, at3Gun, at4Gun, at5Gun] = GUI.weapon_boxes(primatsh, varlist,1, 1, 20)
for box in l:
    box['values'] = tuple(gunList)
    box.set('No Weapon Selected')

at1CCVar  = StringVar()
at2CCVar  = StringVar()
at3CCVar  = StringVar()
at4CCVar  = StringVar()
at5CCVar  = StringVar()
varlist = [at1CCVar, at2CCVar,at3CCVar, at4CCVar, at5CCVar]
l = [at1CC, at2CC, at3CC, at4CC, at5CC] = GUI.weapon_boxes(primatcc, varlist,1, 1, 20)
for box in l:
    box['values'] = tuple(ccList)
    box.set('Default')


atex1GunVar = StringVar()
atex2GunVar = StringVar()
varlist = [atex1GunVar, atex2GunVar]
l =[atex1Gun, atex2Gun] = GUI.weapon_boxes(extratsh, varlist, 1, 1, 20)
for box in l:
    box['values'] = tuple(gunList)
    box.set('No Weapon Selected')

atex1CCVar  = StringVar()
atex2CCVar  = StringVar()
varlist = [atex1CCVar, atex2CCVar]
l = [atex1CC, atex2CC] = GUI.weapon_boxes(extratcc, varlist, 1, 1, 20)
for box in l:
    box['values'] = tuple(ccList)
    box.set('Default')

op1CCVar  = StringVar()
op2CCVar  = StringVar()
op3CCVar  = StringVar()
op4CCVar  = StringVar()
op5CCVar  = StringVar()
varlist = [op1CCVar, op2CCVar,op3CCVar, op4CCVar, op5CCVar]
l = [op1CC, op2CC, op3CC, op4CC, op5CC] = GUI.weapon_boxes(primopcc, varlist,1, 1, 20)
for box in l:
    box['values'] = tuple(ccList)
    box.set('Default')

opex1CCVar  = StringVar()
opex2CCVar  = StringVar()
varlist = [opex1CCVar, opex2CCVar]
l = [opex1CC, opex2CC] = GUI.weapon_boxes(extropcc, varlist, 1, 1, 20)
for box in l:
    box['values'] = tuple(ccList)
    box.set('Default')

    
#=============#
#   Labels    #  
#=============#

# Weapon Labels
ttk.Label(primatsh,  text='Weapon', justify='center', font='TkTextFont 8 bold').grid(column=1, row=0, pady=2)
ttk.Label(primatcc,  text='Weapon', justify='center', font='TkTextFont 8 bold').grid(column=1, row=0, pady=2)
ttk.Label(extratsh,  text='Weapon', justify='center', font='TkTextFont 8 bold').grid(column=1, row=0, pady=2)
ttk.Label(extratcc,  text='Weapon', justify='center', font='TkTextFont 8 bold').grid(column=1, row=0, pady=2)
ttk.Label(primopcc,  text='Weapon', justify='center', font='TkTextFont 8 bold').grid(column=1, row=0)
ttk.Label(extropcc,  text='Weapon', justify='center', font='TkTextFont 8 bold').grid(column=1, row=0)
ttk.Label(primatsh,  text='Number', justify='center', font='TkTextFont 8 bold').grid(column=0, row=0)
ttk.Label(extratsh,  text='Number', justify='center', font='TkTextFont 8 bold').grid(column=0, row=0)
ttk.Label(primatcc,  text='Number', justify='center', font='TkTextFont 8 bold').grid(column=0, row=0)
ttk.Label(extratcc,  text='Number', justify='center', font='TkTextFont 8 bold').grid(column=0, row=0)
ttk.Label(primopcc,  text='Number', justify='center', font='TkTextFont 8 bold').grid(column=0, row=0)
ttk.Label(extropcc,  text='Number', justify='center', font='TkTextFont 8 bold').grid(column=0, row=0)


# Attacker labels
SHOT_label = ttk.Label(attackstat, text='#')
SHOT_label.grid(column=1, row=2, sticky=(W, E))

WS_label = ttk.Label(attackstat, text='WS')
WS_label.grid(column=2, row=2, sticky=(W, E))

BS_label = ttk.Label(attackstat, text='BS')
BS_label.grid(column=3, row=2, sticky=(W, E))

S_label = ttk.Label(attackstat, text='S')
S_label.grid(column=4, row=2, sticky=(W, E))

TA_label = ttk.Label(attackstat, text='T')
TA_label.grid(column=5, row=2, sticky=(W, E))

W_label = ttk.Label(attackstat, text='W')
W_label.grid(column=6, row=2, sticky=(W, E))

I_label = ttk.Label(attackstat, text='I')
I_label.grid(column=7, row=2, sticky=(W, E))

A_label = ttk.Label(attackstat, text='A')
A_label.grid(column=8, row=2, sticky=(W, E))

SVA_label = ttk.Label(attackstat, text='SV')
SVA_label.grid(column=9, row=2, sticky=(W, E))

INV_label = ttk.Label(attackstat, text='Inv')
INV_label.grid(column=10, row=2, sticky=(W, E))

# Enemy labels
ENEMY_label = ttk.Label(enemystat, text="#")
ENEMY_label.grid(column=1, row=2, sticky=(W, E))

WSO_label = ttk.Label(enemystat, text='WS')
WSO_label.grid(column=2, row=2, sticky=(W, E))

BSO_label = ttk.Label(enemystat, text='BS')
BSO_label.grid(column=3, row=2, sticky=(W, E))

SO_label = ttk.Label(enemystat, text='S')
SO_label.grid(column=4, row=2, sticky=(W, E))

T_label = ttk.Label(enemystat, text='T')
T_label.grid(column=5, row=2, sticky=(W, E))

WO_label = ttk.Label(enemystat, text='W')
WO_label.grid(column=6, row=2, sticky=(W, E))

IO_label = ttk.Label(enemystat, text='I')
IO_label.grid(column=7, row=2, sticky=(W, E))

AO_label = ttk.Label(enemystat, text='A')
AO_label.grid(column=8, row=2, sticky=(W, E))

SV_label = ttk.Label(enemystat, text='SV')
SV_label.grid(column=9, row=2, sticky=(W, E))

INVO_label = ttk.Label(enemystat, text='Inv')
INVO_label.grid(column=10, row=2, sticky=(W, E))

# Probability Labels
HIT_label = ttk.Label(probframe, text='Average Hits')
HIT_label.grid(column=0, row=0, sticky=(N, W), ipadx=10)

WOUND_label = ttk.Label(probframe, text='Average Wounded')
WOUND_label.grid(column=0, row=1, sticky=(N, W), ipadx=10)

KILL_label = ttk.Label(probframe, text='Average Killed')
KILL_label.grid(column=0, row=2, sticky=(N, W), ipadx=10)

HitVal = StringVar()
HITNUM_label = ttk.Label(probframe, textvariable=HitVal)
HITNUM_label.grid(column=1, row=0, sticky=(N, E))
HitVal.set('0')

WoundVal = StringVar()
WOUNDNUM_label = ttk.Label(probframe, textvariable=WoundVal)
WOUNDNUM_label.grid(column=1, row=1, sticky=(N, E))
WoundVal.set('0')

KillVal = StringVar()
KILLNUM_label = ttk.Label(probframe, textvariable=KillVal)
KILLNUM_label.grid(column=1, row=2, sticky=(N, E))
KillVal.set('0')

# Progress Bar
PBAR = ttk.Progressbar(barframe, orient=HORIZONTAL, length=120, mode='determinate')
PBAR.grid(column=1, row=0, sticky=(S, E))
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


    
