"""
BOJ N1463 1로 만들기
"""

x = int(input())

# 각 정수의 최소 연산 횟수를 저장하는 dp table
d = [0] * 1000001

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

print(d[x])