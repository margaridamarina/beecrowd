t=int(input().strip())
for _ in range(t):
    maze=[]
    while len(maze)<5:
        s=input().strip()
        if not s:
            continue
        maze.append(list(map(int,s.split())) if ' ' in s else [int(ch) for ch in s])
    vis=[[False]*5 for _ in range(5)]
    if maze[0][0]==0:
        q=[(0,0)]
        vis[0][0]=True
        idx=0
        while idx<len(q):
            r,c=q[idx];idx+=1
            if r==4 and c==4:
                break
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr,nc=r+dr,c+dc
                if 0<=nr<5 and 0<=nc<5 and maze[nr][nc]==0 and not vis[nr][nc]:
                    vis[nr][nc]=True
                    q.append((nr,nc))
    print("COPS" if vis[4][4] else "ROBBERS")
