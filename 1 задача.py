#1
with open('input.txt', 'r') as file_input:
    a, b = map(int, file_input.read().split())
with open('output.txt', 'w') as file_output:
    file_output.write(str(a + b))
#2
with open('input.txt', 'r') as file_input:
    a, b = map(int, file_input.read().split())
with open('output.txt', 'w') as file_output:
    file_output.write(str(a + b**2))
