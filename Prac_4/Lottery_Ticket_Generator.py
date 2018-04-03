import random


def main():
    quick_picks = int(input("how many games do you wish to play?"))
    numbers_played = get_numbers(quick_picks)
    printing_ticket(numbers_played)


def get_numbers(n):
    ticket = []
    for i in range(n):
        game = []
        while len(game) < 6:
            new_number = random.randint(1, 45)
            if new_number not in game:
                game.append(new_number)
        game.sort()
        ticket.append(game)
    return ticket


def printing_ticket(numbers_played):
        for i in range(len(numbers_played)):
            for j in range(len(numbers_played[i])):
                print('{}' .format(numbers_played[j], terminate='\n'))
                print()

if __name__ == '__main__':
    main()