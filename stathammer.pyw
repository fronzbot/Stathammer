#!/usr/bin/python
'''
Stathammer (c) 2012
Author : Kevin Fronczak
Email  : kfronczak@gmail.com
Source : http://github.com/fronzbot/Stathammer

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

version = '0.1.3'

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import webbrowser
import random
import os
import GUI
import simulation
import WCreate

# Check for <ccl.wf> ands create if it does not exist
try:
    f = open('ccl.wf', 'r')
    f.close()
except IOError:
    f = open('ccl.wf', 'w')
    f.write('Default 1 None \n')
    f.close() 


def bug(*args):
    webbrowser.open('http://github.com/fronzbot/Stathammer/issues')


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
        self.INV.set(unitStats[10])

    # Method returns all values for a unit
    def get_values(self):
        name = "_".join(self.name.get().split(" "))
        return [name, self.attacks.get(), self.WS.get(),
                self.BS.get(), self.S.get(), self.T.get(), self.W.get(),
                self.I.get(), self.A.get(), self.SV.get(), self.INV.get()]

    # Method returns all values and converts number strings into ints
    def get_int_values(self):
        name = "_".join(self.name.get().split(" "))
        return [name, int(self.attacks.get()), int(self.WS.get()),
                int(self.BS.get()), int(self.S.get()), int(self.T.get()), int(self.W.get()),
                int(self.I.get()), int(self.A.get()), int(self.SV.get()), int(self.INV.get())]

            
def get_about(*args):
    app.deiconify()

def open_source(*args):
    webbrowser.open('http://github.com/fronzbot/Stathammer')
    
# Method used to return window to previous state (on last close)
def load_init():
    f = open('.init', 'r')
    data = f.readlines()
    f.close()

    #Attackers
    data[0]  = data[0].split(" ")   # Attacker name
    data[1]  = data[1].split(" ")   # Attacker params
    data[2]  = data[2].split(" ")   # Extra Attacker params

    #Enemies
    data[3]  = data[3].split(" ")   # Enemy name
    data[4]  = data[4].split(" ")   # Enemy params
    data[5]  = data[5].split(" ")   # Extra Enemy params

    #Weapons
    data[6]  = data[6].split(" ")   # Attacker Guns
    data[7]  = data[7].split(" ")   # Extra Attacker Guns
    data[8]  = data[8].split(" ")   # Attacker CC
    data[9]  = data[9].split(" ")   # Extra Attacker CC
    data[10] = data[10].split(" ")  # Enemy CC
    data[11] = data[11].split(" ")  # Extra Enemy CC

    #Set variables
    Unitvar.set(" ".join(data[0][0].split("_")))
    UnitvarO.set(" ".join(data[3][0].split("_")))
    namea1 = " ".join(data[1][0].split("_"))
    namea2 = " ".join(data[2][0].split("_"))
    nameo1 = " ".join(data[3][0].split("_"))
    nameo2 = " ".join(data[4][0].split("_"))
    attacker_1.set_values([namea1, data[1][1], data[1][2], data[1][3],
                           data[1][4], data[1][5], data[1][6], data[1][7],
                           data[1][8], data[1][9], data[1][10]])
    
    attacker_2.set_values([namea2, data[2][1], data[2][2], data[2][3],
                           data[2][4], data[2][5], data[2][6], data[2][7],
                           data[2][8], data[2][9], data[2][10]])

    
    enemy_1.set_values([nameo1, data[4][1], data[4][2], data[4][3],
                        data[4][4], data[4][5], data[4][6], data[4][7],
                        data[4][8], data[4][9], data[4][10]])
    
    enemy_2.set_values([nameo2, data[5][1], data[5][2], data[5][3],
                        data[5][4], data[5][5], data[5][6], data[5][7],
                        data[5][8], data[5][9], data[5][10]])

    i = 0
    vals = [primAtWep1, primAtWep2, primAtWep3, primAtWep4, primAtWep5]
    weps = [at1Gun, at2Gun, at3Gun, at4Gun, at5Gun]
    for count, name in simulation.pairwise(data[6]):
        if name == "\n":
            name = "No Weapon Selected"
        vals[i].set(count)
        weps[i].set(name)
        i += 1

    i = 0
    vals = [extrAtWep1, extrAtWep2]
    weps = [atex1Gun, atex2Gun]
    for count, name in simulation.pairwise(data[7]):
        if name == "\n":
            name = "No Weapon Selected"
        vals[i].set(count)
        weps[i].set(name)
        i += 1

    i = 0
    vals = [primAtCC1, primAtCC2, primAtCC3, primAtCC4, primAtCC5]
    weps = [at1CC, at2CC, at3CC, at4CC, at5CC]
    for count, name in simulation.pairwise(data[8]):
        if name == "\n":
            name = "Default"
        vals[i].set(count)
        weps[i].set(name)
        i += 1

    i = 0
    vals = [extrAtCC1, extrAtCC2]
    weps = [atex1CC, atex2CC]
    for count, name in simulation.pairwise(data[9]):
        if name == "\n":
            name = "Default"
        vals[i].set(count)
        weps[i].set(name)
        i += 1

    i = 0
    vals = [primOpCC1, primOpCC2, primOpCC3, primOpCC4, primOpCC5]
    weps = [op1CC, op2CC, op3CC, op4CC, op5CC]
    for count, name in simulation.pairwise(data[10]):
        if name == "\n":
            name = "Default"
        vals[i].set(count)
        weps[i].set(name)
        i += 1

    i = 0
    vals = [extrOpCC1, extrOpCC2]
    weps = [opex1CC, opex2CC]
    for count, name in simulation.pairwise(data[11]):
        if name == "\n":
            name = "Default"
        vals[i].set(count)
        weps[i].set(name)
        i += 1
   
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

    attackWeapons = ""
    weapons = [[primAtWep1, primAtWep2, primAtWep3, primAtWep4, primAtWep5],
               [at1Gun, at2Gun, at3Gun, at4Gun, at5Gun],
               [extrAtWep1, extrAtWep2],
               [atex1Gun, atex2Gun],
               [primAtCC1, primAtCC2, primAtCC3, primAtCC4, primAtCC5],
               [at1CC, at2CC, at3CC, at4CC, at5CC],
               [extrAtCC1, extrAtCC2],
               [atex1CC, atex2CC],
               [primOpCC1, primOpCC2, primOpCC3, primOpCC4, primOpCC5],
               [op1CC, op2CC, op3CC, op4CC, op5CC],
               [extrOpCC1, extrOpCC2],
               [opex1CC, opex2CC]]

    i = 0
    while (i < 11):
        for j in range(0, len(weapons[i])):
            if weapons[i][j].get() != "":
                string = weapons[i][j].get()+" "+weapons[i+1][j].get()+" "
                attackWeapons += string
            else:
                break
        attackWeapons += " \n"
        i += 2
             
    f = open('.init', 'w')
    f.write(attacker+" \n"+enemy+" \n"+attackWeapons)
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

        attackWeapons = ""
        weapons = [[primAtWep1, primAtWep2, primAtWep3, primAtWep4, primAtWep5],
                   [at1Gun, at2Gun, at3Gun, at4Gun, at5Gun],
                   [extrAtWep1, extrAtWep2],
                   [atex1Gun, atex2Gun],
                   [primAtCC1, primAtCC2, primAtCC3, primAtCC4, primAtCC5],
                   [at1CC, at2CC, at3CC, at4CC, at5CC],
                   [extrAtCC1, extrAtCC2],
                   [atex1CC, atex2CC]]

        i = 0
        while (i < 7):
            for j in range(0, len(weapons[i])):
                if weapons[i][j].get() != "":
                    string = weapons[i][j].get()+" "+weapons[i+1][j].get()+" "
                    attackWeapons += string
                else:
                    break
            
            attackWeapons += "\n"
            i += 2
            
        save = open(saveFile, 'w')
        save.write(attacker+" \n"+attackWeapons)
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

        attackWeapons = ""
        weapons = [[primOpCC1, primOpCC2, primOpCC3, primOpCC4, primOpCC5],
                   [op1CC, op2CC, op3CC, op4CC, op5CC],
                   [extrOpCC1, extrOpCC2],
                   [opex1CC, opex2CC]]

        i = 0
        while (i < 3):
            for j in range(0, len(weapons[i])):
                if weapons[i][j].get() != "":
                    string = weapons[i][j].get()+" "+weapons[i+1][j].get()+" "
                    attackWeapons += string
                else:
                    break
            attackWeapons += "\n"
            i += 2
            
        save = open(saveFile, 'w')
        save.write(enemy+" \n"+attackWeapons)
        save.close()

# Load attacker profile
def load_attacker():
    types = [('Attacker Profile', '.at'),('All Files', '.*')]
    loadFile = filedialog.askopenfilename(initialdir='profiles',
                                            filetypes=types)
    if loadFile[-3:] != '.at' and loadFile:
        messagebox.showerror(message='ERROR', detail='Invalid File Type!', icon='error', default='ok',parent=root)
    else:
        load = open(loadFile, 'r')
        data = load.readlines()
        load.close()
        data[0] = data[0].split()
        data[1] = data[1].split()
        data[2] = data[2].split()
        data[3] = data[3].split(" ")   # Attacker Guns
        data[4] = data[4].split(" ")   # Extra Attacker Guns
        data[5] = data[5].split(" ")   # Attacker CC
        data[6] = data[6].split(" ")   # Extra Attacker CC
        
        Unitvar.set(" ".join(data[0][0].split("_")))
        attacker_1.set_values([data[1][0], data[1][1], data[1][2], data[1][3],
                               data[1][4], data[1][5], data[1][6], data[1][7],
                               data[1][8], data[1][9], data[1][10]])
        attacker_2.set_values([data[2][0], data[2][1], data[2][2], data[2][3],
                               data[2][4], data[2][5], data[2][6], data[2][7],
                               data[2][8], data[2][9], data[2][10]])

        i = 0
        vals = [primAtWep1, primAtWep2, primAtWep3, primAtWep4, primAtWep5]
        weps = [at1Gun, at2Gun, at3Gun, at4Gun, at5Gun]
        for count, name in simulation.pairwise(data[3]):
            vals[i].set(count)
            weps[i].set(name)
            i += 1
        for j in range(i, len(vals)):
            vals[i].set("")
            weps[i].set("No Weapon Selected")
    
        i = 0
        vals = [extrAtWep1, extrAtWep2]
        weps = [atex1Gun, atex2Gun]
        for count, name in simulation.pairwise(data[4]):
            vals[i].set(count)
            weps[i].set(name)
            i += 1
        for j in range(i, len(vals)):
            vals[i].set("")
            weps[i].set("No Weapon Selected")
        
        i = 0
        vals = [primAtCC1, primAtCC2, primAtCC3, primAtCC4, primAtCC5]
        weps = [at1CC, at2CC, at3CC, at4CC, at5CC]
        for count, name in simulation.pairwise(data[5]):
            vals[i].set(count)
            weps[i].set(name)
            i += 1
        for j in range(i, len(vals)):
            vals[i].set("")
            weps[i].set("Default")
            
        i = 0
        vals = [extrAtCC1, extrAtCC2]
        weps = [atex1CC, atex2CC]
        for count, name in simulation.pairwise(data[6]):
            vals[i].set(count)
            weps[i].set(name)
            i += 1
        for j in range(i, len(vals)):
            vals[i].set("")
            weps[i].set("Default")
            
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
        data[3] = data[3].split(" ")  # Enemy CC
        data[4] = data[4].split(" ")  # Extra Enemy CC
        
        UnitvarO.set(" ".join(data[0][0].split("_")))
        enemy_1.set_values([data[1][0], data[1][1], data[1][2], data[1][3],
                            data[1][4], data[1][5], data[1][6], data[1][7],
                            data[1][8], data[1][9], data[1][10]])
        enemy_2.set_values([data[2][0], data[2][1], data[2][2], data[2][3],
                            data[2][4], data[2][5], data[2][6], data[2][7],
                            data[2][8], data[2][9], data[1][10]])
        i = 0
        vals = [primOpCC1, primOpCC2, primOpCC3, primOpCC4, primOpCC5]
        weps = [op1CC, op2CC, op3CC, op4CC, op5CC]
        for count, name in simulation.pairwise(data[3]):
            vals[i].set(count)
            weps[i].set(name)
            i += 1
        for j in range(i, len(vals)):
            vals[i].set("")
            weps[i].set("Default")
            
        i = 0
        vals = [extrOpCC1, extrOpCC2]
        weps = [opex1CC, opex2CC]
        for count, name in simulation.pairwise(data[4]):
            vals[i].set(count)
            weps[i].set(name)
            i += 1
        for j in range(i, len(vals)):
            vals[i].set("")
            weps[i].set("Default")
            
        root.update()


def export_csv(*args):
    types = [('CSV (Comma Delimited)', '.csv'),('All Files', '.*')]
    saveFile = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=types)
    if saveFile != '':
        data = ["Kills, Shooting, Attacker Assault, Enemy Assault, "]

        total = max(len(simulation.shooting_prob), len(simulation.attacker_prob), len(simulation.enemy_prob))
        for kills in range(0, total+1):
            data.append(str(kills)+", ")
            index = kills+1
            try:
                prob = simulation.shooting_prob[kills]
                data[index] = data[index] + str(prob)+", "
            except KeyError:
                data[index] = data[index] + "0.00, "
                
            try:
                prob = simulation.attacker_prob[kills]
                data[index] = data[index] + str(prob)+", "
            except KeyError:
                data[index] = data[index] + "0.00, "
            
            try:
                prob = simulation.enemy_prob[kills]
                data[index] = data[index] + str(prob)
            except KeyError:
                data[index] = data[index] + "0.00"
        try:
            if os.path.exists(saveFile):
                os.remove(saveFile)
            save = open(saveFile, 'w')
            for line in data:
                save.write(line+",\n")
            save.close()
        except IOError as e:
            messagebox.showerror(message='ERROR', detail=e,
                                 icon='error', default='ok',parent=root)


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
        box.set(box.get())

    # Update CC Weapons
    l = [at1CC, at2CC, at3CC, at4CC, at5CC, atex1CC, atex2CC,
         op1CC, op2CC, op3CC, op4CC, op5CC, opex1CC, opex2CC]
    for box in l:
        box['values'] = tuple(ccList)
        box.set(box.get())
    
    weaponCreator.app.withdraw()

    
# Method to create probability distribution
def create_distribution(sh_data, at_data, en_data):
    try:
        attacks  = int(attacker_1.attacks.get())*int(attacker_1.A.get())+int(attacker_2.attacks.get())*int(attacker_2.A.get())
        attack_w = int(attacker_1.attacks.get())*int(attacker_1.W.get())+int(attacker_2.attacks.get())*int(attacker_2.W.get())
        enemies  = int(enemy_1.attacks.get())*int(enemy_1.A.get())+int(enemy_2.attacks.get())*int(enemy_2.A.get())
        enemy_w  = int(enemy_1.attacks.get())*int(enemy_1.W.get())+int(enemy_2.attacks.get())*int(enemy_2.W.get())
        attacks  = max([attacks, enemies, attack_w, enemy_w])
            
        if attacks < 5:
            attacks = 5
    except ValueError:
        attacks = 5

    # Create probability dict
    sh_prob = simulation.create_prob_dict(sh_data, attacks)
    at_prob = simulation.create_prob_dict(at_data, attacks)
    en_prob = simulation.create_prob_dict(en_data, attacks)

    attacks = max(len(sh_prob), len(at_prob), len(en_prob)) + 1
    
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
    simulation.shooting_prob = sh_prob
    simulation.attacker_prob = at_prob
    simulation.enemy_prob    = en_prob
    sh_probs = sorted(sh_probs)	 	
    sh_largestProb = int(sh_probs.pop()*100)+10
    at_probs = sorted(at_probs)	 	
    at_largestProb = int(at_probs.pop()*100)+10
    en_probs = sorted(en_probs)	 	
    en_largestProb = int(en_probs.pop()*100)+10

    largestProb = max([sh_largestProb, at_largestProb, en_largestProb])

    # Create legend
    graphframe.create_line(430, 20, 460, 20, fill='DeepSkyBlue4', width=4)
    graphframe.create_line(430, 32, 460, 32, fill='LightSkyBlue3', width=4)
    graphframe.create_line(430, 44, 460, 44, fill='orange2', width=4)
    graphframe.create_text(420, 20, text='%s'%("Shooting Phase"), anchor=E)
    graphframe.create_text(420, 32, text='%s'%("Assault (Attacker)"), anchor=E)
    graphframe.create_text(420, 44, text='%s'%("Assault (Enemy)"), anchor=E)
    
    create_marks(attacks, largestProb, sh_prob, 'DeepSkyBlue4', 18)
    create_marks(attacks, largestProb, at_prob, 'LightSkyBlue3', 10)
    create_marks(attacks, largestProb, en_prob, 'orange2', 3)
    
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

    # Axis labels
    graphframe.create_text(250, 340, text='%s'%("Number of Kills"), anchor=S)
    root.update()
    
graphLocs = {}
graphProb = {}
def create_marks(attacks, max_prob, probdict, color, width):
    m = width/2+2
    ticks = 0
    for key in probdict:
        x_pos = 50 + (key * 400/attacks)
        y_pos = 300 - round((probdict[key]*250*100/max_prob))
        if x_pos not in graphLocs:
            graphLocs[x_pos] = [(y_pos, width)]
        else:
            graphLocs[x_pos].append((y_pos, width))
        graphProb[y_pos] = probdict[key]
        if x_pos >= 50:
            graphframe.create_line(x_pos, 300, x_pos, y_pos, width=width, fill=color)
            graphframe.create_oval(x_pos-m, y_pos-m, x_pos+m, y_pos+m, fill=color, width=2, outline=color)
            

            
    
def popup_prob(event):
    graphcontext.delete(0)
    mouse_x = graphframe.canvasx(event.x)
    mouse_y = graphframe.canvasy(event.y)
    popup_x = event.x+root.winfo_x()+graphframe.winfo_x()+topframe.winfo_x()+graphpage.winfo_x()+sideframe.winfo_x()+10
    popup_y = event.y+root.winfo_y()+graphframe.winfo_y()+topframe.winfo_y()+graphpage.winfo_y()+sideframe.winfo_y()+25
    for x in graphLocs:
        if mouse_x <= x+8 and mouse_x >= x-8:
            for y, tolerance in sorted(graphLocs[x], reverse=True):
                if mouse_y <= y+tolerance/2 and mouse_y >= y-tolerance/2:
                    graphcontext.insert(0, 'command', label=str(int(graphProb[y]*100*1000)/1000) + "%")
                    graphcontext.post(int(popup_x), int(popup_y))
                    break
    #print(str(graphframe.canvasx(event.x))+", "+str(graphframe.canvasy(event.y)))
    
def calculate(*args):
    iterations = int(IterVar.get())
    if iterations == 0:
        iterations = 1
    PBAR['maximum'] = iterations

    hasExtraAttacker = bool(int(ExAtVal.get()))
    hasExtraEnemy = bool(int(ExOpVal.get()))

    
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

    shoot_hit_list    = []
    enemy_hit_list    = []
    attack_hit_list   = []
    shoot_wound_list  = []
    enemy_wound_list  = []
    attack_wound_list = []
    shoot_kill_list   = []
    enemy_kill_list   = []
    attack_kill_list  = []
    loop_count = 0

    attackerGunAttributes = {}
    exAttackerGunAttributes = {}
    
    # Get Parameters
    [name, numAttack, wsa, bsa, sa, ta, wa, ia, aa, sva, inva] = attacker_1.get_int_values()
    [name, numEnemy,  wso, bso, so, to, wo, io, ao, svo, invo] = enemy_1.get_int_values()
    if hasExtraAttacker:
        [name2, numAttack2, wsa2, bsa2, sa2, ta2, wa2, ia2, aa2, sva2, inva2] = attacker_2.get_int_values()
    if hasExtraEnemy:
        [name2, numEnemy2,  wso2, bso2, so2, to2, wo2, io2, ao2, svo2, invo2] = enemy_2.get_int_values()

    # Get weapon usage
    ##################
    # Guns for primary attacker
    unitGunCount = [primAtWep1.get(), primAtWep2.get(), primAtWep3.get(), primAtWep4.get(), primAtWep5.get()]
    unitGunNames = [at1GunVar.get(), at2GunVar.get(), at3GunVar.get(), at4GunVar.get(), at5GunVar.get()] 
    attackerGuns = simulation.sort_weapons(unitGunNames, unitGunCount)
        
    # CC Weapons for primary attacker
    unitCCCount = [primAtCC1.get(), primAtCC2.get(), primAtCC3.get(), primAtCC4.get(), primAtCC5.get()]
    unitCCNames = [at1CCVar.get(), at2CCVar.get(), at3CCVar.get(), at4CCVar.get(), at5CCVar.get()]
    attackerCC  = simulation.sort_weapons(unitCCNames, unitCCCount)

    if hasExtraAttacker:
        # Guns for secondary attacker
        extraGunCount = [extrAtWep1.get(), extrAtWep2.get()]
        extraGunNames = [atex1GunVar.get(), atex2GunVar.get()] 
        extraAttackerGuns = simulation.sort_weapons(extraGunNames, extraGunCount)

        # CC Weapons for secondary attacker
        extraCCCount = [extrAtCC1.get(), extrAtCC2.get()]
        extraCCNames = [atex1CCVar.get(), atex2CCVar.get()]
        extraAttackerCC  = simulation.sort_weapons(extraCCNames, extraCCCount)


    # CC Weapons for primary enemy
    opCCCount = [primOpCC1.get(), primOpCC2.get(), primOpCC3.get(), primOpCC4.get(), primOpCC5.get()]
    opCCNames = [op1CCVar.get(), op2CCVar.get(), op3CCVar.get(), op4CCVar.get(), op5CCVar.get()]
    enemyCC  = simulation.sort_weapons(opCCNames, opCCCount)

    if hasExtraEnemy:
        # CC Weapons for secondary enemy
        extraOpCCCount = [extrOpCC1.get(), extrOpCC2.get()]
        extraOpCCNames = [opex1CCVar.get(), opex2CCVar.get()]
        extraEnemyCC  = simulation.sort_weapons(extraOpCCNames, extraOpCCCount)

    # Get total number of attacks for weapons and modify strength for cc weapons
    attackerCCStrength = {}
    for gun in attackerGuns:
        attackerGuns[gun] *= int(weaponCreator.guns[gun][0])
        attackerGunAttributes[gun] = weaponCreator.guns[gun][3:]
    for cc in attackerCC:
        try:
            attackerCC[cc] *= int(weaponCreator.cc[cc][0])
            attackerCCStrength[cc] = simulation.get_cc_strength(weaponCreator.cc[cc][2:], sa)
        except KeyError:
            attackerCCStrength[cc] = sa
            
        attackerCC[cc] *= aa

    if hasExtraAttacker:
        extraAttackerCCStrength = {}
        for gun in extraAttackerGuns:
            extraAttackerGuns[gun] *= int(weaponCreator.guns[gun][0])
            exAttackerGunAttributes[gun] = weaponCreator.guns[gun][3:]
        for cc in extraAttackerCC:
            try:
                extraAttackerCC[cc] *= int(weaponCreator.cc[cc][0])
                extraAttackerCCStrength[cc] = simulation.get_cc_strength(weaponCreator.cc[cc][2:], sa2)
            except KeyError:
                extraAttackerCCStrength[cc] = sa2
                
            extraAttackerCC[cc] *= aa2

    # Enemy
    enemyCCStrength = {}
    for cc in enemyCC:
        try:
            enemyCC[cc] *= int(weaponCreator.cc[cc][0])
            enemyCCStrength[cc] = simulation.get_cc_strength(weaponCreator.cc[cc][2:], so)
        except KeyError:
            enemyCCStrength[cc] = so
            
        enemyCC[cc] *= ao

    if hasExtraEnemy:
        extraEnemyCCStrength = {}
        for cc in extraEnemyCC:
            try:
                extraEnemyCC[cc] *= int(weaponCreator.cc[cc][0])
                extraEnemyCCStrength[cc] = simulation.get_cc_strength(weaponCreator.cc[cc][2:], so2)
            except KeyError:
                extraEnemyCCStrength[cc] = so2
                
            extraEnemyCC[cc] *= ao2
        
    PrimAt_wounds  = numAttack*wa
    PrimOp_wounds  = numEnemy*wo
    if hasExtraAttacker:
        ExtrAt_wounds  = numAttack2*wa2
    if hasExtraEnemy:
        ExtrOp_wounds  = numEnemy2*wo2
    
    # Retrieve score needed to hit for Primary Units
    if bsa > 5:
        bsa = 5
        for gun in attackerGuns:
            attackerGunAttributes[gun].append('Re-roll Hits')
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

    # Retrieve score needed to hit for Secondary Units
    if hasExtraAttacker:
        if bsa2 > 5:
            bsa2 = 5
            for gun in extraAttackerGuns:
                exAttackerGunAttributes[gun].append('Re-roll Hits')
        scoreToHit2 = 7-bsa2
    
        if wso > wsa2:
            Attack2_ToHit = 4
            if wso > 2*wsa2:
                Attack2_ToHit = 5      
        elif wsa2 > wso:
            Attack2_ToHit = 3
        else:
            Attack2_ToHit = 4

    if hasExtraEnemy:
        if wsa > wso2:
            Enemy2_ToHit = 4
            if wsa > 2*wso2:
                Enemy2_ToHit = 5      
        elif wso2 > wsa:
            Enemy2_ToHit = 3
        else:
            Enemy2_ToHit = 4


    # Retrieve score needed to wound for shooting and Instant-Kill check
    Gun_ToWound      = {}
    Gun_InstantKill  = {}
    for weapon in attackerGuns:
        Gun_ToWound[weapon] = simulation.get_scoreToWound(int(weaponCreator.guns[weapon][1]),
                                                          attackerGunAttributes[gun], to)

        Gun_InstantKill[weapon] = simulation.check_instant_kill(int(weaponCreator.guns[weapon][1]),
                                                     to, attackerGunAttributes[gun],
                                                     int(weaponCreator.guns[weapon][2]))

    if hasExtraAttacker:
        Gun2_ToWound     = {}
        Gun2_InstantKill = {}
        for weapon in extraAttackerGuns:
            Gun2_ToWound[weapon] = simulation.get_scoreToWound(int(weaponCreator.guns[weapon][1]),
                                                              exAttackerGunAttributes[gun], to)
    
            Gun2_InstantKill[weapon] = simulation.check_instant_kill(int(weaponCreator.guns[weapon][1]),
                                                         to, exAttackerGunAttributes[gun],
                                                         int(weaponCreator.guns[weapon][2]))
        
    # Retrieve score needed to wound for cc and Instant-Kill check
    CC_ToWound      = {}
    CC_InstantKill  = {}
    for weapon in attackerCC:
        try:
            CC_ToWound[weapon] = simulation.get_scoreToWound(attackerCCStrength[weapon],
                                                              weaponCreator.cc[weapon][1:], to)
            CC_InstantKill[weapon] = simulation.check_instant_kill(attackerCCStrength[weapon],
                                                         to, weaponCreator.cc[weapon][1:], 0)
        except KeyError:
            CC_ToWound[weapon] = simulation.get_scoreToWound(attackerCCStrength[weapon], [], to)
            CC_InstantKill[weapon] = simulation.check_instant_kill(attackerCCStrength[weapon], to, [], 0)

    if hasExtraAttacker:
        CC2_ToWound     = {}
        CC2_InstantKill = {}        
        for weapon in extraAttackerCC:
            try:
                CC2_ToWound[weapon] = simulation.get_scoreToWound(extraAttackerCCStrength[weapon],
                                                                  weaponCreator.cc[weapon][1:], to)
                CC2_InstantKill[weapon] = simulation.check_instant_kill(extraAttackerCCStrength[weapon],
                                                             to, weaponCreator.cc[weapon][1:], 0)
            except KeyError:
                CC2_ToWound[weapon] = simulation.get_scoreToWound(extraAttackerCCStrength[weapon], [], to)
                CC2_InstantKill[weapon] = simulation.check_instant_kill(extraAttackerCCStrength[weapon], to, [], 0)
    
    # Retrieve enemy score needed to wound for cc and Instant-Kill check
    enemyCC_ToWound       = {}
    enemyCC_InstantKill   = {}
    for weapon in enemyCC:
        try:
            enemyCC_ToWound[weapon] = simulation.get_scoreToWound(enemyCCStrength[weapon],
                                                                  weaponCreator.cc[weapon][1:], to)
            enemyCC_InstantKill[weapon] = simulation.check_instant_kill(enemyCCStrength[weapon],
                                                                        ta, weaponCreator.cc[weapon][1:], 0)
        except KeyError:
            enemyCC_ToWound[weapon] = simulation.get_scoreToWound(enemyCCStrength[weapon], [], ta)
            enemyCC_InstantKill[weapon] = simulation.check_instant_kill(enemyCCStrength[weapon], ta, [], 0)

    if hasExtraEnemy:
        enemy2CC_ToWound      = {}
        enemy2CC_InstantKill  = {}
        for weapon in extraEnemyCC:
            try:
                enemy2CC_ToWound[weapon] = simulation.get_scoreToWound(extraEnemyCCStrength[weapon],
                                                                      weaponCreator.cc[weapon][1:], to)
                enemy2CC_InstantKill[weapon] = simulation.check_instant_kill(extraEnemyCCStrength[weapon],
                                                                            ta, weaponCreator.cc[weapon][1:], 0)
            except KeyError:
                enemy2CC_ToWound[weapon] = simulation.get_scoreToWound(extraEnemyCCStrength[weapon], [], ta)
                enemy2CC_InstantKill[weapon] = simulation.check_instant_kill(extraEnemyCCStrength[weapon], ta, [], 0)

    while(loop_count < iterations):
        PBAR.step(1.0)
        root.update()

        shoot_hits   = {}
        shoot_wounds = {}
        shoot_kills  = {}
        currentShot_hits   = []
        currentShot_wounds = []
        currentShot_kills  = []
        attackerCC_hits     = []
        attackerCC_wounds   = []
        attackerCC_kills    = []
        
        attacker2CC_hits     = []
        attacker2CC_wounds   = []
        attacker2CC_kills    = []
        
        enemyCC_hits     = []
        enemyCC_wounds   = []
        enemyCC_kills    = []
        
        enemy2CC_hits     = []
        enemy2CC_wounds   = []
        enemy2CC_kills    = []
        
        
        for weapon in attackerGuns:
            # Get hit probability
            shoot_hits[weapon]   = simulation.to_hit(scoreToHit, attackerGuns[weapon],
                                                     attackerGunAttributes[gun])
            # Get Wound Probability
            [shoot_wounds[weapon], rending] = simulation.to_wound(Gun_ToWound[weapon],
                                                                  shoot_hits[weapon],
                                                                  attackerGunAttributes[gun])
            
            if Gun_InstantKill[weapon]:
                shoot_kills[weapon] = simulation.kills(shoot_wounds[weapon], 0, invo)
            else:
                shoot_kills[weapon] = simulation.kills(shoot_wounds[weapon], svo, invo)
                
            shoot_kills[weapon] += rending
            currentShot_hits.append(shoot_hits[weapon])
            currentShot_wounds.append(shoot_wounds[weapon])
            currentShot_kills.append(shoot_kills[weapon])

        # Check how many kills there are.  If there are <number of enemy> kills then allocate to secondary.
        allocateToSecondary = False
        if hasExtraAttacker:
            if currentShot_kills[-1] == numEnemy:
                allocateToSecondary = True
                for weapon in extraAttackerGuns:
                    Gun2_ToWound[weapon] = simulation.get_scoreToWound(int(weaponCreator.guns[weapon][1]),
                                                                           exAttackerGunAttributes[gun], to2)

                    Gun2_InstantKill[weapon] = simulation.check_instant_kill(int(weaponCreator.guns[weapon][1]),
                                                                             to2, exAttackerGunAttributes[gun],
                                                                             int(weaponCreator.guns[weapon][2]))
                    
            for weapon in extraAttackerGuns:
                # Get hit probability
                shoot_hits[weapon]   = simulation.to_hit(scoreToHit2, extraAttackerGuns[weapon],
                                                         exAttackerGunAttributes[gun])
                # Get Wound Probability
                [shoot_wounds[weapon], rending] = simulation.to_wound(Gun2_ToWound[weapon],
                                                                      shoot_hits[weapon],
                                                                      exAttackerGunAttributes[gun])
                
                if Gun2_InstantKill[weapon]:
                    if allocateToSecondary:
                        shoot_kills[weapon] = simulation.kills(shoot_wounds[weapon], 0, invo2)
                    else:
                        shoot_kills[weapon] = simulation.kills(shoot_wounds[weapon], 0, invo)
                else:
                    if allocateToSecondary:
                        shoot_kills[weapon] = simulation.kills(shoot_wounds[weapon], svo2, invo2)
                    else:
                        shoot_kills[weapon] = simulation.kills(shoot_wounds[weapon], svo, invo)
                    
                shoot_kills[weapon] += rending
                currentShot_hits.append(shoot_hits[weapon])
                currentShot_wounds.append(shoot_wounds[weapon])
                currentShot_kills.append(shoot_kills[weapon])

        # Initiative checking (not perfect, but it's sufficient)

        # If there are extra units for both attackers and enemys
        if hasExtraAttacker and hasExtraEnemy:
            # Primary vs Primary
            if ia > io:
                [attackerCC_hits, attackerCC_wounds, attackerCC_kills] = simulation.calculate_assault(weaponCreator, attackerCC,
                                                                                                      Attack_ToHit, CC_ToWound,
                                                                                                      invo, svo, CC_InstantKill, 0)
                kills = 0
                for kill in attackerCC_kills:
                    kills += kill
                [enemyCC_hits, enemyCC_wounds, enemyCC_kills] = simulation.calculate_assault(weaponCreator, enemyCC,
                                                                                             Enemy_ToHit, enemyCC_ToWound,
                                                                                             inva, sva, enemyCC_InstantKill, kills)
            elif ia < io:
                [enemyCC_hits, enemyCC_wounds, enemyCC_kills] = simulation.calculate_assault(weaponCreator, enemyCC,
                                                                                             Enemy_ToHit, enemyCC_ToWound,
                                                                                             inva, sva, enemyCC_InstantKill, 0)
                kills = 0
                for kill in enemyCC_kills:
                    kills += kill                
                [attackerCC_hits, attackerCC_wounds, attackerCC_kills] = simulation.calculate_assault(weaponCreator, attackerCC,
                                                                                                      Attack_ToHit, CC_ToWound,
                                                                                                      invo, svo, CC_InstantKill, kills)
            else:
                [attackerCC_hits, attackerCC_wounds, attackerCC_kills] = simulation.calculate_assault(weaponCreator, attackerCC,
                                                                                                      Attack_ToHit, CC_ToWound,
                                                                                                      invo, svo, CC_InstantKill, 0)
                
                [enemyCC_hits, enemyCC_wounds, enemyCC_kills] = simulation.calculate_assault(weaponCreator, enemyCC,
                                                                                             Enemy_ToHit, enemyCC_ToWound,
                                                                                             inva, sva, enemyCC_InstantKill, 0)
            # Secondary vs Secondary
            if ia2 > io2:
                [attacker2CC_hits, attacker2CC_wounds, attacker2CC_kills] = simulation.calculate_assault(weaponCreator, extraAttackerCC,
                                                                                                         Attack2_ToHit, CC2_ToWound,
                                                                                                         invo2, svo2, CC2_InstantKill, 0)
                kills = 0
                for kill in attacker2CC_kills:
                    kills += kill
                [enemy2CC_hits, enemy2CC_wounds, enemy2CC_kills] = simulation.calculate_assault(weaponCreator, extraEnemyCC,
                                                                                                Enemy2_ToHit, enemy2CC_ToWound,
                                                                                                inva2, sva2, enemy2CC_InstantKill, kills)
            elif ia2 < io2:
                [enemy2CC_hits, enemy2CC_wounds, enemy2CC_kills] = simulation.calculate_assault(weaponCreator, extraEnemyCC,
                                                                                                Enemy2_ToHit, enemy2CC_ToWound,
                                                                                                inva2, sva2, enemy2CC_InstantKill, 0)
                kills = 0
                for kill in enemy2CC_kills:
                    kills += kill
                [attacker2CC_hits, attacker2CC_wounds, attacker2CC_kills] = simulation.calculate_assault(weaponCreator, extraAttackerCC,
                                                                                                         Attack2_ToHit, CC2_ToWound,
                                                                                                         invo2, svo2, CC2_InstantKill, kills)
            else:
                [attacker2CC_hits, attacker2CC_wounds, attacker2CC_kills] = simulation.calculate_assault(weaponCreator, extraAttackerCC,
                                                                                                         Attack2_ToHit, CC2_ToWound,
                                                                                                         invo2, svo2, CC2_InstantKill, 0)
                
                [enemy2CC_hits, enemy2CC_wounds, enemy2CC_kills] = simulation.calculate_assault(weaponCreator, extraEnemyCC,
                                                                                                Enemy2_ToHit, enemy2CC_ToWound,
                                                                                                inva2, sva2, enemy2CC_InstantKill, 0)
        # If only extra Attacker (assumes all enemy hits land on primary unit)
        elif hasExtraAttacker:
            if ia > io:
                [attackerCC_hits, attackerCC_wounds, attackerCC_kills] = simulation.calculate_assault(weaponCreator, attackerCC,
                                                                                                      Attack_ToHit, CC_ToWound,
                                                                                                      invo, svo, CC_InstantKill, 0)
                
                [attacker2CC_hits, attacker2CC_wounds, attacker2CC_kills] = simulation.calculate_assault(weaponCreator, extraAttackerCC,
                                                                                                         Attack2_ToHit, CC2_ToWound,
                                                                                                         invo, svo, CC2_InstantKill, 0)
                kills = 0
                for kill, kill2 in zip(attackerCC_kills, attacker2CC_kills):
                    kills += kill
                    kills += kill2

                [enemyCC_hits, enemyCC_wounds, enemyCC_kills] = simulation.calculate_assault(weaponCreator, enemyCC,
                                                                                             Enemy_ToHit, enemyCC_ToWound,
                                                                                             inva, sva, enemyCC_InstantKill, kills)
            elif ia < io:
                [attacker2CC_hits, attacker2CC_wounds, attacker2CC_kills] = simulation.calculate_assault(weaponCreator, extraAttackerCC,
                                                                                                         Attack2_ToHit, CC2_ToWound,
                                                                                                         invo, svo, CC2_InstantKill, 0)
                kills = 0
                for kill in attacker2CC_kills:
                    kills += kill
                [enemyCC_hits, enemyCC_wounds, enemyCC_kills] = simulation.calculate_assault(weaponCreator, enemyCC,
                                                                                             Enemy_ToHit, enemyCC_ToWound,
                                                                                             inva, sva, enemyCC_InstantKill, kills)
                kills = 0
                for kill in enemyCC_kills:
                    kills += kill
                [attackerCC_hits, attackerCC_wounds, attackerCC_kills] = simulation.calculate_assault(weaponCreator, attackerCC,
                                                                                                      Attack_ToHit, CC_ToWound,
                                                                                                      invo, svo, CC_InstantKill, kills)
                
            else:
                [attackerCC_hits, attackerCC_wounds, attackerCC_kills] = simulation.calculate_assault(weaponCreator, attackerCC,
                                                                                                      Attack_ToHit, CC_ToWound,
                                                                                                      invo, svo, CC_InstantKill, 0)
                
                [attacker2CC_hits, attacker2CC_wounds, attacker2CC_kills] = simulation.calculate_assault(weaponCreator, extraAttackerCC,
                                                                                                         Attack2_ToHit, CC2_ToWound,
                                                                                                         invo, svo, CC2_InstantKill, 0)
 
                [enemyCC_hits, enemyCC_wounds, enemyCC_kills] = simulation.calculate_assault(weaponCreator, enemyCC,
                                                                                             Enemy_ToHit, enemyCC_ToWound,
                                                                                             inva, sva, enemyCC_InstantKill, 0)
                

        # If only extra Enemy (assumes all attacker hits land on primary unit)
        elif hasExtraAttacker:
            if io > ia:
                [enemyCC_hits, enemyCC_wounds, enemyCC_kills] = simulation.calculate_assault(weaponCreator, enemyCC,
                                                                                             Enemy_ToHit, enemyCC_ToWound,
                                                                                             inva, sva, enemyCC_InstantKill, 0)
                
                [enemy2CC_hits, enemy2CC_wounds, enemy2CC_kills] = simulation.calculate_assault(weaponCreator, extraEnemyCC,
                                                                                                Enemy2_ToHit, enemy2CC_ToWound,
                                                                                                inva, sva, enemyCC2_InstantKill, 0)
                kills = 0
                for kill, kill2 in zip(enemyCC_kills, enemy2CC_kills):
                    kills += kill
                    kills += kill2
                [attackerCC_hits, attackerCC_wounds, attackerCC_kills] = simulation.calculate_assault(weaponCreator, attackerCC,
                                                                                                      Attacker_ToHit, CC_ToWound,
                                                                                                      invo, svo, CC_InstantKill, kills)
            elif io < ia:
                [enemy2CC_hits, enemy2CC_wounds, enemy2CC_kills] = simulation.calculate_assault(weaponCreator, extraEnemyCC,
                                                                                                Enemy2_ToHit, enemy2CC_ToWound,
                                                                                                inva, sva, enemyCC2_InstantKill, 0)
                kills = 0
                for kill in enemy2CC_kills:
                    kills += kill
                [attackerCC_hits, attackerCC_wounds, attackerCC_kills] = simulation.calculate_assault(weaponCreator, attackerCC,
                                                                                                      Attacker_ToHit, CC_ToWound,
                                                                                                      invo, svo, CC_InstantKill, kills)
                kills = 0
                for kill in atackerCC_kills:
                    kills += kill
                [enemyCC_hits, enemyCC_wounds, enemyCC_kills] = simulation.calculate_assault(weaponCreator, enemyCC,
                                                                                             Enemy_ToHit, enemyCC_ToWound,
                                                                                             inva, sva, enemyCC_InstantKill, kills)
                
            else:
                [enemyCC_hits, enemyCC_wounds, enemyCC_kills] = simulation.calculate_assault(weaponCreator, enemyCC,
                                                                                             Enemy_ToHit, enemyCC_ToWound,
                                                                                             inva, sva, enemyCC_InstantKill, 0)
                
                [enemy2CC_hits, enemy2CC_wounds, enemy2CC_kills] = simulation.calculate_assault(weaponCreator, extraEnemyCC,
                                                                                                Enemy2_ToHit, enemy2CC_ToWound,
                                                                                                inva, sva, enemyCC2_InstantKill, 0)
                
                [attackerCC_hits, attackerCC_wounds, attackerCC_kills] = simulation.calculate_assault(weaponCreator, attackerCC,
                                                                                                      Attacker_ToHit, CC_ToWound,
                                                                                                      invo, svo, CC_InstantKill, 0)
        else:
            # Primary vs Primary
            if ia > io:
                [attackerCC_hits, attackerCC_wounds, attackerCC_kills] = simulation.calculate_assault(weaponCreator, attackerCC,
                                                                                                      Attack_ToHit, CC_ToWound,
                                                                                                      invo, svo, CC_InstantKill, 0)
                kills = 0
                for kill in attackerCC_kills:
                    kills += kill
                [enemyCC_hits, enemyCC_wounds, enemyCC_kills] = simulation.calculate_assault(weaponCreator, enemyCC,
                                                                                             Enemy_ToHit, enemyCC_ToWound,
                                                                                             inva, sva, enemyCC_InstantKill, kills)
            elif ia < io:
                [enemyCC_hits, enemyCC_wounds, enemyCC_kills] = simulation.calculate_assault(weaponCreator, enemyCC,
                                                                                             Enemy_ToHit, enemyCC_ToWound,
                                                                                             inva, sva, enemyCC_InstantKill, 0)
                kills = 0
                for kill in enemyCC_kills:
                    kills += kill                
                [attackerCC_hits, attackerCC_wounds, attackerCC_kills] = simulation.calculate_assault(weaponCreator, attackerCC,
                                                                                                      Attack_ToHit, CC_ToWound,
                                                                                                      invo, svo, CC_InstantKill, kills)
            else:
                [attackerCC_hits, attackerCC_wounds, attackerCC_kills] = simulation.calculate_assault(weaponCreator, attackerCC,
                                                                                                      Attack_ToHit, CC_ToWound,
                                                                                                      invo, svo, CC_InstantKill, 0)
                
                [enemyCC_hits, enemyCC_wounds, enemyCC_kills] = simulation.calculate_assault(weaponCreator, enemyCC,
                                                                                             Enemy_ToHit, enemyCC_ToWound,
                                                                                             inva, sva, enemyCC_InstantKill, 0)
                
        # Get total stats from shooting
        total_hits   = 0
        total_wounds = 0
        total_kills  = 0
        for hits, wounds, kills in zip(currentShot_hits, currentShot_wounds, currentShot_kills):
            total_hits   += hits
            total_wounds += wounds
            total_kills  += kills

        shoot_hit_list.append(total_hits)
        shoot_wound_list.append(total_wounds)
        shoot_kill_list.append(total_kills)

        Shoot_MeanHit   += total_hits
        Shoot_MeanWound += total_wounds
        Shoot_MeanKill  += total_kills
        
        
        # Get total stats from assault
        total_hits   = 0
        total_wounds = 0
        total_kills  = 0
        for hits, wounds, kills in zip(attackerCC_hits, attackerCC_wounds, attackerCC_kills):
            total_hits   += hits
            total_wounds += wounds
            total_kills  += kills
        for hits, wounds, kills in zip(attacker2CC_hits, attacker2CC_wounds, attacker2CC_kills):
            total_hits   += hits
            total_wounds += wounds
            total_kills  += kills

        Attack_MeanHit   += total_hits
        Attack_MeanWound += total_wounds
        Attack_MeanKill  += total_kills

        attack_hit_list.append(total_hits)
        attack_wound_list.append(total_wounds)
        attack_kill_list.append(total_kills)
        
        # Get total stats from assault
        total_hits   = 0
        total_wounds = 0
        total_kills  = 0
        for hits, wounds, kills in zip(enemyCC_hits, enemyCC_wounds, enemyCC_kills):
            total_hits   += hits
            total_wounds += wounds
            total_kills  += kills
        for hits, wounds, kills in zip(enemy2CC_hits, enemy2CC_wounds, enemy2CC_kills):
            total_hits   += hits
            total_wounds += wounds
            total_kills  += kills

        enemy_hit_list.append(total_hits)
        enemy_wound_list.append(total_wounds)
        enemy_kill_list.append(total_kills)   

        Enemy_MeanHit   += total_hits
        Enemy_MeanWound += total_wounds
        Enemy_MeanKill  += total_kills

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

    # Averages
    shootTable.insert(1, 1, simulation.round_int(Shoot_MeanHit))
    shootTable.insert(2, 1, simulation.round_int(Shoot_MeanWound))
    shootTable.insert(3, 1, simulation.round_int(Shoot_MeanKill))

    atccTable.insert(1, 1, simulation.round_int(Attack_MeanHit))
    atccTable.insert(2, 1, simulation.round_int(Attack_MeanWound))
    atccTable.insert(3, 1, simulation.round_int(Attack_MeanKill))

    opccTable.insert(1, 1, simulation.round_int(Enemy_MeanHit))
    opccTable.insert(2, 1, simulation.round_int(Enemy_MeanWound))
    opccTable.insert(3, 1, simulation.round_int(Enemy_MeanKill))

    # Standard Deviations
    shootTable.insert(1, 2, simulation.standard_dev(shoot_hit_list,   Shoot_MeanHit))
    shootTable.insert(2, 2, simulation.standard_dev(shoot_wound_list, Shoot_MeanWound))
    shootTable.insert(3, 2, simulation.standard_dev(shoot_kill_list,  Shoot_MeanKill))

    atccTable.insert(1, 2, simulation.standard_dev(attack_hit_list,   Attack_MeanHit))
    atccTable.insert(2, 2, simulation.standard_dev(attack_wound_list, Attack_MeanWound))
    atccTable.insert(3, 2, simulation.standard_dev(attack_kill_list,  Attack_MeanKill))

    opccTable.insert(1, 2, simulation.standard_dev(enemy_hit_list,   Enemy_MeanHit))
    opccTable.insert(2, 2, simulation.standard_dev(enemy_wound_list, Enemy_MeanWound))
    opccTable.insert(3, 2, simulation.standard_dev(enemy_kill_list,  Enemy_MeanKill))

    # Min
    shootTable.insert(1, 3, simulation.round_int(min(shoot_hit_list)))
    shootTable.insert(2, 3, simulation.round_int(min(shoot_wound_list)))
    shootTable.insert(3, 3, simulation.round_int(min(shoot_kill_list)))

    atccTable.insert(1, 3, simulation.round_int(min(attack_hit_list)))
    atccTable.insert(2, 3, simulation.round_int(min(attack_wound_list)))
    atccTable.insert(3, 3, simulation.round_int(min(attack_kill_list)))

    opccTable.insert(1, 3, simulation.round_int(min(enemy_hit_list)))
    opccTable.insert(2, 3, simulation.round_int(min(enemy_wound_list)))
    opccTable.insert(3, 3, simulation.round_int(min(enemy_kill_list)))

    # Max
    shootTable.insert(1, 4, simulation.round_int(max(shoot_hit_list)))
    shootTable.insert(2, 4, simulation.round_int(max(shoot_wound_list)))
    shootTable.insert(3, 4, simulation.round_int(max(shoot_kill_list)))

    atccTable.insert(1, 4, simulation.round_int(max(attack_hit_list)))
    atccTable.insert(2, 4, simulation.round_int(max(attack_wound_list)))
    atccTable.insert(3, 4, simulation.round_int(max(attack_kill_list)))

    opccTable.insert(1, 4, simulation.round_int(max(enemy_hit_list)))
    opccTable.insert(2, 4, simulation.round_int(max(enemy_wound_list)))
    opccTable.insert(3, 4, simulation.round_int(max(enemy_kill_list)))

    create_distribution(shoot_kill_list, attack_kill_list, enemy_kill_list)
    
'''
    GUI Setup
'''

root = Tk()
root.columnconfigure(0, weight=1)
root.title("Stathammer "+version)
if os.name == "posix":
    root.wm_iconbitmap('@staticon.xbm') # For non-windows systems (works on linux, not sure about OSX)
else:
    root.wm_iconbitmap('staticon.ico')  # For windows

root.protocol('WM_DELETE_WINDOW', save_init)

#root.minsize(800, 520)


#================#
# Weapon Creator #
#================#
weaponCreator = WCreate.WWindow(root)
weaponCreator.app.protocol('WM_DELETE_WINDOW', refresh_weapons)

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
tableframe = ttk.Frame(probframe)
shootstatframe      = GUI.label_frame_create(tableframe, 'Attacker Shooting Phase', 0, 0)
atassaultstatframe  = GUI.label_frame_create(tableframe, 'Attacker Assault Phase', 1, 0)
opassaultstatframe  = GUI.label_frame_create(tableframe, 'Enemy Assault Phase', 2, 0)
shootTable  = GUI.Table(shootstatframe, 4, 5)
atccTable   = GUI.Table(atassaultstatframe, 4, 5)
opccTable   = GUI.Table(opassaultstatframe, 4, 5)
GUI.create_stat_table(shootTable)
GUI.create_stat_table(atccTable)
GUI.create_stat_table(opccTable)
tableframe.pack()


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

graphframe = GUI.canvas_create(graphpage, 0, 0, [500, 350], 'gray94')
graphframe.bind('<1>', popup_prob)

attackex_one = ttk.Frame(atstatframe, padding="3 3 12 12")
attackex_one.grid(column=0, row=2, sticky=(N, E, W, S))
attackex_one.columnconfigure(0, weight=1)
attackex_one.rowconfigure(2, weight=1)

enemyex_one = ttk.Frame(opstatframe, padding="3 3 12 12")
enemyex_one.grid(column=0, row=2, sticky=(N, E, W, S))
enemyex_one.columnconfigure(0, weight=1)
enemyex_one.rowconfigure(2, weight=1)

#barframe = GUI.frame_create(mainframe, 1, 0)
#calcframe = ttk.Frame(root)
#calcframe.pack()
barframe = ttk.Frame(root)
barframe.pack(side=RIGHT)

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
optmenu.add_separator()
optmenu.add_command(label="Export Distribution", command=export_csv)
IterVar = StringVar()
optmenu.add_cascade(label="Iterations", menu=itermenu)
itermenu.add_radiobutton(label="100", variable=IterVar, value="100")
itermenu.add_radiobutton(label="1000", variable=IterVar, value="1000")
itermenu.add_radiobutton(label="2500", variable=IterVar, value="2500")
itermenu.add_radiobutton(label="5000", variable=IterVar, value="5000")
itermenu.add_radiobutton(label="10000", variable=IterVar, value="10000")
IterVar.set("2500")

# Help ->
helpmenu.add_command(label="About", command=get_about)
helpmenu.add_separator()
helpmenu.add_command(label="Submit Bug", command=bug)

root.config(menu=menubar)

graphcontext = Menu(graphframe)
graphcontext.configure(background='BlanchedAlmond', activebackground='BlanchedAlmond',
                       activeforeground='black', cursor='tcross')

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
attacker_1.name.set('UNIT-NAME')
attacker_1.attacks.set('1')

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
attacker_2.name.set('UNIT-NAME')
attacker_2.attacks.set('1')
      
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
enemy_1.name.set('UNIT-NAME')
enemy_1.attacks.set('1')

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
enemy_2.name.set('UNIT-NAME')
enemy_2.attacks.set('1')

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
calc = ttk.Button(root, text='Calculate', command=calculate, width=20)
#calc.grid(column=0, row=0, ipady=5, pady=10)
calc.pack(ipady=5)
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


# Progress Bar
PBAR = ttk.Progressbar(barframe, orient=HORIZONTAL, length=120, mode='determinate')
PBAR.grid(column=1, row=0, sticky=(S, E))
PBAR['value']=0


#=============#
#   Graph     #  
#=============#
graphframe.create_line(50,300,450,300, width=2)  # X-axis
graphframe.create_line(50,300,50,50, width=2)    # Y-axis

#=============#
#   About     #
#=============#
app = Toplevel(root)
app.title("About Stathammer")
app.lift(root)
app.protocol('WM_DELETE_WINDOW', app.withdraw)
if os.name == "posix":
    app.wm_iconbitmap('@staticon.xbm')
else:
    app.wm_iconbitmap('staticon.ico')
app.resizable(0,0)
titlefrm = GUI.frame_create(app, 0, 0)
txtframe = GUI.frame_create(app, 1, 0)
btnframe = GUI.frame_create(app, 2, 0)
ttk.Label(titlefrm, text='Stathammer v'+version, font='TkDefaultFont 16 bold').grid(column=0,row=0)
ttk.Label(txtframe, text='Kevin Fronczak (c) 2012').grid(column=0,row=0, sticky=W)
GUI.Link(txtframe, 'Email', 'mailto:kfronczak@gmail.com').hyperlink.grid(column=0, row=1, sticky=W)
GUI.Link(txtframe, 'Website', 'http://kevinfronczak.com').hyperlink.grid(column=0, row=2, sticky=W)

# README
readme = Toplevel(app)
readme.title("Readme")
readme.lift(root)
if os.name == "posix":
    readme.wm_iconbitmap('@staticon.xbm')
else:
    readme.wm_iconbitmap('staticon.ico')
readme.protocol('WM_DELETE_WINDOW', readme.withdraw)

t = Text(readme, width=60, height=25, wrap='word', background='gray95', font='TkDefaultFont 10 normal')
t.grid(column=0, row=0, sticky=(N,W,E,S))
s = ttk.Scrollbar(readme, orient=VERTICAL, command=t.yview)
s.grid(column=1, row=0, sticky=(N,S))
t['yscrollcommand']=s.set
f = open('README.txt', 'r')
readme.grid_columnconfigure(0, weight=1)
readme.grid_rowconfigure(0, weight=1)
lines = f.readlines()   
f.close()
data = "".join(lines)
t.insert(END, data)
t.configure(state=DISABLED)
readme.withdraw()

# CHANGELOG
change = Toplevel(app)
change.title("Changelog")
change.lift(root)
if os.name == "posix":
    change.wm_iconbitmap('@staticon.xbm')
else:
    change.wm_iconbitmap('staticon.ico')
change.protocol('WM_DELETE_WINDOW', change.withdraw)

t = Text(change, width=60, height=35, wrap='word', background='gray95', font='TkDefaultFont 10 normal')
t.grid(column=0, row=0, sticky=(N,W,E,S))
s = ttk.Scrollbar(change, orient=VERTICAL, command=t.yview)
s.grid(column=1, row=0, sticky=(N,S))
t['yscrollcommand']=s.set
f = open('CHANGELOG.txt', 'r')
change.grid_columnconfigure(0, weight=1)
change.grid_rowconfigure(0, weight=1)
lines = f.readlines()   
f.close()
data = "".join(lines)
t.insert(END, data)
t.configure(state=DISABLED)
change.withdraw()


# LICENSE
licen = Toplevel(app)
licen.title("License")
licen.lift(root)
if os.name == "posix":
    licen.wm_iconbitmap('@staticon.xbm')
else:
    licen.wm_iconbitmap('staticon.ico')
licen.protocol('WM_DELETE_WINDOW', licen.withdraw)

t = Text(licen, width=60, height=35, wrap='word', background='gray95', font='TkDefaultFont 10 normal')
t.grid(column=0, row=0, sticky=(N,W,E,S))
s = ttk.Scrollbar(licen, orient=VERTICAL, command=t.yview)
s.grid(column=1, row=0, sticky=(N,S))
t['yscrollcommand']=s.set
f = open('LICENSE.txt', 'r')
licen.grid_columnconfigure(0, weight=1)
licen.grid_rowconfigure(0, weight=1)
lines = f.readlines()   
f.close()
data = "".join(lines)
t.insert(END, data)
t.configure(state=DISABLED)
licen.withdraw()


ttk.Button(btnframe, text='Readme',     command=readme.deiconify,  width=15).grid(column=0, row=0, sticky=W)
ttk.Button(btnframe, text='License',    command=licen.deiconify,   width=15).grid(column=1, row=0, sticky=E)
ttk.Button(btnframe, text='Changelog',  command=change.deiconify,  width=15).grid(column=0, row=1, sticky=W)
ttk.Button(btnframe, text='Source',     command=open_source,       width=15).grid(column=1, row=1, sticky=E)
app.withdraw()


root.bind('<Return>', calculate)
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


try:
    load_init()
except IOError:
    pass

root.mainloop()


    
