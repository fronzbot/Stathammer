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
import GUI
import sys
import os

weaponAttributes = {'gun': ('Ignore-Armor', 'Ignore-Invul', 'Lance',
                            'Melta', 'None', 'Poisoned_3+', 'Poisoned_4+',
                            'Poisoned_5+', 'Re-roll Hits','Re-roll Wounds', 'Rending', 'Sniper'),
                    'cc' : ('+1-Strength', '+2-Strength', 'Double-Strength', 'None', 'Ignore-Invul',
                            'Poisoned_3+', 'Poisoned_4+', 'Poisoned_5+', 'Power-Fist', 'Power-Weapon',
                            'Re-roll Hits', 'Re-roll Wounds', 'Rending', 'Thunder-Hammer', 'Witchblade')}


class WWindow(object):
    def __init__(self, top_level):
        self.gunAttrCount = 1
        self.ccAttrCount  = 1
        self.app = Toplevel(top_level)
        self.app.title("Weapon Creation Tool")
        self.app.lift(top_level)
        
        # Get current weapon lists
        self.guns = self.update_dicts('gnl.wf')
        self.cc   = self.update_dicts('ccl.wf')
        
        if os.name == "posix":
            self.app.wm_iconbitmap('@staticon.xbm') # For non-windows systems (works on linux, not sure about OSX)
        else:
            self.app.wm_iconbitmap('staticon.ico') # For windows
        
        # Frames
        self.gunframe = GUI.label_frame_create(self.app, 'Shooting', 0, 0)
        self.ccframe  = GUI.label_frame_create(self.app, 'Assault', 1, 0)
        self.gunstatframe = GUI.frame_create(self.gunframe, 0, 0) 
        self.gunsvframe   = GUI.frame_create(self.gunframe, 1, 0)
        self.ccstatframe  = GUI.frame_create(self.ccframe, 0, 0)
        self.ccsvframe    = GUI.frame_create(self.ccframe, 1, 0)
        self.gunsvframe   = GUI.frame_create(self.gunstatframe, 2, 0)
        self.ccsvframe    = GUI.frame_create(self.ccstatframe,  2, 0)
        self.gunattrbtns  = GUI.frame_create(self.gunstatframe, 0, 5)
        self.ccattrbtns   = GUI.frame_create(self.ccstatframe,  0, 3)
        self.gunattrbtns.grid(sticky=(N, S))
        self.ccattrbtns.grid(sticky=(N, S))
        
        # Labels
        ttk.Label(self.gunstatframe, text='Weapon Name').grid(column=0, row=0, sticky=W)
        ttk.Label(self.gunstatframe, text='Shots', justify='center').grid(column=1, row=0, sticky=W)
        ttk.Label(self.gunstatframe, text='S', justify='center').grid(column=2, row=0)
        ttk.Label(self.gunstatframe, text='AP', justify='center').grid(column=3, row=0)
        ttk.Label(self.gunstatframe, text='Attributes', justify='center').grid(column=4, row=0)
    
        ttk.Label(self.ccstatframe, text='Weapon Name').grid(column=0, row=0, sticky=W)
        ttk.Label(self.ccstatframe, text='Atx', justify='center').grid(column=1, row=0)
        ttk.Label(self.ccstatframe, text='Attributes', justify='center').grid(column=2, row=0)
        
        # Entries
        self.gunNameVar = StringVar()
        self.ccNameVar  = StringVar()
        self.ccAtkVar   = StringVar()
        self.gunShotVar = StringVar()
        self.gunSVar    = StringVar()
        self.gunAPVar   = StringVar()
        self.gunName    = GUI.input_create(self.gunstatframe, 'entry', self.gunNameVar, 25, [1, 0, (W, E)], [])
        self.gunShots   = GUI.input_create(self.gunstatframe, 'entry', self.gunShotVar, 4,  [1, 1, (W, E)], [])
        self.gunS       = GUI.input_create(self.gunstatframe, 'entry', self.gunSVar,    2,  [1, 2, (W, E)], [])
        self.gunAP      = GUI.input_create(self.gunstatframe, 'entry', self.gunAPVar,   2,  [1, 3, (W, E)], [])
        self.CCName     = GUI.input_create(self.ccstatframe,  'entry', self.ccNameVar,  25, [1, 0, (W, E)], [])
        self.CCAtk      = GUI.input_create(self.ccstatframe,  'entry', self.ccAtkVar,   4,  [1, 1, (W, E)], [])
        
        self.gunS.grid(padx=2)
        self.app.withdraw()
        self.gunNameVar.set('ENTER NAME OF GUN')
        self.ccNameVar.set('ENTER NAME OF WEAPON')
        self.gunShotVar.set('#')
        self.ccAtkVar.set('#')
        self.gunSVar.set('#')
        self.gunAPVar.set('#')

        self.addGunAttr = ttk.Button(self.gunattrbtns, text = '+', width=3, command=self.add_gun_attr)
        self.delGunAttr = ttk.Button(self.gunattrbtns, text = '-', width=3, command=self.del_gun_attr)
        self.addCCAttr  = ttk.Button(self.ccattrbtns,  text = '+', width=3, command=self.add_cc_attr)
        self.delCCAttr  = ttk.Button(self.ccattrbtns,  text = '-', width=3, command=self.del_cc_attr)
        self.addGunAttr.grid(column=0, row=0, sticky=(W, N, S))
        self.delGunAttr.grid(column=1, row=0, sticky=(E, N, S))
        self.addCCAttr.grid(column=0, row=0, sticky=(W, N, S))
        self.delCCAttr.grid(column=1, row=0, sticky=(E, N, S))
        
        # Attributes Boxes
        self.gunAttrVar1 = StringVar()
        self.gunAttrVar2 = StringVar()
        self.gunAttrVar3 = StringVar()
        self.gunAttrVar4 = StringVar()
        self.ccAttrVar1  = StringVar()
        self.ccAttrVar2  = StringVar()
        self.ccAttrVar3  = StringVar()
        self.ccAttrVar4  = StringVar()
        self.gunAttr1 = ttk.Combobox(self.gunstatframe, textvariable=self.gunAttrVar1)
        self.gunAttr2 = ttk.Combobox(self.gunstatframe, textvariable=self.gunAttrVar2, state=DISABLED)
        self.gunAttr3 = ttk.Combobox(self.gunstatframe, textvariable=self.gunAttrVar3, state=DISABLED)
        self.gunAttr4 = ttk.Combobox(self.gunstatframe, textvariable=self.gunAttrVar4, state=DISABLED)
        self.ccAttr1  = ttk.Combobox(self.ccstatframe,  textvariable=self.ccAttrVar1)
        self.ccAttr2  = ttk.Combobox(self.ccstatframe,  textvariable=self.ccAttrVar2, state=DISABLED)
        self.ccAttr3  = ttk.Combobox(self.ccstatframe,  textvariable=self.ccAttrVar3, state=DISABLED)
        self.ccAttr4  = ttk.Combobox(self.ccstatframe,  textvariable=self.ccAttrVar4, state=DISABLED)
        self.gunAttr1.grid(column=4, row=1, padx=2)
        self.gunAttr2.grid(column=5, row=1, padx=2)
        self.gunAttr3.grid(column=4, row=2, padx=2)
        self.gunAttr4.grid(column=5, row=2, padx=2)
        self.ccAttr1.grid(column=2, row=1, padx=2)
        self.ccAttr2.grid(column=3, row=1, padx=2)
        self.ccAttr3.grid(column=2, row=2, padx=2)
        self.ccAttr4.grid(column=3, row=2, padx=2)
        
        self.gunAttr1['values'] = weaponAttributes['gun']
        self.gunAttr2['values'] = weaponAttributes['gun']
        self.gunAttr3['values'] = weaponAttributes['gun']
        self.gunAttr4['values'] = weaponAttributes['gun']
        self.ccAttr1['values']  = weaponAttributes['cc']
        self.ccAttr2['values']  = weaponAttributes['cc']
        self.ccAttr3['values']  = weaponAttributes['cc']
        self.ccAttr4['values']  = weaponAttributes['cc']
        self.gunAttr1.set('None')
        self.gunAttr2.set('None')
        self.gunAttr3.set('None')
        self.gunAttr4.set('None')
        self.ccAttr1.set('None')
        self.ccAttr2.set('None')
        self.ccAttr3.set('None')
        self.ccAttr4.set('None')
        
        
        self.saveGun = ttk.Button(self.gunsvframe, text = 'Save Weapon', width=15, command=self.save_gun)
        self.saveCC  = ttk.Button(self.ccsvframe,  text = 'Save Weapon', width=15, command=self.save_cc)
        self.saveGun.grid(column=0, row=0, sticky=(N, S))
        self.saveCC.grid(column=0,  row=0, sticky=(N, S))

    # Method is used to save gun information into file gnl.wf
    # Each weapon is saved as an array seperated by spaces.
    # [Name] [Strength] [AP] [Attributes...]
    def save_gun(self):
        
        gunAttrBoxes = (self.gunAttrVar1.get(), self.gunAttrVar2.get(), self.gunAttrVar3.get(), self.gunAttrVar4.get())
        name = "_".join(self.gunNameVar.get().split(" "))

        # Check if weapon already exists and prompt for overwrite if it does
        if name in self.guns:
            result = messagebox.askokcancel(title='Weapon Creator', message='Overwrite Weapon?',
                                            detail=name+" already exists, do you want to overwrite this entry?",
                                            icon='question', default='cancel', parent=self.app)
            if not result:
                return
        
        data = [self.gunShotVar.get(), self.gunSVar.get(), self.gunAPVar.get()]
        
        # Loop through additional attributes and append to data
        for i in range(0, self.gunAttrCount):
            data.append(gunAttrBoxes[i])

        # Add to gun dictionary
        self.guns[name] = data

        f = open('gnl.wf', 'w')

        # A catch for any unforseen errors.  Throws error window to screen
        # to give user more error information to make bug tracking simpler
        try:
            for key in self.guns:
                f.write(key)
                for element in self.guns[key]:
                    f.write(" "+element)
                f.write(" \n")
            f.close()
            messagebox.showinfo(title='Weapon Creator', message='Save Complete!', detail='Weapon Save Successful!',
                                icon='info', default='ok', parent=self.app)
        except:
            f.close()
            e = "In save gun method:\n"+str(sys.exc_info()[1])
            messagebox.showerror(title='Weapon Creator', message='ERROR', detail=e, icon='error',
                                default='ok', parent=self.app)
            self.app.withdraw()

            
    # Method is used to save cc information into file ccl.wf
    # Each weapon is saved as an array seperated by spaces.
    # [Name] [Attributes...]
    def save_cc(self):
        ccAttrBoxes = (self.ccAttrVar1.get(), self.ccAttrVar2.get(), self.ccAttrVar3.get(), self.ccAttrVar4.get())

        name = "_".join(self.ccNameVar.get().split(" "))
        # Check if weapon already exists and prompt for overwrite if it does
        if name in self.cc:
            result = messagebox.askokcancel(title='Weapon Creator', message='Overwrite Weapon?',
                                            detail=name+" already exists, do you want to overwrite this entry?",
                                            icon='question', default='cancel', parent=self.app)
            if not result:
                return

        data = [self.ccAtkVar.get()]
        # Loop through additional attributes and append to data
        for i in range(0, self.ccAttrCount):
            data.append(ccAttrBoxes[i])

        # Add to cc dictionary
        self.cc[name] = data
        
        f = open('ccl.wf', 'w')

        # A catch for any unforseen errors.  Throws error window to screen
        # to give user more error information to make bug tracking simpler
        try:
            for key in self.cc:
                f.write(key)
                for element in self.cc[key]:
                    f.write(" "+element)
                f.write(" \n")
            f.close()
            messagebox.showinfo(title='Weapon Creator', message='Save Complete!', detail='Weapon Save Successful!',
                                icon='info', default='ok', parent=self.app)
        except:
            f.close()
            e = "In save cc method:\n"+str(sys.exc_info()[1])
            messagebox.showerror(title='Weapon Creator', message='ERROR', detail=e, icon='error',
                                default='ok', parent=self.app)
            self.app.withdraw() 

    def show(self):
        self.app.deiconify()

    # Methods to either enable or disable attribute boxes
    def add_gun_attr(self):
        self.gunAttrCount += 1
        if self.gunAttrCount > 4:
            self.gunAttrCount = 4
        else:
            attrBox = (self.gunAttr2, self.gunAttr3, self.gunAttr4)
            attrBox[self.gunAttrCount-2].config(state=NORMAL)
            
    def del_gun_attr(self):
        self.gunAttrCount -= 1
        if self.gunAttrCount < 1:
            self.gunAttrCount = 1
        else:
            attrBox = (self.gunAttr2, self.gunAttr3, self.gunAttr4)
            attrBox[self.gunAttrCount-1].config(state=DISABLED)

    def add_cc_attr(self):
        self.ccAttrCount += 1
        if self.ccAttrCount > 4:
            self.ccAttrCount = 4
        else:
            attrBox = (self.ccAttr2, self.ccAttr3, self.ccAttr4)
            attrBox[self.ccAttrCount-2].config(state=NORMAL)
            
    def del_cc_attr(self):
        self.ccAttrCount -= 1
        if self.ccAttrCount < 1:
            self.ccAttrCount = 1
        else:
            attrBox = (self.ccAttr2, self.ccAttr3, self.ccAttr4)
            attrBox[self.ccAttrCount-1].config(state=DISABLED)

    def update_dicts(self, file):
        dictionary = {}

        # Open if file exists, exit if it does not
        try:
            f = open(file, 'r')
            data = f.readlines()
            f.close()

            for weaponStr in data:
                paramList = []
                weapon = weaponStr.split(" ")
                key = weapon.pop(0)
                for attrib in weapon:
                    if attrib == "\n":
                        break
                    paramList.append(attrib)

                # Add to gun dictionary
                dictionary[key] = paramList
                
        except IOError:
            # No weapon file
            pass

        return dictionary
