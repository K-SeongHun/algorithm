import sys

N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
DP = [
