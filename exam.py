inst = 1
while True:
    try:
        n, k = map(int, input().split())
    except EOFError:
        break                         
    if n == 0 and k == 0:
        break                         

    names = []
    while len(names) < n:
        names.extend(input().split())

    i = 0
    while i < n and k > 0:
        end = min(i + k, n - 1)     
        min_idx = i
        for j in range(i + 1, end + 1):
            if names[j] < names[min_idx]:
                min_idx = j
        k -= (min_idx - i)             
        names.insert(i, names.pop(min_idx))
        i += 1

    print(f"Instancia {inst}")
    print(' '.join(names) + ' ')      
    print()                            
    inst += 1
