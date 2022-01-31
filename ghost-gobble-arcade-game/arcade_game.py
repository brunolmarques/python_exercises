def eat_ghost(power_pellet_active, touching_ghost):
    """
    Returns a Boolean value if Pac-Man is able to eat the ghost.
    The function should return True only if Pac-Man has a power pellet active and is touching a ghost.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """
    Returns a Boolean value if Pac-Man scored.
    The function should return True if Pac-Man is touching a power pellet or a dot.

    :param touching_power_pellet: bool - does the player have an active power pellet?
    :param touching_dot:  bool - is the player touching a dot?
    :return: bool
    """
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """
    Returns a Boolean value if Pac-Man loses.
    The function should return True if Pac-Man is touching a ghost and does not have a power pellet active.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool
    """
    return not power_pellet_active and touching_ghost


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """
    returns a Boolean value if Pac-Man wins.
    The function should return True if Pac-Man has eaten all of the dots
    and has not lost based on the parameters defined in part 3.

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)
