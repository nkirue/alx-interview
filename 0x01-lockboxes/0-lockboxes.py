#!/usr/bin/python3
'''Working with lockboxes.
'''


def canUnlockAll(boxes):
    '''method that determines if all the boxes can be opened
    '''
    n = len(boxes)
    sen_boxes = set([0])
    unsen_boxes = set(boxes[0]).difference(set([0]))
    while len(unsen_boxes) > 0:
        boxIdex = unsen_boxes.pop()
        if not boxIdex or boxIdex >= n or boxIdex < 0:
            continue
        if boxIdex not in sen_boxes:
            unsen_boxes = unsen_boxes.union(boxes[boxIdex])
            sen_boxes.add(boxIdex)
    return n == len(sen_boxes)
