import sys
from collections import deque
def jbo(boris, nurik):
    moves = 0
    max_moves = 20000
    while boris and nurik and moves <= max_moves:
        moves +=1
        b_card = boris.popleft()
        n_card = nurik.popleft()
        if b_card == 0 and n_card == 9:
            boris.append(b_card)
            boris.append(n_card)
        elif b_card == 9 and n_card == 0:
            nurik.append(b_card)
            nurik.append(n_card)
        elif b_card > n_card:
            boris.append(b_card)
            boris.append(n_card)
        else:
            nurik.append(b_card)
            nurik.append(n_card)
    if not nurik:
        print(f"Boris {moves}")
    elif not boris:
        print(f"Nursik {moves}")
    else:
        print("draw")
b = deque(map(int, sys.stdin.readline().split()))
n = deque(map(int, sys.stdin.readline().split()))
jbo(b, n)