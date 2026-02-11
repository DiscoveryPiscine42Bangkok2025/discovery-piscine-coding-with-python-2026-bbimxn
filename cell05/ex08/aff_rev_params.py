import sys

if len(sys.argv) < 3:
    print("none")
else:
    for n in range(len(sys.argv)-1,0,-1):
        print(sys.argv[n])