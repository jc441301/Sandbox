


import random



def main():
    quick_picks = int(input("how many games do you wish to play?"))
    numbers_played = get_numbers(quick_picks)
    printing_ticket(numbers_played, quick_picks)


def get_numbers(n):
    ticket = []
    for i in range(n):
        game = []
        while len(game) < 6:
            game.append(random.randint(1, 45))
            for k in range(len(game)):
                for j in range(len(game)):
                    if k-1 != j-1 and game[k-1] == game[j-1]:
                            del game[j-1]
        game.sort()
        ticket.append(game)
    return ticket


def printing_ticket(n, m):
    for i in range(len(n)):
        print('{}' .format(n[i], end=' '))
        print()


if __name__ == '__main__':
    main()