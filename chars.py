def calculate_dmg(attacker, defender):
    damage = (attacker.ap ** 2) / (attacker.ap + defender.defense)
    return max(1, int(damage))

class Entity:
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_

    def __str__(self):
        return (f"Entity Information \n"
                f"Name: {self.name} "
                f"Type: {self.type_} ")

    def __repr__(self):
        return self.__str__()


class PlayerChar(Entity):
    def __init__(self, name, type_, hp, ap, defense, level):
        super().__init__(name, type_)

        self.hp = hp
        self.ap = ap
        self.defense = defense
        self.level = level
        self.inventory = []
        self.inventory_space_max = 5
        self.equipment = []


    def __str__(self):
        return super().__str__() + (f"HP: {self.hp} "
                                    f"AP: {self.ap} "
                                    f"Defense: {self.defense} "
                                    f"Level: {self.level} ")


    def calculate_current_stats(self):
        # TODO flesh out function
        pass


    def check_inventory_space(self):
        return len(self.inventory) < self.inventory_space_max


    def put_in_inventory(self, target_item):
        if self.check_inventory_space():
            self.inventory.append(target_item)
            print(f"You picked up: {target_item.name}")
        else:
            print(f"Inventory is full! {target_item.name} will be destroyed!")
            del target_item


    def show_inventory(self):
        print(f"Your inventory currently contains the following items:")
        for item in self.inventory:
            print(item)


    def attack_target(self, target):
        dmg = calculate_dmg(self, target)
        target.hp -= dmg
        print(f"{self.name} launches an attack! It deals {dmg} damage, {target.name} has {target.hp} HP remaining")


    def trade_item(self):
        # TODO flesh out function
        pass



char_1 = PlayerChar("Horst", "Player", 100, 5, 3, 1)
print(char_1)

char_2 = PlayerChar("Joachim", "Player", 100, 5, 3, 1)
print(char_2)

char_1.attack_target(char_2)