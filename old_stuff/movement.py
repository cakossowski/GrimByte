import chars
import dungeons

def get_current_position(player):
    """
    Get the current position of the player.

    :param player: The player object containing a position attribute.
    :type player: object
    :return: The current (x, y) position of the player.
    :rtype: tuple[int, int]
    """
    current_x, current_y = player.position
    return current_x, current_y


def check_target_destination(player, target_direction, current_map):
    """
    Check if the player can move to the target destination on the current map
    and return the new position if valid.

    :param player: The player object containing the current position.
    :type player: object
    :param target_direction: The direction the player wants to move
        ("north", "south", "west", or "east").
    :type target_direction: str
    :param current_map: The dungeon map represented as a 2D list of rooms.
    :type current_map: list[list[dungeons.DungeonRoom]]
    :return: The new (x, y) position if movement is valid, otherwise False.
    :rtype: tuple[int, int] | bool
    """
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
            target_room.visited = True
            return new_position
        else:
            print("Your way is blocked, can't move here!")
            return False
    except IndexError:
        print("Your way is blocked, can't move here!")
        return False


def move_player_to_target_destination(player, target_position, current_map):
    # TODO new movement implementation needed
    """
    Move the player to the target destination on the current map by updating
    their position and transferring them between rooms.

    :param player: The player object to be moved.
    :type player: object
    :param target_position: The new (x, y) position the player should move to.
    :type target_position: tuple[int, int]
    :param current_map: The dungeon map represented as a 2D list of rooms.
    :type current_map: list[list[dungeons.DungeonRoom]]
    :return: None
    :rtype: None
    """
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
