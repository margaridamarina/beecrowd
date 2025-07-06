import sys,heapq
d=list(map(int,sys.stdin.buffer.read().split()))
r=[]
i=0
while i<len(d):
    n=d[i];h=d[i+1];i+=2
    a=[(d[i+2*j],d[i+2*j+1])for j in range(n)]
    i+=2*n
    a.sort(key=lambda x:x[1])
    q=[]
    s=0
    for v,t in a:
        heapq.heappush(q,v)
        s+=v
        if len(q)>t:
            s-=heapq.heappop(q)
    r.append(str(sum(v for v,_ in a)-s))
sys.stdout.write('\n'.join(r)+'\n')
