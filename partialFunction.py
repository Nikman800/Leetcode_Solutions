#!/bin/python3

import math
import os
import random
import re
import sys
from typing import Callable


def compute(*args, **kwargs):
    if kwargs["operation"] == "add":
        return sum(args)
    elif kwargs["operation"] == "max":
        return max(args)
    elif kwargs["operation"] == "min":
        return min(args)
    else:
        return -1

#
# Complete the 'partial' function below.
#
# The function is expected to return an FUNCTION.
# The function accepts 3 parameters, func: Function, args, and kwargs.
#

def partial(func: Callable, *args, **kwargs) -> Callable:
    def new_func(*new_args, **new_kwargs):
        combined_args = args + new_args
        combined_kwargs = {**kwargs, **new_kwargs}
        return func(*combined_args, **combined_kwargs)
        
    return new_func
            
    
if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    operation_in = input()

    result = partial(compute, operation=operation_in)

    for _ in range(n - 1):
        arguments = list(map(int, input().rstrip().split()))
        result = partial(result, *arguments)

    arguments = list(map(int, input().rstrip().split()))

    fptr.write(str(result(*arguments)) + "\n")

    fptr.close()
