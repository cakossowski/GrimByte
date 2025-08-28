import chars
import items
import dungeons
import generator

def get_current_position(player: chars.PlayerChar):
    current_x, current_y = player.position
    return current_x, current_y

