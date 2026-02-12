#!/usr/bin/env python3
import sys

num_params = len(sys.argv) - 1
print(f"parameters: {num_params}")

if len(sys.argv) < 2:
    print("none")
else:
    for i in range(1,len(sys.argv)):
        print(sys.argv[i],": ",len(sys.argv[i]))