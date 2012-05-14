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

def to_hit(score, attacks):
    attack_dice = monte_carlo(attacks)
  
    attack_hit_prob = 0

    # Get HIT probability
    for i in range(score-1, 6):
        attack_hit_prob += attack_dice[i]

    return round_int(attack_hit_prob*attacks)

def to_wound(score, hits):
    attack_dice = monte_carlo(hits)
  
    attack_wound_prob = 0

    for i in range(score-1, 6):
        attack_wound_prob += attack_dice[i]

    return round_int(attack_wound_prob*hits)

def kills(wounds, save):
    if save:
        dice = monte_carlo(wounds)
        save_prob = 0
        for i in range(save-1, 6):
            save_prob += dice[i]
        return round_int((1-save_prob)*wounds)

    else:
        return wounds
    
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
        
        


    
        
