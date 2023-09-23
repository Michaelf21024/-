from time import perf_counter_ns
from os import getpid
from psutil import Process



start_time = perf_counter_ns()

with open('input.txt', 'r') as file_input:
    n = int(file_input.read())
fib = [0, 1]
for i in range(2, n + 1):
    fib.append((fib[-1] + fib[-2])%10)
with open('output.txt', 'w') as file_output:
    file_output.write(str(fib[n]))

print('Время выполнения:', (perf_counter_ns() - start_time) / 10 ** 9, 'с')
print('Затраты памяти:', Process(getpid()).memory_info().rss / 1024 ** 2, 'Мб')
