niz = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# +---+---+---+
# | 0 | 1 | 2 |
# +---+---+---+
# | 3 | 4 | 5 |
# +---+---+---+
# | 6 | 7 | 8 |
# +---+---+---+


def board():
    print('')
    print(' ', niz[0], '|', niz[1], '|', niz[2], ' ')
    print(u'\u2500' * 13)
    print(' ', niz[3], '|', niz[4], '|', niz[5], ' ')
    print(u'\u2500' * 13)
    print(' ', niz[6], '|', niz[7], '|', niz[8], ' ')
    print('')


def win(player):
    if niz[0] == niz[1] == niz[2] == player:
        return True
    if niz[3] == niz[4] == niz[5] == player:
        return True
    if niz[6] == niz[7] == niz[8] == player:
        return True
    if niz[0] == niz[3] == niz[6] == player:
        return True
    if niz[1] == niz[4] == niz[7] == player:
        return True
    if niz[2] == niz[5] == niz[8] == player:
        return True
    if niz[0] == niz[4] == niz[8] == player:
        return True
    if niz[2] == niz[4] == niz[6] == player:
        return True
    else:
        return False


def game():
    print('Tic Tac Toe!')
    game_won = False
    player = 'X'

    while not game_won:
        board()
        pos = int(input("Player " + player + ": ")) - 1

        if pos > 8 or pos < 0 or niz[pos] != ' ':
            print("Invalid move. Try again.")

        else:
            niz[pos] = player
            if win(player):
                board()
                print(player, ' wins!')
                game_won = True

            elif ' ' not in niz:
                board()
                print('Draw')
                game_won = True

            else:
                player = 'O' if player == 'X' else 'X'


game()
