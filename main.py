import state_machine
import generator

item_pool = []
weapon_pool = []
encounter_pool = []
dungeon_pool = []
new_map = []


def main():
    state_machine.create_pools_for_startup(item_pool, weapon_pool, encounter_pool, dungeon_pool)
    generator.generate_map(new_map, dungeon_pool, 5, 3)
    generator.render_map(new_map)

if __name__ == "__main__":
    main()