import chars
import dungeons

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

    new_x, new_y = new_position
    print(new_position)
    if new_x < 0 or new_y < 0 or new_y > len(current_map):
        print("Your way is blocked - can't move here!")
        return False

    try:
        target_room = current_map[new_y][new_x]
        if not target_room.blocked:
            print(f"You move {target_direction} and enter the next room!")
            return new_position
        else:
            print("Your way is blocked, can't move here!")
            return False
    except IndexError:
        print("Your way is blocked, can't move here!")
        return False


def move_player_to_target_destination(player, target_position, current_map):
    # get current position of player
    current_x, current_y = get_current_position(player)
    # select current room object based on coords of player
    current_room = current_map[current_y][current_x]
    # remove player from selected room
    current_room.entities.remove(player)
    # set new x, y values on basis of target direction, select specific room and append player to it
    new_x, new_y = target_position
    target_room = current_map[new_y][new_x]
    target_room.entities.append(player)
    player.position = target_position
