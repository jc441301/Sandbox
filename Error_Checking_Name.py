'''check if the name entered is valid, as far as not just blank space.'''


def get_name():
    global name
    name = input("Enter your name here ").strip()
    while len(name) <= 0:
        print("Invalid name ")
        name = input("Enter your name here ").strip()

def grab_letter(n,m):
    for i in range(m-1, len(n), m):
        print('{}'.format(n[i]), end=' ')

get_name()
grab_letter(name,2)
