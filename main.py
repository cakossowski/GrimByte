import state_machine
import generator
import chars
import movement
from movement import check_target_destination, move_player_to_target_destination

# initialize empty lists for pool creation
item_pool = []
weapon_pool = []
encounter_pool = []
dungeon_pool = []
new_map = []


def main():
    # TODO add basic workflow for functions
    state_machine.create_pools_for_startup(item_pool, weapon_pool, encounter_pool, dungeon_pool)
    generator.generate_map(new_map, dungeon_pool, 5, 3)
    generator.render_map(new_map)

    new_player = chars.PlayerChar("Horst", "player", 100, 5, 5, 1)
    new_map[0][0].entities.append(new_player)
    while True:
        target = input("Direction: \n")
        new_position = check_target_destination(new_player, target, new_map)
        if new_position:
            move_player_to_target_destination(new_player, new_position, new_map)




if __name__ == "__main__":
    main()