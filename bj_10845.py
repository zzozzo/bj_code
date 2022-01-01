import sys

que = []


n = int(sys.stdin.readline())

for i in range(n):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == 'push':
        que.append(cmd[1])
        
    elif cmd[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else: 
            print(que.pop(0))

            
    elif cmd[0] == 'size':
        print(len(que))
    
    elif cmd[0] == 'empty':
        if len(que) == 0:
            print(1)
        else: 
            print(0)
    
    elif cmd[0] == 'front':
        if len(que) == 0:
            print(-1)
        else: 
            print(que[0])
    
    elif cmd[0] == 'back':
        if len(que) == 0:
            print(-1)
        else: 
            print(que[-1])   