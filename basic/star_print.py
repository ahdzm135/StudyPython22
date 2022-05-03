# * 찍기
for x in range(1, 6):
    for y in range(x, 5):
        print('*', end='')
    print('')

    for y in range(1, x):
        print('x', end='')
    print('')

print('Hello', end= ' ')
print('World')
