import sys
lines = sys.stdin.readlines()

max = (0,0)
for idx, val in enumerate(map(int, lines)):
    max = (val, idx+1) if max[0] < val else max

print(max[0], max[1], sep='\n')  