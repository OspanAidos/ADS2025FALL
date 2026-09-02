import sys
import math
input = sys.stdin.readline()
if input:
    a, b = map(int, input.split())
    print(math.gcd(a, b))