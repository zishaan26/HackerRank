## Python If-Else
## https://www.hackerrank.com/challenges/py-if-else/submissions

import math
import os
import random
import re
import sys

from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    n = int(raw_input().strip())
    if n%2!=0:
        print("Weird")
    else:
        if n in range(2,5,1):
            print("Not Weird")
        elif n in range(6,21,1):
            print("Weird")
        elif n>20:
            print("Not Weird")
        else:
            print("Default")
