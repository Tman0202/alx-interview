#!/usr/bin/python3
""" LockBoxes Challenge """

def canUnlockAll(boxes):

     """
    determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    """

    n = len(boxes)
    unlocked = set([0])  # first box is unlocked

    # iterate over boxes until no more boxes can be unlocked
    while True:
        new_keys = set()
        for box_idx in unlocked:
            new_keys |= set(boxes[box_idx])

        if not new_keys:
            break

        new_unlocked = new_keys - unlocked
        if not new_unlocked:
            break

        unlocked |= new_unlocked

    # check if all boxes are unlocked
    return len(unlocked) == n
