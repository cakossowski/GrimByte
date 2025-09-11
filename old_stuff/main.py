import generator
import chars
from movement import check_target_destination, move_player_to_target_destination
import time

# initialize empty lists for pool creation
item_pool = []
weapon_pool = []
encounter_pool = []
dungeon_pool = []
new_map = []


def main():

    # part of initial generation
    print("""
    Willkommen bei GrimByte, Abenteuerer! Du befindest dich gerade am Anfang deiner kleinen Reise.
    Wir haben nicht mit deiner überraschenden Ankunft gerechnet und müssen noch ein paar Dinge vorbereiten.
    Bitte warte solange, wir informieren dich über den Stand der Vorbereitungen!
    """)
    time.sleep(5)
    generator.create_pools_for_startup(item_pool, weapon_pool, encounter_pool, dungeon_pool)
    print("Die zauberhaften Schätze die du finden kannst existieren jetzt!")
    time.sleep(5)
    print("Es gibt Waffen mit denen du dich verteidigen kannst!")
    time.sleep(3)
    print("Wir wissen jetzt welche Wesen dir unterwegs begegnen werden!")
    time.sleep(3)
    print("Wir haben ein paar schöne Räume aus den Kisten gekramt die du erkunden musst!")
    time.sleep(3)
    generator.generate_map(new_map, dungeon_pool, 5, 3)
    print("Elementarmagie sei dank - wir können die alten karten jetzt entziffern und haben die Welt erschaffen die du betreten wirst.")
    time.sleep(2)
    # generator.render_map_overall(new_map)

    # create player
    player_name = input("Wie willst du während dieser Reise genannt werden? \n")
    new_player = chars.PlayerChar(player_name, "player", 100, 5, 5, 1)

    new_map[0][0].entities.append(new_player)
    new_map[0][0].visited = True
    time.sleep(2)
    print(f"{player_name} - wir haben dich direkt in dein Abenteuer geworfen, es geht los! Es gibt nichts zu befürchten...")
    time.sleep(2)

    # main loop
    while True:
        command = input("> ").strip().lower().split()
        cmd = command[0]
        arg = command[1]



        target = input("Direction: \n")
        new_position = check_target_destination(new_player, target, new_map)
        if new_position:
            move_player_to_target_destination(new_player, new_position, new_map)

        if target == "render":
            generator.render_map_for_player(new_map)




if __name__ == "__main__":
    main()