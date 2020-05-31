# 循环: while循环， for循环

# while循环，从1累加到100
i = 1
result_while = 0
while i <= 100:
    result_while += i
    i += 1
print(f'result_while=: {result_while}')

# for循环，从1累加到50
result_for = 0
for i in range(1, 101):
    result_for += i
print(f'result_for=: {result_for}')
