### Messing about trying to make a basic game.
import random
import time

### Set variables and functions.

# Player Race List.
player_races = ["Human", "Elf", "Orc", "Dwarf"]

# Player Class List.
player_classes = ["Warrior", "Hunter", "Mage", "Priest", "Rogue", "Warlock"]

# Player start Hit Points.
player_hp = 25

# Abilities [Name, Damage, Initiative, Verb] if Damage is negative is heal.
warrior_abilities = (("Mortal Strike", 4, 2, "use"), ("Charge", 1, 1, "use"), ("Warcry", -2, 1, "use"))
hunter_abilities = (("Ranged Shot", 3, 2, "use"), ("Quick Shot", 2, 1, "use"), ("Nature Mend", -2, 1, "use"))
mage_abilities = (("Frost Bolt", 3, 2, "cast"), ("Fire Bolt", 2, 1, "cast"), ("Protective Ward", -2, 1, "cast"))
priest_abilities = (("Smite", 2, 2, "cast"), ("Holy Fire", 2, 1, "cast"), ("Heal Wounds", -3, 1, "cast"))
rogue_abilities = (("Slash", 2, 2, "use"), ("Throwing Knife", 3, 1, "use"), ("Bottle of Rum", -2, 1, "use"))
warlock_abilities = (("Shadow Bolt", 4, 2, "cast"), ("Drain Life", 3, 2, "cast"))

# Enemy List.
enemy_names = ["Troll", "Gnoll", "Owl Bear", "Bandit", "Thief", "Harpy", "Ogre", "Witch"]

# Difficulty Levels.
levels = ["Easy", "Normal", "Hard"]

# Dice Results.
def d3_result():
    return random.randint(1,3)
def d6_result():
    return random.randint(1,6)

# Proper grammar is only proper. Checks whether an A or An is needed. ---- Not foolproof like an unicorn. 
def ay_or_an(noun):
    vowel = ["A","E","I","O","U"]
    if noun[0] in vowel:
        return "an"
    else:
        return "a"

### Game starts - Player Setup. 

# Invite the player to select a race from the list. 
print("Welcome to this Fantasy Adventure Game!")
time.sleep(2)
print("\nFirst lets create a character, please pick the race you wish to play as from the following options:\n")
time.sleep(2)

for race in player_races:
    print(race)

# User input. Makes sure the chosen race is allowed.
idiot_test = True
while idiot_test == True:
    selected_race = input("\nType your selected race here:  ").title()
    if selected_race in player_races:
        idiot_test = False
    else:
        print("\nOops! Looks like you didn't enter a valid race.")

# Now get the player to pick a class. 
print("\nNow please select the class you wish to play as from the following options:\n")
time.sleep(2)

for classes in player_classes:
    print(classes)
    
#User input. Makes sure the chosen class is allowed. 
idiot_test = True
while idiot_test == True:
    selected_class = input("\nType your selected class here:  ").title()
    if selected_class in player_classes:
        idiot_test = False
    else:
        print("\nOops! Looks like you didn't enter a valid class.")

# Set player abilities based on choice.
player_abilities, damage, initiative, verbs = zip(*globals()[selected_class.lower() + "_abilities"])

# Confirms player choice.
print("\nGreat! You will be playing as {} {} {}.".format(ay_or_an(selected_race), selected_race, selected_class))
time.sleep(2)

# Player chooses difficulty.
print("\nYou will now face a number of enemies which you must vanquish. \nThe number depends on which of the following modes you pick:\n")
time.sleep(3)

for level in levels:
    print(level)

#User input. Makes sure the chosen difficulty is allowed. 
idiot_test = True
while idiot_test == True:
    selected_mode = input("\nType your selected difficulty here:  ").title()
    if selected_mode in levels:
        idiot_test = False
        difficulty = range(3+(levels.index(selected_mode)))
    else:
        print("\nOops! Looks like you didn't enter a valid difficulty.")

# Creates a lineup of enemies to be fought. 3 for easy, 4 for normal, 5 for hard. Enemies get a name and hit points value between 5 and 10. Also adds number description. 
number = ["first", "second", "third", "forth", "final"]
enemy_lineup = [[number[i], enemy_names[random.randint(0,7)], random.randint(5,10)] for i in difficulty]
if len(difficulty) < 5:
    enemy_lineup[-1][0] = number[-1]

### Start combat.

print("\nYou will now face {} enemies. Defeat them all to win the game.".format(str(len(difficulty))))
time.sleep(2)

# Game start state variables.
victory = 0
enemy_no = 0
num = 0
current_player_abilities = player_abilities

### Combat sequence.

while num < len(difficulty):
    # Enemy info.
    enemy_number = enemy_lineup[num][0]
    enemy_current = enemy_lineup[num][1]
    enemy_hp = enemy_lineup[num][2]
    print("\nThe {} enemy approaches... It's {} {} with {} Hit Points.".format(enemy_number, ay_or_an(enemy_current), enemy_current, enemy_hp))
    time.sleep(2)

    while victory == 0:
        time.sleep(1)
        print("\nWhich ability will you use?\n")

        for ability in current_player_abilities:
            print(ability)

        # User input. Makes sure the chosen ability is allowed. Generates player stats for this turn.
        idiot_test = True
        while idiot_test == True:
            chosen_ability = input("\nI want to use:  ").title()
            if chosen_ability in current_player_abilities:
                if chosen_ability == "Drain Life":
                    drain_life_protocol = True
                else:
                    drain_life_protocol = False  
                idiot_test = False
                i = player_abilities.index(chosen_ability)
                ability_damage = damage[i]
                rng = d3_result()
                ability_initiative = initiative[i]
                verb = verbs[i]
            else:
                print("\nOops! Looks like you didn't enter a valid ability.")

        ### Run one round of combat.

        # Check if Drain Life is used.
        if drain_life_protocol == True:
            enemy_damage = d6_result()
            player_hp -= enemy_damage
            if player_hp <= 0:
                player_hp = 0
                victory = -1
            time.sleep(1)
            print("\nThe enemy {} attacks you for {} damage. Your hit points are reduced to {}.".format(enemy_current, enemy_damage, player_hp))
            if victory == -1:
                time.sleep(1)
                print("\nOh no! You've been slain by the {}. You lose the game.".format(enemy_current))
                exit()
            else:
                enemy_hp -= (ability_damage + rng)
                if enemy_hp <= 0:
                    enemy_hp = 0
                    victory = 1
                time.sleep(1)
                print("\nYou {} {}. It does {} + {} damage to the enemy! The {} is reduced to {} hit points.".format(verb, chosen_ability, ability_damage, rng, enemy_current, enemy_hp))
                if victory == 1:
                    time.sleep(1)
                    print("\nWell Done! You defeated the {}.".format(enemy_current))
            heal = ability_damage
            player_hp += (heal + rng)
            time.sleep(2)
            print("\nYou {} {}. It heals you for {} + {} hit points up to {}".format(verb, chosen_ability, heal, rng, player_hp))
            enemy_damage = d6_result()
            player_hp -= enemy_damage
            if player_hp <= 0:
                player_hp = 0
                victory = -1
            time.sleep(1)
            print("\nThe enemy {} attacks you for {} damage. Your hit points are reduced to {}.".format(enemy_current, enemy_damage, player_hp))
            if victory == -1:
                time.sleep(1)
                print("\nOh no! You've been slain by the {}. You lose the game.".format(enemy_current))
                exit()

        # Elif if heal ability is used.
        elif ability_damage < 0:
            heal = (ability_damage * -1)
            player_hp += (heal + rng)
            time.sleep(1)
            print("\nYou {} {}. It heals you for {} + {} hit points up to {}".format(verb, chosen_ability, heal, rng, player_hp))
            enemy_damage = d6_result()
            player_hp -= enemy_damage
            if player_hp <= 0:
                player_hp = 0
                victory = -1
            time.sleep(1)
            print("\nThe enemy {} attacks you for {} damage. Your hit points are reduced to {}.".format(enemy_current, enemy_damage, player_hp))
            if victory == -1:
                time.sleep(1)
                print("\nOh no! You've been slain by the {}. You lose the game.".format(enemy_current))
                exit()

        # ELif player goes first.
        elif ability_initiative == 1:
            enemy_hp -= (ability_damage + rng)
            if enemy_hp <= 0:
                enemy_hp = 0
                victory = 1
            time.sleep(1)
            print("\nYou {} {}. It does {} + {} damage to the enemy! The {} is reduced to {} hit points.".format(verb, chosen_ability, ability_damage, rng, enemy_current, enemy_hp))
            if victory == 1:
                time.sleep(1)
                print("\nWell Done! You defeated the {}.".format(enemy_current))
            else:
                enemy_damage = d6_result()
                player_hp -= enemy_damage
                if player_hp <= 0:
                    player_hp = 0
                    victory = -1
                time.sleep(1)
                print("\nThe enemy {} attacks you for {} damage. Your hit points are reduced to {}.".format(enemy_current, enemy_damage, player_hp))
                if victory == -1:
                    time.sleep(1)
                    print("\nOh no! You've been slain by the {}. You lose the game.".format(enemy_current))
                    exit()

        # Else enemy goes first. 
        else:
            enemy_damage = d6_result()
            player_hp -= enemy_damage
            if player_hp <= 0:
                player_hp = 0
                victory = -1
            time.sleep(1)
            print("\nThe enemy {} attacks you for {} damage. Your hit points are reduced to {}.".format(enemy_current, enemy_damage, player_hp))
            if victory == -1:
                time.sleep(1)
                print("\nOh no! You've been slain by the {}. You lose the game.".format(enemy_current))
                exit()
            else:
                enemy_hp -= (ability_damage + rng)
                if enemy_hp <= 0:
                    enemy_hp = 0
                    victory = 1
                time.sleep(1)
                print("\nYou {} {}. It does {} + {} damage to the enemy! The {} is reduced to {} hit points.".format(verb, chosen_ability, ability_damage, rng, enemy_current, enemy_hp))
                if victory == 1:
                    time.sleep(1)
                    print("\nWell Done! You defeated the {}.".format(enemy_current))
        # Make so player can't use same ability twice.
        current_player_abilities = [not_used for not_used in player_abilities if not_used != chosen_ability]
    victory = 0
    num += 1
    time.sleep(2)

### We're in the Endgame now.
    
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("CONGRATULATIONS! You've beaten the game.")
time.sleep(1)
print("Thank you for playing.")