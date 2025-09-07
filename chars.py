import random
from items import Item

def calculate_dmg(attacker, defender):
    """
    Calculate the damage dealt by an attacker to a defender using their battle stats.

    The formula used is: damage = (attacker.battle_ap ** 2) / (attacker.battle_ap + defender.battle_defense)
    The result is always at least 1 and returned as an integer.

    :param attacker: The entity dealing damage, with a 'battle_ap' attribute.
    :param defender: The entity receiving damage, with a 'battle_defense' attribute.
    :return: The calculated damage value (minimum 1).
    :rtype: int
    """
    damage = (attacker.battle_ap ** 2) / (attacker.battle_ap + defender.battle_defense)
    return max(1, int(damage))

class Entity:
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_

    def __str__(self):
        return (f"Entity Information: \n"
                f"Name: {self.name} \n"
                f"Type: {self.type_} \n")

    def __repr__(self):
        return self.__str__()


class PlayerChar(Entity):
    def __init__(self, name, type_, hp, base_ap, defense, level):
        super().__init__(name, type_)

        self.hp = hp
        self.base_ap = base_ap
        self.battle_ap = 0
        self.base_defense = defense
        self.battle_defense = 0
        self.level = level
        self.inventory = []
        self.inventory_space_max = 5
        self.equipment_weapon = []
        self.equipment_armor = []
        self.gold = 0
        self.position = (0, 0)



    def __str__(self):
        return super().__str__() + (f"HP: {self.hp} "
                                    f"AP: {self.base_ap} "
                                    f"Base Defense: {self.base_defense} "
                                    f"Level: {self.level} ")


    def calculate_current_stats(self):
        """
        Recalculate and update the current battle stats of the character
        based on base values and equipped items.

        :return: None
        :rtype: None
        """
        self.battle_ap = self.equipment_weapon[0].ap + self.base_ap
        self.battle_defense = self.equipment_armor[0].defense + self.base_defense


    def check_inventory_space(self):
        """
        Check if the character's inventory has free space for additional items.

        :return: True if there is space available, False otherwise.
        :rtype: bool
        """
        return len(self.inventory) < self.inventory_space_max


    def put_in_inventory(self, target_item):
        """
        Attempt to add an item to the character's inventory.
        If there is available space, the item is added.
        If the inventory is full, the item is destroyed.

        :param target_item: The item to be added to the inventory.
        :type target_item: object
        :return: None
        :rtype: None
        """
        if self.check_inventory_space():
            self.inventory.append(target_item)
            print(f"You picked up: {target_item.name}")
        else:
            print(f"Inventory is full! {target_item.name} will be destroyed!")
            del target_item


    def show_inventory(self):
        """
        Display the contents of the character's inventory in the console.

        :return: None
        :rtype: None
        """
        print(f"Your inventory currently contains the following items:")
        for item in self.inventory:
            print(item)


    def attack_monster(self, target):
        """
        Perform an attack on a target monster, calculate the dealt damage,
        and update the target's HP accordingly.

        :param target: The monster being attacked.
        :type target: chars.Monster
        :return: None
        :rtype: None
        """
        dmg = calculate_dmg(self, target)
        target.hp -= dmg
        print(f"{self.name} launches an attack! It deals {dmg} damage, {target.name} has {target.hp} HP remaining")


    def trade_item(self):
        # TODO flesh out function
        pass


    def level_up(self):
        """
        Increase the character's level and improve base stats accordingly.

        Effects:
        - Attack power (base_ap) increases by 2
        - Defense (base_defense) increases by 1
        - Health points (hp) increase by 4
        - Level increases by 1

        :return: None
        :rtype: None
        """
        self.base_ap += 2
        self.base_defense += 1
        self.hp += 4
        self.level += 1


class Trader(Entity):
    def __init__(self, name, type_, description):
        super().__init__(name, type_)

        self.description = description
        self.inventory = []


class Monster(Entity):
    def __init__(self, name, type_, base_ap, base_defense, base_hp, death_quote):
        super().__init__(name, type_)

        self.base_ap = base_ap
        self.base_defense = base_defense
        self.base_hp = base_hp

        self.battle_ap = 0
        self.weapon = []
        self.death_quote = death_quote

    def __str__(self):
        return super().__str__() + (f"BASE AP: {self.base_ap} \n"
                                    f"BASE DEFENSE: {self.base_defense} \n"
                                    f"BASE HP: {self.base_hp} \n"
                                    f"DEATH MSG: '{self.death_quote}' \n"
                                    f"---- END OF ENTITY INFORMATION FOR THIS OBJECT --- \n")

    def calculate_battle_ap(self):
        """
        Calculate and update the character's current battle attack power
        based on the equipped weapon and base attack power.

        :return: None
        :rtype: None
        """
        self.battle_ap = self.weapon[0].ap + self.base_ap


    def attack_player(self, player: PlayerChar):
        """
        Perform an attack on the player, calculate the dealt damage,
        and update the player's HP accordingly.

        :param player: The player character being attacked.
        :type player: PlayerChar
        :return: None
        :rtype: None
        """
        dmg = calculate_dmg(self, player)
        player.hp -= dmg
        print(f"{self.name} launched an attack on you - it did {dmg} damage. You have {player.hp} HP left!")


def calculate_base_stats_monsters():
    """
    Generate randomized base stats for a fodder monster.

    :return: A tuple containing base attack power, base defense, and base HP.
    :rtype: tuple[int, int, int]
    """
    base_ap = random.randint(3, 5)
    base_defense = random.randint(3, 6)
    base_hp = random.randint(8, 12)
    return base_ap, base_defense, base_hp

def calculate_base_stats_bosses():
    """
    Generate randomized base stats for a boss monster.

    :return: A tuple containing base attack power, base defense, and base HP.
    :rtype: tuple[int, int, int]
    """
    base_ap = random.randint(7, 9)
    base_defense = random.randint(8, 10)
    base_hp = random.randint(40, 55)
    return base_ap, base_defense, base_hp


def sell_item(player: PlayerChar, merchant: Trader, item_name: str):
    """
    Sell an item from the player's inventory to a merchant.
    If the item is found, it is transferred to the merchant,
    the player receives its value in gold, and the item is removed
    from the player's inventory.

    :param player: The player character selling the item.
    :type player: PlayerChar
    :param merchant: The merchant (trader) buying the item.
    :type merchant: Trader
    :param item_name: The name of the item to be sold.
    :type item_name: str
    :return: None
    :rtype: None
    """
    traded_item = next((item for item in player.inventory if item.name == item_name), None)
    if traded_item is None:
        print("You don't possess this ominous item!")
        return

    merchant.inventory.append(traded_item)
    player.gold += traded_item.value
    player.inventory.remove(traded_item)
    print(f"You sold {traded_item.name} for {traded_item.value} Gold.")
    print(f"{merchant.name}: Thank you, Traveller!")
