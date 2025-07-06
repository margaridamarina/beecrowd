results = []

while True:
    try:
        N = int(input())
    except EOFError:
        break

    per_day_cost = int(input())
    revenues = [int(input()) for _ in range(N)]

    max_profit = 0
    current = 0
    for r in revenues:
        current += r - per_day_cost
        if current < 0:
            current = 0
        if current > max_profit:
            max_profit = current

    results.append(max_profit)

for p in results:
    print(p)
