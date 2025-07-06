import sys,itertools
d=list(map(int,sys.stdin.buffer.read().split()))
o=[]
i=0
while i<len(d):
    n=d[i];m=d[i+1];i+=2
    c=d[i:i+n];i+=n
    seen=set()
    tie=False
    for tpl in itertools.product(range(1,m+1),repeat=n):
        s=sum(ci*ti for ci,ti in zip(c,tpl))
        if s in seen:
            tie=True
            break
        seen.add(s)
    o.append("Lucky Denis!" if not tie else "Try again later, Denis...")
sys.stdout.write("\n".join(o)+"\n")
