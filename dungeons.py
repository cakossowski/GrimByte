class DungeonRoom:
    def __init__(self, name, type_, description, blocked):
        self.name = name
        self.type_ = type_
        self.monsters = []
        self.description = description
        self.blocked = blocked
        self.treasures = []


    def __str__(self):
        return (f"---Dungeon Room---"
                f"NAME: {self.name} \n"
                f"TYPE: {self.type_} \n"
                f"DESCRIPTION: {self.description} \n"
                f"BLOCKED: {self.blocked}\n"
                f"MONSTERS {self.monsters} \n"
                f"TREASURES: {self.treasures} \n"
                f"---END OF ROOM---")

    def __repr__(self):
        return self.__str__()

