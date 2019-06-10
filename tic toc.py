import random

list = [' '] * 10


def drawBoard(list):
    board = f'''
 _____  _____  _____ 
|      |      |      |      
|  {list[7]}   |  {list[8]}   |  {list[9]}   |
 _____  _____  _____ 
|      |      |      |      
|  {list[4]}   |  {list[5]}   |  {list[6]}   |
 _____  _____  _____ 
|      |      |      |      
|  {list[1]}   |  {list[2]}   |  {list[3]}   |
 _____  _____  _____ '''
    print(board)


def Playerturn(list):
    while True:
        pos = input('\nYour turn choose position between 1 and 9 > ')
        if not pos.isdigit():
            continue
        pos=int(pos)
        if pos >9:
            continue
        if list[pos] != ' ':
            print('\nAlready taken choose another position ')
            continue
        list[pos] = 'X'
        drawBoard(list)
        break


def Win(list):
    while True:
        if list[7] == list[8] == list[9] and list[7] != ' ':
            if list[7] == 'X':
                print('You won ')
            else:
                print('PC won')
            return True
            break
        elif list[4] == list[5] == list[6] and list[4] != ' ':
            if list[4] == 'X':
                print('You won ')
            else:
                print('PC won')
            return True
            break
        elif list[1] == list[2] == list[3] and list[1] != ' ':
            if list[1] == 'X':
                print('You won ')
            else:
                print('PC won')
            return True
            break
        elif list[7] == list[4] == list[1] and list[7] != ' ':
            if list[7] == 'X':
                print('You won ')
            else:
                print('PC won')
            return True
            break

        elif list[8] == list[5] == list[2] and list[2] != ' ':
            if list[2] == 'X':
                print('You won ')
            else:
                print('PC won')
            return True
            break
        elif list[9] == list[6] == list[3] and list[3] != ' ':
            if list[3] == 'X':
                print('You won ')
            else:
                print('PC won')
            return True
            break
        elif list[7] == list[5] == list[3] and list[3] != ' ':
            if list[3] == 'X':
                print('You won ')
            else:
                print('PC won')
            return True
            break
        elif list[9] == list[5] == list[1] and list[1] != ' ':
            if list[1] == 'X':
                print('You won ')
            else:
                print('PC won')
            return True
            break
        elif ' ' not in list[1:]:
            print('Draw ')
            return True
            break
        else:
            return False
            break


def Pcturn(list):
    while True:
        pos = random.randint(1, 9)
        if list[pos] != ' ':
            continue
        print('\nPC turn \n')
        list[pos] = 'O'
        drawBoard(list)
        break


def draw(list):
    win = False
    turn = random.choice(['PC', 'PLAYER'])
    while not win:
        if turn == 'PC':
            Pcturn(list)
            turn='PLAYER'
            if Win(list):
                break
        else:
            Playerturn(list)
            turn='PC'
            if Win(list):
                break


if __name__ == '__main__':
    draw(list)
