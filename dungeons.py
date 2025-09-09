class DungeonRoom:
    def __init__(self, name, type_, description):
        self.name = name
        self.type_ = type_
        self.entities = []
        self.description = description
        self.blocked = False
        self.treasures = []
        self.position = ()
        self.visited = False
        self.enemies_visible = True

    def __str__(self):
        return (f"---Dungeon Room---"
                f"NAME: {self.name} \n"
                f"TYPE: {self.type_} \n"
                f"DESCRIPTION: {self.description} \n"
                f"BLOCKED: {self.blocked}\n"
                f"ENTITIES: {self.entities} \n"
                f"TREASURES: {self.treasures} \n"
                f"POSITION: {self.position} \n"
                f"---END OF ROOM--- \n")

    def __repr__(self):
        return self.__str__()

