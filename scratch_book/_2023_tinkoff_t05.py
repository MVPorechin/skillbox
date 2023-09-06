from collections import deque

n, m = map(int, input().split())
graf = dict()
for g in range(1, m+1):
    u, v, w = map(int, input().split())
    graf[u] = (v, w)


print(graf)