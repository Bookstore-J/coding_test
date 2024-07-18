# from collections import deque

# visited = [0] * 100000

# N,K = map(int, input().split())


# def bfs(N, K):
#     cnt = 0 
#     queue = deque([N])
#     visited[N] = cnt
    
#     move = [N-1, N+1, 2*N]
#     while queue:
#         n = queue.popleft()    
#         cnt += 1
        
#         for i in move:
#             if visited[n+i] == 0:
#                 queue.append(n+1)
#                 visited[n+1] = cnt
#                 if n+i == K :
#                     return cnt-1
        
        
# print(bfs(N, K))


from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0<=nx<=MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)
                

MAX = 10 ** 5
dist = [0] * (MAX+1)
n,k = map(int, input().split())

bfs()