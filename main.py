import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
list = []
if not n:
    print("0")
else:
    for i in input().split():
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)
        list.append(t)
    if len(list) == 1:
        print(list[0])

    else:
        b = []
        c = []
        for i in list:
            if i < 0:
                b.append(i)
            else:
                c.append(i)
        if len(b) != 0 and len(c) != 0:
            if max(b) + min(c) == 0:
                print(min(c))
            elif max(b) + min(c) < 0:
                print(min(c))
            else:
                print(max(b))
        elif len(b) == 0 and len(c) != 0:
            print(min(c))
        else:
            print(max(b))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


