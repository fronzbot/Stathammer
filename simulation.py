import random

# Method to properly round float to int
def round_int(num):
    if (num > 0):
        return int(num+.5)
    else:
        return int(num-.5)

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

# Calculates number of hits
def to_hit(score, attacks):
    attack_dice = monte_carlo(attacks)
  
    attack_hit_prob = 0

    # Get HIT probability
    for i in range(score-1, 6):
        attack_hit_prob += attack_dice[i]

    return round_int(attack_hit_prob*attacks)

# Calculate number of wounds
def to_wound(score, hits):
    attack_dice = monte_carlo(hits)
  
    attack_wound_prob = 0

    for i in range(score-1, 6):
        attack_wound_prob += attack_dice[i]

    return round_int(attack_wound_prob*hits)

# Calculates amount of kills
def kills(wounds, save):
    if save:
        dice = monte_carlo(wounds)
        save_prob = 0
        for i in range(save-1, 6):
            save_prob += dice[i]
        return round_int((1-save_prob)*wounds)

    else:
        return wounds

# NEEDS A COMMENT    
def create_prob_dict(data, attacks):
    data.sort()
    probdict = {}
    for val in data:
        if val > attacks:
            val = attacks
        try:
            probdict[val] += 1
        except KeyError:
            probdict[val] = 1

    return probdict
        

# Method used to create dictionary of weapon => count        
def sort_weapons(key_list, val_list):
    dictionary = {}
    for weapon, val in zip(key_list, val_list):
        if not val or weapon == 'No Weapon Selected':
            break
        num = int(val)
        dictionary[weapon] = num

    return dictionary

# Method used to get the die roll needed to wound
# parameter 'weapon' is a list ordered as:
# [Shots, Strength, AP, Attributes...]
def get_scoreToWound(weapon_strength, weapon_attributes, opposing_toughness):
    if "Poisoned_3+" in weapon_attributes:
        return 3
    if "Poisoned_4+" in weapon_attributes:
        return 4
    if "Poisoned_5+" in weapon_attributes:
        return 5
    if "+1-Strength" in weapon_attributes:
        weapon_strength += 1
    if "+2-Strength" in weapon_attributes:
        weapon_strength += 2
    if ("Double-Strength" or "Power-Fist" or "Thunder-Hammer") in weapon_attributes:
        weapon_strength *= 2
    
    if weapon_strength == opposing_toughness:
        return 4
    if weapon_strength < opposing_toughness:
        temp = 4 + (opposing_toughness - weapon_strength)
        if temp > 6:
            return 7
        else:
            return temp
    elif weapon_strength > opposing_toughness:
        temp = 4 - (weapon_strength - opposing_toughness)
        if temp < 2:
            return 2
        else:
            return temp


def get_cc_strength(weapon_attributes, base_strength):
    if "+1-Strength" in weapon_attributes:
        base_strength += 1
    if "+2-Strength" in weapon_attributes:
        base_strength += 2
    if ("Double-Strength" or "Power-Fist" or "Thunder-Hammer") in weapon_attributes:
        base_strength *= 2

    return base_strength

    
# Method to check if weapon will ignore armor or have high enough
# Strength for an instant-kill (AP is set to 0 for CC weapons)
def check_instant_kill(strength, toughness, weapon_attributes, weapon_AP):
    print(weapon_attributes)
    if strength >= 2*toughness:
        return True
    if ("Power-Weapon" or "Ignore-Armor" or "Power-Fist" or "Thunder-Hammer") in weapon_attributes:
        return True
    if weapon_AP > 0 and weapon_AP < 3:
        return True

    return False
