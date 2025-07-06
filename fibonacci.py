MAX_X = 39
fib_values = [0] * (MAX_X + 1)
call_counts = [0] * (MAX_X + 1)
fib_values[1] = 1
for i in range(2, MAX_X + 1):
    fib_values[i] = fib_values[i - 1] + fib_values[i - 2]
    call_counts[i] = call_counts[i - 1] + call_counts[i - 2] + 2
N = int(input())
outputs = []
for _ in range(N):
    X = int(input())
    outputs.append(f"fib({X}) = {call_counts[X]} calls = {fib_values[X]}")
print('\n'.join(outputs))