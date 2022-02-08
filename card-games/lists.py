def get_rounds(number):
    """
    takes the current round number and returns a single list with that round and the next two that are coming up

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """

    return [number] + [number + x for x in range(1, 3)]


def concatenate_rounds(rounds_1, rounds_2):
    """
    takes two lists and returns a single list consisting of all the rounds in the first list,
    followed by all the rounds in the second list

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """
    takes two arguments, a list of rounds played and a round number.
    The function will return True if the round is in the list of rounds played, False if not
    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    if number in rounds:
        return True
    else:
        return False


def card_average(hand):
    """
    The average can be found by summing up all the card values and then dividing
    that sum by the number of cards in the hand.
    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    return sum(hand)/len(hand)


def approx_average_is_average(hand):
    """
    Take the average of the first and last number in the hand.
    Using the median (middle card) of the hand.
    Return True if either one or both of the, above named, strategies result in a number equal to the actual average.
    Note: The length of all hands are odd, to make finding a median easier.

    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.
    """

    return (hand[0] + hand[-1])/2 == card_average(hand) or hand[int(len(hand)/2)] == card_average(hand)


def average_even_is_average_odd(hand):
    """
    returns a Boolean indicating if the average of the cards at even indexes
    is the same as the average of the cards at odd indexes.
    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    even = 0
    odd = 0
    for x in range(0, len(hand)):
        if x % 2 == 0:
            even += hand[x]
        else:
            odd += hand[x]

    if len(hand) % 2 == 0:
        even /= len(hand)/2
        odd /= len(hand)/2
    else:
        even /= (int(len(hand)/2) + 1)
        odd /= 1

    return even == odd


def maybe_double_last(hand):
    """
    takes a hand and checks if the last card is a Jack (11). If the the last card is a Jack (11),
    double its value before returning the hand.
    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = 22
        return hand
    else:
        return hand
