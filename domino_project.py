import random


def max_duo(lst):
    m = 0
    l = []
    for i in lst:
        if i[0] == i[1]:
            l.append(i)
            m = max(l)
    return m


all_domino = [[1, 4], [1, 3], [2, 3], [4, 5], [2, 2], [0, 3], [6, 6], [0, 6], [5, 5], [4, 4],
              [4, 6], [0, 1], [0, 5], [1, 6], [2, 5], [1, 2], [3, 6], [0, 0], [0, 2], [5, 6], [3, 5], [2, 4],
              [3, 4], [1, 5], [0, 4], [2, 6], [3, 3], [1, 1]];


def deal(domino):
    dealed = random.sample(domino, 7)
    if not isinstance(max_duo(dealed), int):
        return dealed
    else:
        return deal(domino)


def print_pieces(dominos):
    print("Your pieces:")
    for element in dominos:
        index = dominos.index(element)
        print(str(index + 1) + ':' + str(element))
    print('')


Computer_pieces = deal(all_domino)
rest_domino = [fruit for fruit in all_domino if fruit not in Computer_pieces]
Player_pieces = deal(rest_domino)
Stock_pieces = [fruit for fruit in rest_domino if fruit not in Player_pieces]

# print('Stock pieces: ' + str(Stock_pieces))

x = max_duo(Computer_pieces)
y = max_duo(Player_pieces)

status = ""
z = 0
if x < y:
    z = y
    if z in Player_pieces:
        Player_pieces.remove(z)
    status = "computer"
    # removeMaxDuo(Player_pieces)
else:
    z = x
    if z in Computer_pieces:
        Computer_pieces.remove(z)
    status = "player"
    # removeMaxDuo(Computer_pieces)

# print('Computer pieces: ' + str(Computer_pieces))
# print('player pieces: ' + str(Player_pieces))

domino_snake = [z]
# print('Domino snake: ' + str(domino_snake))

# print('Status: ' + str(status))
print('=' * 70)

print('Stock size: ' + str(len(Stock_pieces)))
print('Computer pieces: ' + str(len(Computer_pieces)))
print('')
print(''.join(map(str,domino_snake)))
print('')

print_pieces(Player_pieces)

# if status == str('computer'):
#     print("Status: Computer is about to make a move. Press Enter to continue...\n>", end=' ')


def get_input():
    value = int(input())
    try:
        val = int(value)
        if abs(val) <= len(Player_pieces):
            return val
        else:
            print("Invalid input. Please try again.\n", end='')
            return get_input()
    except ValueError:
        print("Invalid input. Please try again.\n", end='')
        return get_input()


def is_draw():
    x = domino_snake[0]
    y = domino_snake[-1]
    if x[0] == y[1]:
        counter = 0
        for i in domino_snake:
            if i[0] == x[0]:
                counter += 1
            if i[1] == x[0]:
                counter += 1
        if counter == 8:
            return True


def print_snake():
    if len(domino_snake) > 6:
        print(str(domino_snake[0])+str(domino_snake[1])+str(domino_snake[2]) + '...' + str(domino_snake[-3])+str(domino_snake[-2])+str(domino_snake[-1]))
    else:
        print(''.join(map(str, domino_snake)))


def add_to_beg(domino_to_insert):
    x = domino_snake[0]
    if x[0] == domino_to_insert[1]:
        domino_snake.insert(0, domino_to_insert)
    elif x[0] == domino_to_insert[0]:
        domino_to_insert[0],domino_to_insert[1] = domino_to_insert[1], domino_to_insert[0]
        domino_snake.insert(0, domino_to_insert)
    else:
        print('Illegal move. Please try again.')
        return -1


def add_to_end(domino_to_insert):
    y = domino_snake[-1]
    if y[1] == domino_to_insert[0]:
        domino_snake.append(domino_to_insert)
    elif y[1] == domino_to_insert[1]:
        domino_to_insert[0], domino_to_insert[1] = domino_to_insert[1], domino_to_insert[0]
        domino_snake.append(domino_to_insert)
    else:
        print('Illegal move. Please try again.')
        return -1


def insert_domino():
    global status
    turn = get_input()
    domino_to_insert = Player_pieces[abs(turn) - 1]
    if turn < 0:
        foo = add_to_beg(domino_to_insert)
        if foo == -1:
            insert_domino()
            return
        Player_pieces.remove(domino_to_insert)
    elif turn > 0:
        foo = add_to_end(domino_to_insert)
        if foo == -1:
            insert_domino()
            return
        Player_pieces.remove(domino_to_insert)
    elif turn == 0:
        pieces_to_add = random.choice(Stock_pieces)
        Player_pieces.append(pieces_to_add)
        Stock_pieces.remove(pieces_to_add)
        status = 'computer'


def get_domino_for_computer():
    left = domino_snake[0]
    right = domino_snake[-1]
    for i in Computer_pieces:
        if i[0] == right[1]:
            domino_snake.append(i)
            Computer_pieces.remove(i)
            return
        elif i[1] == left[0]:
            domino_snake.insert(0, i)
            Computer_pieces.remove(i)
            return
        elif i[0] == left[0]:
            i[0], i[1] = i[1], i[0]
            domino_snake.insert(0, i)
            Computer_pieces.remove(i)
            return
        elif i[1] == right[1]:
            i[0], i[1] = i[1], i[0]
            domino_snake.append(i)
            Computer_pieces.remove(i)
            return
    if len(Stock_pieces) == 0:
        return
    else:
        pieces_to_add = random.choice(Stock_pieces)
        Computer_pieces.append(pieces_to_add)
        Stock_pieces.remove(pieces_to_add)



while True:
    if status == str('player'):
        print("Status: It's your turn to make a move. Enter your command.")

        insert_domino()
        print('=' * 70)
        print('Stock size: ' + str(len(Stock_pieces)))
        print('Computer pieces: ' + str(len(Computer_pieces)))
        print('')
        print_snake()
        print('')
        print_pieces(Player_pieces)
        status = str('computer')

    elif status == str('computer'):
        print("Status: Computer is about to make a move. Press Enter to continue...")
        input()
        # n = input()
        # n = random.randint(0, len(Computer_pieces) - 1)
        print('')
        # h = random.choice(Computer_pieces)
        get_domino_for_computer()
        status = str('player')

        print('=' * 70)
        print('Stock size: ' + str(len(Stock_pieces)))

        print('Computer pieces: ' + str(len(Computer_pieces)))
        print('')
        print_snake()
        print('')

        print_pieces(Player_pieces)

    if len(Player_pieces) == 0:
        print('Status: The game is over. You won!')
        break
    elif len(Computer_pieces) == 0:
        print('Status: The game is over. The computer won!')
        break
    elif is_draw():
        print("Status: The game is over. It's a draw!")
        break






