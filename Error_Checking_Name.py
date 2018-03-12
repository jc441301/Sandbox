'''check if the name entered is valid, as far as not just blank space.'''

name = input("Enter your name here ").strip()
while len(name) <= 0:
    print("Invalid name ")
    name = input("Enter your name here ").strip()
for i in range(1, len(name), 2):
    print('{}'.format(name[i]), end=' ')