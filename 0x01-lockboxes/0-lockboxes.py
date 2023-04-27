#!/usr/bin/python3
""" LockBoxes Challenge """


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    """
    box_len = len(boxes)  # get total number of boxes
    keys = boxes[0][:]  # initialised list to store availabe keys
    box_list = {}  # dictionary to keep track of each box's unlock status
    count = 0  # unlock cycle counter
    pending = 0  # tracker for unopened boxes

    while (count < (box_len - pending)):
        x = 1  # initialise the box index for the next cycle
        while (x < box_len):
            if x in keys:
                box_list[f'{x}'] = True  # set box status
                for key in boxes[x]:
                    if key not in keys:  # if same key was not added earlier
                        keys.append(key)
            else:
                box_list[f'{x}'] = False  # set box status
                pending += 1
            x += 1  # increment the index
        count += 1  # increment the unlock cycle counter
        if pending == 0:  # if all boxes get unlocked after first cycle
            break

# Checking the box status after running all unlock attempts
    for status in box_list.values():
        if status is False:
            return False  # One ore more boxes can not be opened
    return True  # All the boxes can be opened
