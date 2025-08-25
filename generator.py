import chars
import dungeons
from dungeons import DungeonRoom
from items import Item, Weapon
import random

# initial dictionary for room names and description
room_names_and_desc = {
    "Hall of Whispers": "The walls gossip about your failures… and they never forget.",
    "Cursed Pantry": "Food so rotten even the rats leave polite notes.",
    "Skeleton Ballroom": "Bony dancers practice their eternal waltz, no partner required.",
    "Bloody Chapel": "Candles flicker over altars long past any holy inspection.",
    "Spider's Antechamber": "Webs so thick even spiders need a machete.",
    "Torturer's Library": "Books scream silently, the margins soaked in irony… and blood.",
    "Forgotten Crypt": "Where the dead nap and occasionally judge your life choices.",
    "Ghoul's Pantry": "Dinner served cold, with a side of gnawing teeth.",
    "Mirror of Regret": "Shows not your face, but the awful decisions behind it.",
    "Pit of Endless Echoes": "Every scream echoes… like a bad punchline in a void.",
    "Haunted Armory": "Armor moves by itself, but don’t worry—it’s a pacifist.",
    "Alchemist's Demise": "Potions bubble ominously; the owner did not survive the taste test.",
    "Chamber of Bones": "The décor is skeletal, the vibe is judgmental.",
    "The Rotting Garden": "Plants die slowly, plotting revenge on anyone who enters.",
    "Bloodstained Hall": "Every stain tells a story… none of them are cheerful.",
    "Sorcerer's Attic": "Books levitate, cursing anyone who sneezes.",
    "The Wailing Corridor": "The walls cry, complain, and occasionally snicker at you.",
    "Damp Mausoleum": "Moist, moldy, and mildly offended by your presence.",
    "Fleshbound Cellar": "The walls breathe… mostly to mock your panic.",
    "Necromancer's Study": "Skulls, feathers, and bad decisions float lazily in candlelight.",
    "Vampire's Lounge": "Velvet chairs, stale wine, and a hint of existential dread.",
    "Ghastly Pantry": "Spoiled cheese sighs sadly when opened.",
    "Cryptic Nursery": "Rattles echo, rocking chairs move themselves, babies are optional.",
    "Coffin Corridor": "Line up, lie down, and try not to join permanently.",
    "Skeletal Spa": "Steam rises, bones creak, relaxation is mandatory.",
    "Mad Altar": "Candles scream when lit, incense argues with your nose.",
    "Rusty Dungeon": "Chains rattle like sarcastic applause.",
    "Goblin's Restroom": "It smells worse than any curse could describe.",
    "Infernal Kitchen": "Cooking utensils attempt self-defense.",
    "Plague Cellar": "The rats wear tiny masks. You should too.",
    "Weeping Library": "Books cry for attention, mostly yours.",
    "Cursed Throne": "Sit if you dare, get judgment in return.",
    "Fungus Ballroom": "Mold waltzes elegantly, spores applause.",
    "Specter's Closet": "Hangers float, coats whisper secrets you didn’t ask for.",
    "Bloody Pantry": "Ingredients scream when touched, and some might bite.",
    "Ghoul Gym": "Weights lift themselves and mock your weak arms.",
    "Tortured Workshop": "Tools are alive, slightly resentful, and sharp.",
    "Haunted Hallway": "Floors creak and ceilings moan; a classic welcome.",
    "Shadow Kitchen": "Shadows stir the pot, seasoning with spite.",
    "Necrotic Nursery": "Toys move, dolls judge, crib squeaks like a scream.",
    "Corpse Courtyard": "Grass grows over bones, giving it a chic aesthetic.",
    "Eternal Cellar": "Every step downward feels like a decade.",
    "Ghastly Gallery": "Paintings stare… and occasionally wink at your misery.",
    "Wraith Workshop": "Ghostly hands fix broken things… poorly.",
    "Vile Vault": "Treasure gleams, curses gleam brighter.",
    "Plagued Pantry": "Ingredients rot faster than your hope.",
    "The Murmuring Chamber": "Whispers and giggles, mostly at your expense.",
    "Bone Attic": "Dusty skulls line the walls, judging your taste in decor.",
    "Rotting Study": "Books smell like despair and mildew.",
    "Eerie Alcove": "Shadows gather here for tea and idle gossip.",
    "Flesh Garden": "Plants seem to twitch when you blink.",
    "Spectral Hall": "Ghosts politely step aside… sometimes."
}

# initial dictionary for junk_item names and description
junk_items = {
    "Rusty Teapot": "Once boiled water, now mostly memories and rust flakes.",
    "Moth-Eaten Cloak": "Guaranteed to add at least two ghostly inches to your silhouette.",
    "Broken Pocket Watch": "Time travels here, but only backwards.",
    "Old Boots": "Odor adds +2 intimidation, style -5.",
    "Cracked Goblet": "Holds liquids, though it might pour them into another dimension.",
    "Foul Candle": "Burns slowly… and complains the entire time.",
    "Dusty Teacup": "Holds tea, dust, and existential disappointment.",
    "Rusty Spoon": "Perfect for stirring potions… or grudges.",
    "Cracked Mirror": "Shows what you fear most: unpaid taxes and spiders.",
    "Soggy Scroll": "Contains a prophecy… or just soggy paper.",
    "Cobwebbed Bottle": "Contains liquid… or dreams. Hard to tell.",
    "Tiny Cage": "Holds… something, but nobody wants to find out.",
    "Mismatched Socks": "A fashion statement, possibly cursed.",
    "Old Shoe": "Smells of adventure and regret.",
    "Faded Banner": "Once heralded greatness, now mostly mildew."
}

# initial dictionary for normal_item names and description
normal_items = {
    "Faded Map": "Shows somewhere you’ve never wanted to go… probably.",
    "Tarnished Locket": "Holds memories… mostly regret and dust.",
    "Porcelain Doll Head": "Eyes follow you. Not creepy at all.",
    "Tiny Music Box": "Plays tunes of sorrow with a hint of sarcasm.",
    "Cracked Compass": "Always points somewhere vaguely ominous.",
    "Patchwork Hat": "Adds +1 style, -3 dignity.",
    "Jar of Glowworms": "Tiny light bulbs with an attitude problem.",
    "Tattered Diary": "Someone’s embarrassing secrets, minus context.",
    "Skeletal Key": "Opens a lock… eventually. Or just mocks you.",
    "Miniature Chair": "For fairies, or really cruel pets.",
    "Glass Eye": "Someone lost one, now it’s your problem.",
    "Faintly Glowing Rock": "Mildly magical, mostly judgmental.",
    "Jar of Pickled Eyeballs": "Oddly flavored, and slightly judgmental.",
    "Faded Banner": "Once waved in glory, now mostly mildew.",
    "Cracked Goblet": "Holds liquids… occasionally something interesting."
}

# initial dictionary for high_value_item names and description
high_value_items = {
    "Phoenix Feather": "Warm to the touch and slightly judgmental.",
    "Elixir of Forgetfulness": "Makes you forget… minor regrets or tax debts.",
    "Cursed Coin": "Worth more than it should… at a cost.",
    "Miniature Dragon Skull": "Ages well, looks terrifying, slightly valuable.",
    "Potion of Eternal Bubblegum": "Chews forever… or until reality breaks.",
    "Ring of Mild Inconvenience": "Annoys foes subtly; priceless to collectors.",
    "Gilded Teaspoon": "Shiny enough to blind a greedy merchant.",
    "Spectral Candle": "Burns without wax, scent of existential dread included.",
    "Vial of Moonlight": "Captures light that refuses to stay in bottles.",
    "Ancient Music Box": "Plays the lament of a king nobody remembers.",
    "Obsidian Dice": "Roll them and gamble with fate itself.",
    "Golden Feather Quill": "Writes stories that sometimes come true.",
    "Enchanted Snail Shell": "Slowly reveals secrets to those patient enough.",
    "Crystal Jar of Whispering Winds": "Contains voices of forgotten adventurers.",
    "Bag of Trickster Dust": "Makes a mess, causes laughter, and occasionally wealth."
}

# initial dictionary for trash quality weapon names and description
simple_weapons = {
    "Rusty Dagger": "Sharp-ish, mostly rusty, probably tetanus-certified.",
    "Cracked Sword": "Cuts slightly better than wet noodles.",
    "Wooden Club": "Solid, heavy, and smells faintly of regret.",
    "Bent Spear": "Thrown once, bent forever, still kind of useful.",
    "Splintered Stick": "Primitive, yet disturbingly effective.",
    "Broken Shovel": "For digging graves or faces, your choice.",
    "Iron Pipe": "Simple, effective, slightly dented.",
    "Jagged Knife": "Cuts worse than it looks… mostly skin.",
    "Knotted Whip": "Hits like a rope, occasionally like a fist.",
    "Shattered Chair Leg": "Improvise, adapt, survive, or just trip."
}

# initial dictionary for crafted quality weapon names and description
crafted_weapons = {
    "Rusty Mace": "Guaranteed to dent something, maybe your ego.",
    "Chipped Axe": "Cuts wood, maybe a toe.",
    "Spiked Shield": "Defensive until you hit yourself with it.",
    "Heavy Chain": "Good for swinging, dragging, or tripping enemies.",
    "Blunted Hammer": "Hits hard, leaves bruises, not pride.",
    "Spiked Flail": "Swings unpredictably; exciting for all nearby.",
    "Wooden Staff": "Martial arts optional, bruising guaranteed.",
    "Iron Rod": "Pointy enough for persuasion, blunt enough for threats.",
    "Jagged Club": "Handcrafted pain with a hint of malice.",
    "Reinforced Bat": "Extra nails, extra bruises, extra regret."
}

# initial dictionary for legendary quality weapon names and description
legendary_weapons = {
    "Masterwork Longsword": "Shiny, balanced, slightly judgmental of amateurs.",
    "Polished Warhammer": "Blows that make statues nervous.",
    "Engraved Battle Axe": "Cuts with style and a hint of ego.",
    "Spiked Morningstar": "Rolls into combat like a little doom.",
    "Knightly Halberd": "For those who like pointy things at a distance.",
    "Ornate Flanged Mace": "Looks fancy, hits messy.",
    "Reinforced Iron Club": "Simple yet terrifyingly efficient.",
    "Weighted Quarterstaff": "For disciplined strikes and dramatic flair.",
    "Hand-Forged Dagger": "Sharp, elegant, slightly smug.",
    "Veteran’s Polearm": "Old, seasoned, and dangerously opinionated."
}

# initial dictionary for fodder monster names and description
fodder_monsters = {
    "Rotrat": "Half decayed, half alive, fully disgusting.",
    "Mold Goblin": "Throws moldy bread instead of knives.",
    "Bone Cricket": "Chirps loud enough to ruin stealth, not much else.",
    "Slime Blob": "Jiggles menacingly, smells like wet socks.",
    "Dust Skeleton": "Falls apart if you sneeze too hard.",
    "Rotting Bat": "Flies in circles, forgets why halfway.",
    "Gutter Imp": "Steals shoes, laughs way too loud about it.",
    "Gnawed Ghoul": "Half-eaten, but still annoyingly persistent.",
    "Crawling Hand": "Five fingers, zero manners.",
    "Rust Beetle": "Eats armor faster than adventurers.",
    "Torch Moth": "Suicidally in love with your torch.",
    "Shrieking Rat": "Makes more noise than actual damage.",
    "Corpse Worm": "Lives in corpses, visits unexpectedly.",
    "Broken Puppet": "Wooden limbs, creaky insults.",
    "Ash Lizard": "Falls apart into dust when slapped.",
    "Feral Dog": "Mangy, growly, mildly bitey.",
    "Drunk Goblin": "Trips on own weapon more than yours.",
    "Paper Skeleton": "Rattles loudly, folds poorly.",
    "Rotfly": "Buzzes in your ear until rage sets in.",
    "Hungry Shade": "Barely visible, always asking for snacks."
}

# initial dictionary for boss monster names and description
boss_monsters = {
    "Lord Carrion": "A regal corpse king who smells worse than he rules.",
    "The Maw of Ashes": "A giant beast whose cough sets rooms on fire.",
    "Mad Jester Varrox": "Laughs, juggles skulls, kills between punchlines.",
    "Bone Colossus": "A walking pile of skeletons arguing who’s in charge.",
    "The Butcher Priest": "Blesses victims with his cleaver… repeatedly.",
    "Widow Silkskin": "A spider the size of a house with a flair for weaving corpses.",
    "Ghoul General": "Commands rotting troops with military disappointment.",
    "The Rust Tyrant": "A knight whose armor is more fungus than metal.",
    "Eternal Warden": "Guards a door no one asked to open.",
    "The Hollow King": "Wears a crown of teeth, speaks in echoes of despair."
}

# initial list of potential death quotes for all mobs (no difference between fooder/boss mobs)
death_quotes = [
    "lets out a dramatic scream and immediately regrets the performance.",
    "explodes into confetti… of bones.",
    "coughs politely before collapsing into a heap.",
    "whispers: 'tell my rats… I loved them.'",
    "trips over its own corpse on the way down.",
    "vanishes in a puff of dust, leaving only disappointment.",
    "lets out a final burp that smells suspiciously like despair.",
    "hisses one last insult before choking on it.",
    "claps sarcastically, then dies.",
    "melts into a puddle that spells 'oops'.",
    "drops dramatically, as if auditioning for theater.",
    "screams 'I’ll be back!' — it won’t.",
    "turns into smoke that smells like old socks.",
    "gives you the finger… literally.",
    "lets out a fart so powerful it echoes in the void.",
    "tries to say something important but sneezes to death instead.",
    "collapses and whispers: 'worth it… not really.'",
    "turns into dust bunnies that scatter quickly.",
    "salutes you, then faceplants ungracefully.",
    "leaves behind nothing but awkward silence."
]

merchants = {
    "Gregor the Generous": "Sells you back the loot he stole from your corpse last run.",
    "Old Man Ash": "Offers potions that heal, or explode. He won’t say which.",
    "Madame Chains": "Her discounts are great—if you survive the fine print.",
    "Toothless Varric": "Chews on his wares before selling them. Claims it adds flavor.",
    "Sister Mercy": "Blessed your sword… now it screams at night.",
    "Rotgut Rick": "Specializes in food that kills hunger and sometimes the eater.",
    "Phantom Pete": "Takes your gold. Nobody remembers ever getting an item.",
    "The Twins": "Two heads, one purse. Always arguing about the price.",
    "Hollow Jack": "Sells lanterns. All cursed. All still somehow sold out.",
    "Lady Spite": "Her smiles cost extra. Her insults are free."
}


def calculate_item_value(type_treasure: str) -> int:
    """
    Calculate the item value for treasures to be sold later on.
    Function is later on used in create_treasure function

    :param type_treasure: Reference to dict above to select item "quality"
    :return: value (int) for each item stored in a variable
    """
    if type_treasure == "junk":
        value = random.randint(1, 10)
        return value
    elif type_treasure == "normal":
        value = random.randint(11, 25)
        return value
    elif type_treasure == "high_value":
        value = random.randint(75, 100)
        return value
    else:
        print("Unknown treasure type")



def create_treasure(treasure_list: dict, type_treasure: str) -> Item:
    """Create a treasure item based on a given treasure type and list.

    :param treasure_list: Dictionary mapping item names to their descriptions.
    :type treasure_list: dict
    :param type_treasure: The type of treasure to generate, used for value calculation.
    :type type_treasure: str
    :returns: A newly created Item object with name, description, type, and calculated value.
    :rtype: Item
    """
    value = calculate_item_value(type_treasure)
    name, description = random.choice(list(treasure_list.items()))
    new_item = Item(name, "item", description, value)
    return new_item


def generate_treasure_pool(target_item_pool: list) -> list:
    """Generate a pool of treasure items, including junk, normal, and high-value items.

    :param target_item_pool: List to which generated treasure items will be appended.
    :type target_item_pool: list
    :returns: The updated list containing all generated treasure items.
    :rtype: list
    """
    junk_item_count = 0
    normal_item_count = 0
    high_value_item_count = 0

    while junk_item_count < 10:
        junk_item_count += 1
        new_junk_treasure = create_treasure(junk_items, "junk")
        target_item_pool.append(new_junk_treasure)

    while normal_item_count < 5:
        normal_item_count += 1
        new_normal_treasure = create_treasure(normal_items, "normal")
        target_item_pool.append(new_normal_treasure)

    while high_value_item_count < 3:
        high_value_item_count += 1
        new_high_value_treasure = create_treasure(high_value_items, "high_value")
        target_item_pool.append(new_high_value_treasure)
    return target_item_pool


def calculate_weapon_ap_and_value(weapon_quality: str) -> tuple[int, int]:
    """Calculate the attack power and value of a weapon based on its quality.

    :param weapon_quality: The quality tier of the weapon (e.g., "simple", "crafted", "legendary").
    :type weapon_quality: str
    :returns: A tuple containing the weapon's attack power and its value.
    :rtype: tuple[int, int]
    """
    if weapon_quality == "simple":
        attack_power = random.randint(1,5)
        value = random.randint(1,3)
        return attack_power, value
    elif weapon_quality == "crafted":
        attack_power = random.randint(3, 7)
        value = random.randint(5, 10)
        return attack_power, value
    elif weapon_quality == "legendary":
        attack_power = random.randint(10, 15)
        value = random.randint(100, 300)
        return attack_power, value
    else:
        raise ValueError(f"Unknown weapon quality: {weapon_quality}")

def create_weapon(weapon_list: dict, weapon_quality: str) -> Weapon:
    ap, value = calculate_weapon_ap_and_value(weapon_quality)
    name, description = random.choice(list(weapon_list.items()))
    new_weapon = Weapon(name, "weapon", description, value, ap)
    return new_weapon

def generate_weapon_pool(target_weapon_pool: list) -> list:
    simple_weapons_count = 0
    crafted_weapons_count = 0
    legendary_weapons_count = 0

    while simple_weapons_count < 5:
        simple_weapons_count += 1
        new_simple_weapon = create_weapon(simple_weapons, "simple")
        target_weapon_pool.append(new_simple_weapon)

    while crafted_weapons_count < 5:
        crafted_weapons_count += 1
        new_crafted_weapon = create_weapon(crafted_weapons, "crafted")
        target_weapon_pool.append(new_crafted_weapon)

    while legendary_weapons_count < 2:
        legendary_weapons_count += 1
        new_legendary_weapon = create_weapon(legendary_weapons, "legendary")
        target_weapon_pool.append(new_legendary_weapon)
    return target_weapon_pool


def create_room(room_type: str) -> DungeonRoom:
    name, description = random.choice(list(room_names_and_desc.items()))
    new_room = dungeons.DungeonRoom(name, room_type, description)
    return new_room

def generate_dungeon_pool(target_pool: list):
    void_room_count = 0
    sphere_room_count = 0
    encounter_room_count = 0

    while void_room_count < 2:
        void_room_count += 1
        new_room = create_room("void")
        target_pool.append(new_room)

    while sphere_room_count < 2:
        sphere_room_count += 1
        new_room = create_room("sphere")
        target_pool.append(new_room)

    while encounter_room_count < 11:
        encounter_room_count += 1
        new_room = create_room("encounter")
        target_pool.append(new_room)

    return target_pool


def assign_encounters_to_rooms(encounter_pool: list[chars.Monster], room_pool: list[dungeons.DungeonRoom]):
    valid_rooms = [room for room in room_pool if room.type_ == "encounter"]

    for encounter in encounter_pool:
        available_rooms = [room for room in valid_rooms if not room.entities]

        if not available_rooms:
            break

        selected_room = random.choice(available_rooms)
        selected_room.entities.append(encounter)

    return room_pool


def create_merchant():
    name, description = random.choice(list(merchants.items()))
    new_merchant = chars.Trader(name, "merchant", description)
    return new_merchant


def create_fodder_monster():
    name, description = random.choice(list(fodder_monsters.items()))
    base_ap, base_defense, base_hp = chars.calculate_base_stats_monsters()
    new_death_msg = random.choice(death_quotes)
    new_monster = chars.Monster(name, "monster", base_ap, base_defense, base_hp, new_death_msg)
    return new_monster

def create_boss_monster():
    name, description = random.choice(list(boss_monsters.items()))
    base_ap, base_defense, base_hp = chars.calculate_base_stats_bosses()
    new_death_msg = random.choice(death_quotes)
    new_boss = chars.Monster(name, "boss", base_ap, base_defense, base_hp, new_death_msg)
    return new_boss

def generate_encounter_pool(target_pool: list) -> list:
    fodder_count = 0
    boss_count = 0

    while fodder_count < 8:
        fodder_count += 1
        new_fodder_monster = create_fodder_monster()
        target_pool.append(new_fodder_monster)

    while boss_count < 2:
        boss_count += 1
        new_boss = create_boss_monster()
        target_pool.append(new_boss)

    new_merchant = create_merchant()
    target_pool.append(new_merchant)
    return target_pool


def generate_first_chunk(source_dungeon_pool, extension_x) -> list:
    first_chunk = []
    possible_first_room = [room for room in source_dungeon_pool if room.type_ == "sphere"]

    selected_first_room = random.choice(possible_first_room)
    first_chunk.append(selected_first_room)
    source_dungeon_pool.remove(selected_first_room)

    for _ in range(extension_x - 1):
        selected_other_room = random.choice(source_dungeon_pool)
        first_chunk.append(selected_other_room)
        source_dungeon_pool.remove(selected_other_room)

    return first_chunk

def generate_other_chunks(source_dungeon_pool, extension_x):
    new_chunk = []
    for _ in range(extension_x):
        selected_room = random.choice(source_dungeon_pool)
        new_chunk.append(selected_room)
        source_dungeon_pool.remove(selected_room)
    return new_chunk


def generate_map(target_map, source_dungeon_pool, extension_x, extension_y):
    first_chunk = generate_first_chunk(source_dungeon_pool, extension_x)
    target_map.append(first_chunk)

    for _ in range(extension_y-1):
        new_chunk = generate_other_chunks(source_dungeon_pool, extension_x)
        target_map.append(new_chunk)

    return target_map

def render_map(target_map):
    symbols = {
        "sphere": "🔵",
        "encounter": "☠️",
        "void": "⬛"
    }
    for chunk in target_map:
        line = []
        for room in chunk:
            if hasattr(room, "type_"):
                line.append(symbols.get(room.type_))
        print(" ".join(line))


# Simple test area, everything after this line is going to vanish in future updates

print("---ITEM POOL---")
new_item_pool = []
generate_treasure_pool(new_item_pool)
print(new_item_pool)
print(f"COUNTED ITEMS IN POOL: {len(new_item_pool)}")


print("---WEAPON POOL---")
new_weapon_pool = []
generate_weapon_pool(new_weapon_pool)
print(new_weapon_pool)
print(f"COUNTED WEAPONS IN POOL: {len(new_weapon_pool)}")

print("---MONSTER POOL---")
new_encounter_pool = []
generate_encounter_pool(new_encounter_pool)
print(new_encounter_pool)
print(f"COUNTED MONSTERS/ENCOUNTERS IN POOL: {len(new_encounter_pool)}")


print("---NEW ROOM POOL---")
new_dungeon_pool = []
generate_dungeon_pool(new_dungeon_pool)
assign_encounters_to_rooms(new_encounter_pool, new_dungeon_pool)
print(new_dungeon_pool)

print("--------------------------------------------------------------------------------")
print("------------------------ NEW MAP GENERATION IS IMMANENT ------------------------")
new_map = []
print("Empty Map exists")
generate_map(new_map, new_dungeon_pool, 5, 3)
print(new_map)
render_map(new_map)
