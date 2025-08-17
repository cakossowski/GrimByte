class Item:
    def __init__(self, name, type_, description, value):
        self.name = name
        self.type_ = type_
        self.description = description
        self.value = value

    def __str__(self):
        return (f"---{self.name}--- \n"
                f"TYPE: {self.type_} \n"
                f"DESCRIPTION: {self.description} \n"
                f"VALUE {self.value} Gold \n")

    def __repr__(self):
        return self.__str__()


class Weapon(Item):
    def __init__(self, name, type_, description, value, ap):
        super().__init__(name, type_, description, value)

        self.ap = ap

