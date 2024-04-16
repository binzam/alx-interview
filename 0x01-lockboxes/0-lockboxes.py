#!/usr/bin/python3
"""A module for working with lockboxes.
"""


def canUnlockAll(boxes):
    """Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    """
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < num_boxes and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
