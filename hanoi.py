MAX = 3600
squares = {i * i for i in range(1, int(MAX ** 0.5) + 1)}

T = int(input())
results = []
for _ in range(T):
    n = int(input())
    pegs = [0] * n
    ball = 1
    while True:
        placed = False
        for i in range(n):                      
            if pegs[i] == 0 or (pegs[i] + ball) in squares:
                pegs[i] = ball
                placed = True
                break
        if not placed:                         
            results.append(ball - 1)
            break
        ball += 1
print('\n'.join(map(str, results)))

