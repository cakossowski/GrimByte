from states.base_state import BaseState


class Generation(BaseState):
    def __init__(self, game):
        super().__init__(game)
        self.game = game

    def enter(self):
        """ Start generation of items on start """
        pass

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

