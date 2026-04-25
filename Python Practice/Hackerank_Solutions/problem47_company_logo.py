#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    result = Counter(sorted(s)).most_common(3)
    
    for key, value in result:
        print(key,value)