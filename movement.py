import chars
import dungeons

# TODO Review if function is necessary at current state
def get_current_position(player):
    current_x, current_y = player.position
    return current_x, current_y


def check_target_destination(player, target_direction, current_map):
    x, y = player.position

    if target_direction == "north":
        new_position = (x, y - 1)
        print("You try to move north...")

    elif target_direction == "south":
        new_position = (x, y + 1)
        print("You try to move south...")

    elif target_direction == "west":
        new_position = (x-1, y)
        print("You try to move west...")

    elif target_direction == "east":
        new_position = (x+1, y)
        print("You try to move east...")

    else:
        print("This is not a valid direction - you can only move north, south, west and east!")
        return

    x, y = new_position
    try:
        target_room = current_map[y][x]
        if not target_room.blocked:
            print(f"You move {target_direction} and enter the next room!")
            return True
    except IndexError:
        print("Your way is blocked, can't move here!")
        return False

