def check_move(coord, flag):
    global a
    if flag:
        return conver_coord(coord)
    else:
        b = input("Enter the Coordinates: ").split()
        is_it = is_possible(b)
        good_one = check_move(b, is_it)
        return good_one


def is_possible(aux):  # aux[]
    #global a
    aux2 = conver_coord(aux)
    if len(aux) != 2:
        print("You should enter numbers!")
        return False
    elif int(aux[0]) > 3 or int(aux[0]) < 1 or int(aux[1]) > 3 or int(aux[1]) < 1:
        print("Coordinates should be from 1 to 3!")
        return False
    elif a[aux2] != '_':
        print("This cell is occupied! Choose another one!")
        return False
    return True


def conver_coord(aux):
    numb_position = 0
    a0 = int(aux[0])
    a1 = int(aux[1])
    if a0 == 1:
        if a1 == 1:
            numb_position = 6
        elif a1 == 2:
            numb_position = 3
        else:
            numb_position = 0
    elif a0 == 2:
        if a1 == 1:
            numb_position = 7
        elif a1 == 2:
            numb_position = 4
        else:
            numb_position = 1
    else:
        if a1 == 1:
            numb_position = 8
        elif a1 == 2:
            numb_position = 5
        else:
            numb_position = 2
    return numb_position


def print_table():
    print("---------")
    print("| " + a[0] + " " + a[1] + " " + a[2] + " |")
    print("| " + a[3] + " " + a[4] + " " + a[5] + " |")
    print("| " + a[6] + " " + a[7] + " " + a[8] + " |")
    print("---------")


a = ['_' for p in range(9)]  #Begining
print_table()
turns = 1

while True:
    if turns % 2 == 1:
        X_turn = check_move([], False)
        a[X_turn] = 'X'
    else:
        O_turn = check_move([], False)
        a[O_turn] = 'O'
    print_table()
    output = ""
    exes = 0
    ous = 0
    dashes = 0
    row = ""

    for x in a:
        if x == "X":
            exes += 1
        elif x == "O":
            ous += 1
        else:
            dashes += 1

    if abs((exes - ous)) >= 2:
        output = "Impossible"
        break
    else:
        has_won_X = ((a[0] == a[1] == a[2] == "X")
                     or (a[3] == a[4] == a[5] == "X")
                     or (a[6] == a[7] == a[8] == "X")
                     or (a[0] == a[3] == a[6] == "X")
                     or (a[1] == a[4] == a[7] == "X")
                     or (a[2] == a[5] == a[8] == "X")
                     or (a[0] == a[4] == a[8] == "X")
                 or (a[2] == a[4] == a[6] == "X"))
        has_won_O = (a[0] == a[1] == a[2] == "O"
                 or a[3] == a[4] == a[5] == "O"
                 or a[6] == a[7] == a[8] == "O"
                 or a[0] == a[3] == a[6] == "O"
                 or a[1] == a[4] == a[7] == "O"
                 or a[2] == a[5] == a[8] == "O"
                 or a[0] == a[4] == a[8] == "O"
                 or a[2] == a[4] == a[6] == "O")
        if has_won_O == has_won_X == True:
            output = "Impossible"
            break
        elif has_won_X:
            output = "X wins"
            break
        elif has_won_O:
            output = "O wins"
            break
        elif dashes == 0:
            output = "Draw"
            break
        else:
            output = "Game not finished"
    turns += 1

print(output)
