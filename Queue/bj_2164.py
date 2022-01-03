#deque 쓰고 푼 문제
import sys
from collections import deque

n = int(sys.stdin.readline())
q1 = deque([i for i in range(1,n+1)])

while len(q1) > 1:
    q1.popleft()
    q1.append(q1.popleft())
print(*q1)

-----------------------------------------------

#deque 안쓰고 풀어서 시간초과
n = int(input())

q1 = [i for i in range(1,n+1)]

while len(q1) > 1:
    q1.pop(0)
    q1.append(q1.pop(0))
   
print(*q1)