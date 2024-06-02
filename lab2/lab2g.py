#!/usr/bin/env python3

#Author: Raymond Domingo
#AuthorID: rdomingo6
#Date Created: 2024/06/02

import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer != 0:
    print(timer)
    timer = timer -1
print('blast off!')