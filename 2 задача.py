with open('input.txt', 'r') as file_input:
    n = int(file_input.read())
fib = [0, 1]
for i in range(2, n + 1):
    fib.append(fib[-1] + fib[-2])
with open('output.txt', 'w') as file_output:
    file_output.write(str(fib[n]))
