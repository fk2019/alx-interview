#!/usr/bin/python3
"""canUnlockAll method determines if all the boxes can be opened
   First box is always open
"""


def canUnlockAll(boxes):
    """Check if all boxes can be opened"""
    boxes_len = len(boxes)
    opened_boxes = [0]
    for i in opened_boxes:
        for j in boxes[i]:
            if j not in opened_boxes and j < boxes_len:
                opened_boxes.append(j)
    if len(opened_boxes) == boxes_len:
        return True
    return False
