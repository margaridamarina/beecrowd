T = int(input().strip())          

for _ in range(T):
    line = input().strip()
    while not line:
        line = input().strip()

    N, C, M = map(int, line.split())

    floors = []
    while len(floors) < M:
        floors.extend(map(int, input().split()))

    floors.sort(reverse=True)      

    energy = 0
    for i in range(0, M, C):      
        energy += 2 * floors[i]   

    print(energy)
