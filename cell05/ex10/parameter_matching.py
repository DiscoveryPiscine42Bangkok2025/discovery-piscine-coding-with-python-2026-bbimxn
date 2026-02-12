#!/usr/bin/env python3

import sys
print("What was the parameter? ")
parameter = "Sorry"

if len(sys.argv) < 2:
    print("none")
else:
    if sys.argv[1] == parameter:
        print("Good job!")
    else:
        print("Nope,sorry...")