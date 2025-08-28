import chars
import items
import dungeons
import generator

def create_pools_for_startup(item_pool, weapon_pool, encounter_pool, dungeon_pool):
    generator.generate_treasure_pool(item_pool)
    generator.generate_weapon_pool(weapon_pool)
    generator.generate_encounter_pool(encounter_pool)
    generator.generate_dungeon_pool(dungeon_pool)
    return item_pool, weapon_pool, encounter_pool, dungeon_pool

