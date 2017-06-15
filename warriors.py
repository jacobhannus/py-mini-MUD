# TODO:
# TODO: Check if it's possible to color code warriors and other significant statements. //(Yes, with e.g. PyPi Colorama)
# TODO: Make the game playable with more than two warriors.
# TODO: Improve the combatant selection process.
# TODO: Add more weapons (created from combinations of words), more attack modes (?), defense modes (?), and possibly
# TODO: other features (more creatures). Add more descriptive language and comments into the gameplay.


import math
import random
import time

class Warrior:

    def __init__(self, name="", health=100, stamina=100, max_damage=50, max_block=50):
        self.name = name
        self.health = health
        self.stamina = stamina
        self.max_damage = max_damage
        self.max_block = max_block

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):

        if value.isalpha():
            self.__name = value.capitalize()
        else:
            print("Please only enter letters for name")

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):

        if type(value) == int:
            self.__health = value
        else:
            print("Please only enter a numerical value for health")

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):

        if type(value) == int:
            self.__stamina = value
        else:
            print("Please only enter a numerical value for stamina")

    @property
    def max_damage(self):
        return self.__max_damage

    @max_damage.setter
    def max_damage(self, value):

        if type(value) == int:
            self.__max_damage = value
        else:
            print("Please only enter a numerical value for maximum damage")

    @property
    def max_block(self):
        return self.__max_block

    @max_block.setter
    def max_block(self, value):

        if type(value) == int:
            self.__max_block = value
        else:
            print("Please only enter a numerical value for maximum block")

    def attack(self):
        attack_cap = math.trunc(((self.stamina / 100) + (self.health / 100)) / 2 * (self.max_damage + 1))
        if attack_cap > 1:
            attack_power = random.randrange(1, attack_cap)
        else:
            attack_power = 1
        return attack_power

    def block(self, attack_power):
        block_cap = math.trunc(((self.stamina / 100) + (self.health / 100)) / 2 * (self.max_block + 1))
        if block_cap > 0:
            block_power = random.randrange(0, min(block_cap, attack_power))
        else:
            block_power = 0
        return block_power

def print_bars(warrior_1, warrior_2):

    if warrior_1.health >= 0:
        hp_bar1_length = math.trunc(warrior_1.health / 10)
    else:
        hp_bar1_length = 0
    if warrior_2.health >= 0:
        hp_bar2_length = math.trunc(warrior_2.health / 10)
    else:
        hp_bar2_length = 0

    if warrior_1.stamina >= 0:
        stamina_bar1_length = math.trunc(warrior_1.stamina / 10)
    else:
        stamina_bar1_length = 0
    if warrior_2.stamina >= 0:
        stamina_bar2_length = math.trunc(warrior_2.stamina / 10)
    else:
        stamina_bar2_length = 0

    bars1_health = "(" + str(warrior_1.health) + " %)"
    bars2_health = "(" + str(warrior_2.health) + " %)"

    if len(bars1_health) > len(bars2_health):
        bars1_health_field = bars1_health
        bars2_health_field = bars2_health + ' ' * (len(bars1_health) - len(bars2_health))
    elif len(bars1_health) < len(bars2_health):
        bars2_health_field = bars2_health
        bars1_health_field = bars1_health + ' ' * (len(bars2_health) - len(bars1_health))
    else:
        bars1_health_field = bars1_health
        bars2_health_field = bars2_health

    bars1 = "HP: [" + '#' * hp_bar1_length + ' ' * (10 - hp_bar1_length) + "] " + bars1_health_field + '   '
    bars1_cont = "Stamina: [" + '#' * stamina_bar1_length + ' ' * (10 - stamina_bar1_length) + \
        "] (" + str(warrior_1.stamina) + " %)"
    hp_stamina_bars1 = bars1 + bars1_cont
    bars2 = "HP: [" + '#' * hp_bar2_length + ' ' * (10 - hp_bar2_length) + "] " + bars2_health_field + '   '
    bars2_cont = "Stamina: [" + '#' * stamina_bar2_length + ' ' * (10 - stamina_bar2_length) + \
                 "] (" + str(warrior_2.stamina) + " %)"
    hp_stamina_bars2 = bars2 + bars2_cont
    bars1_name = warrior_1.name
    bars2_name = warrior_2.name

    if len(bars1_name) > len(bars2_name):
        bars1_name_field = bars1_name
        bars2_name_field = bars2_name + ' ' * (len(bars1_name) - len(bars2_name))
    elif len(bars1_name) < len(bars2_name):
        bars2_name_field = bars2_name
        bars1_name_field = bars1_name + ' ' * (len(bars2_name) - len(bars1_name))
    else:
        bars1_name_field = bars1_name
        bars2_name_field = bars2_name

    total_bar_1 = bars1_name_field + '   ' + hp_stamina_bars1
    total_bar_2 = bars2_name_field + '   ' + hp_stamina_bars2
    print(total_bar_1)
    print(total_bar_2)
    print()


def fight(warrior_1, warrior_2):

    if (random.randrange(1, 101) / 100) <= (warrior_1.health / (warrior_1.health + warrior_2.health)):
        attack_turn = 1
    else:
        attack_turn = 2

    if attack_turn == 1:
        attack = warrior_1.attack()
        block = warrior_2.block(attack)
        damage = attack - block
        warrior_2.health -= damage
        warrior_1.stamina -= math.trunc(attack / 4)

        time.sleep((100 - warrior_1.health) / 50 + random.randrange(0, 301) / 100)
        attack_str = warrior_1.name + " attacks " + warrior_2.name + " with the power of " + str(attack) + ". "
        if block > 0:
            block_str = warrior_2.name + " manages to block " + str(block) + " of the damage. "
        else:
            block_str = ""
        damage_str = warrior_2.name + " suffers " + str(damage) + " damage. "
        block_dmg_str = block_str + damage_str
        print(attack_str, end="")
        if attack / warrior_1.max_damage <= 0.10:
            print("Embarrassing! ", end="")
        print(block_dmg_str, end="")
        if damage / warrior_1.max_damage >= 0.90:
            print("Touché! ", end="")
        print()
        time.sleep(0.4)
        print(warrior_2.name, "is down to", warrior_2.health, "health.")
        print()

    else:
        attack = warrior_2.attack()
        block = warrior_1.block(attack)
        damage = attack - block
        warrior_1.health -= damage
        warrior_2.stamina -= math.trunc(attack / 4)

        time.sleep((100 - warrior_2.health) / 50 + random.randrange(0, 301) / 100)
        attack_str = warrior_2.name + " attacks " + warrior_1.name + " with the power of " + str(attack) + ". "
        if block > 0:
            block_str = warrior_1.name + " manages to block " + str(block) + " of the damage. "
        else:
            block_str = ""
        damage_str = warrior_1.name + " suffers " + str(damage) + " damage. "
        block_dmg_str = block_str + damage_str
        print(attack_str, end="")
        if attack / warrior_2.max_damage <= 0.10:
            print("Embarrassing! ", end="")
        print(block_dmg_str, end="")
        if damage / warrior_2.max_damage >= 0.90:
            print("Touché! ", end="")
        print()
        time.sleep(0.4)
        print(warrior_1.name, "is down to", warrior_1.health, "health.")
        print()


def battle(combatant_list):
    
    alive_warrior_list = []
    for combatant in combatant_list:
        if combatant.health > 0:
            alive_warrior_list.append(combatant)
    fight_counter = 0
    while len(alive_warrior_list) > 1:
        combatant_1 = random.randrange(0, len(alive_warrior_list))
        combatant_2 = random.randrange(0, len(alive_warrior_list))
        while combatant_2 == combatant_1:
            combatant_2 = random.randrange(0, len(alive_warrior_list))
        fight(alive_warrior_list[combatant_1], alive_warrior_list[combatant_2])
        fight_counter += 1
        if fight_counter == 5:
            time.sleep(0.6)
            print_bars(alive_warrior_list[0], alive_warrior_list[1])
            fight_counter = 0
        if alive_warrior_list[combatant_1].health <= 0:
            print(alive_warrior_list[combatant_1].name, "has succumbed to his wounds and",
                  alive_warrior_list[combatant_2].name, "prevails.")
            print("RIP", alive_warrior_list[combatant_1].name)
            print()
            del alive_warrior_list[combatant_1]
        elif alive_warrior_list[combatant_2].health <= 0:
            print(alive_warrior_list[combatant_2].name, "has succumbed to his wounds and",
                  alive_warrior_list[combatant_1].name, "prevails.")
            print("RIP", alive_warrior_list[combatant_2].name)
            del alive_warrior_list[combatant_2]
            print()
    return alive_warrior_list[0]


def main():
    warrior_amount = int(input("How many warriors do you want to create? "))
    warrior_list = []
    for warrior in range(0, warrior_amount):
        name_str = "Enter name for warrior " + str(warrior + 1) + " : "
        name = input(name_str)
        warrior_list.append(Warrior(name))
    time.sleep(0.9)
    print("\nA great battle ensues...\n")
    victor = battle(warrior_list)
    time.sleep(1)
    print(victor.name, "is VICTORIOUS!\n")
    time.sleep(0.8)
    print("Game Over")

main()
