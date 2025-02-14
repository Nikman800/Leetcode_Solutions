#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMaxUnits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY boxes
#  2. LONG_INTEGER_ARRAY unitsPerBox
#  3. LONG_INTEGER truckSize
#

def getMaxUnits(boxes, unitsPerBox, truckSize):
    # paired_lists = list(zip(unitsPerBox, boxes))
    
    # sorted_pairs = sorted(paired_lists)
    
    # unitsPerBox, boxes = zip(*sorted_pairs)
    
    # unitsPerBox = list(unitsPerBox)
    # boxes = list(boxes)

    # unitsPerBox.reverse()
    # boxes.reverse()
    
    # units = 0
    # index = 0
    
    # for i in range(truckSize):
    #     units += unitsPerBox[index]
    #     boxes[index] -= 1
    #     if (boxes[index] <= 0):
    #         index += 1
    #         if index >= len(unitsPerBox):
    #             break
            
    # return units
        
    paired_lists = sorted(zip(unitsPerBox, boxes), reverse=True)
    
    total_units = 0
    
    for units, box_count in paired_lists:
        if truckSize <= 0:
            break
        boxes_to_take = min(box_count, truckSize)
        total_units += units * boxes_to_take
        truckSize -= boxes_to_take
        
    return total_units
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    boxes_count = int(input().strip())

    boxes = []

    for _ in range(boxes_count):
        boxes_item = int(input().strip())
        boxes.append(boxes_item)

    unitsPerBox_count = int(input().strip())

    unitsPerBox = []

    for _ in range(unitsPerBox_count):
        unitsPerBox_item = int(input().strip())
        unitsPerBox.append(unitsPerBox_item)

    truckSize = int(input().strip())

    result = getMaxUnits(boxes, unitsPerBox, truckSize)

    fptr.write(str(result) + '\n')

    fptr.close()
