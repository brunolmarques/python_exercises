EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(t):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - t


def preparation_time_in_minutes(layers):
    """
    Calculates the total preparation time given a number of layers

    :param layers: number of layers in the lasagna
    :return: the total time ti will take to prepare
    """
    return layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculates total time spent so far in preparing the lasagna

    :param number_of_layers: Number of layers used in the lasagna
    :param elapsed_bake_time: How much time the lasagna is cooking in the oven
    :return: Total time spent so far
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
