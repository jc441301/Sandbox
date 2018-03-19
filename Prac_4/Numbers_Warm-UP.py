
''' * fun little exercise to warm up the fingers before coding.'''
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[0] = 10
numbers[-1] = 1
for i in range(0,len(numbers)):
    print('{}'.format(numbers[i]), end=" ")
print()
for i in range(1, len(numbers)-1):
    print('{}'.format(numbers[i]), end=' ')

if 9 in numbers:
    print('9 is an element of numbers')
else:
    print('9 is NOT an element in numbers')

