import random

end = 100

def checkladder(point):
    if point == 8:
        print('Ladder')
        return 26
    elif point == 21:
        print('Ladder')
        return 82
    elif point == 43:
        print('Ladder')
        return 77
    elif point == 50:
        print('Ladder')
        return 91
    elif point == 54:
        print('Ladder')
        return 93
    elif point == 62:
        print('Ladder')
        return 96
    elif point == 66:
        print('Ladder')
        return 87
    elif point == 80:
        print('Ladder')
        return 100
    else:
        # no ladder
        return point

def check_snake(point):
    if point == 44:
        print('Snake')
        return 22
    elif point == 46:
        print('Snake')
        return 5 
    elif point == 48:
        print('Snake')
        return 9
    elif point == 52:
        print('Snake')
        return 11
    elif point == 55:
        print('Snake')
        return 7
    elif point == 59:
        print('Snake')
        return 17
    elif point == 64:
        print('Snake')
        return 36
    elif point == 69:
        print('Snake')
        return 33
    elif point == 73:
        print('Snake')
        return 1
    elif point == 83:
        print('Snake')
        return 19
    elif point == 92:
        print('Snake')
        return 51
    elif point == 95:
        print('Snake')
        return 24  
    elif point == 98:
        print('Snake')
        return 28 
    else:
        # no snake
        return point

def reached_end(point):
    if point == end:
        return True
    else:
        return False
def play():

    #input player 1 name
    ply_1 = input("Player 1, Enter your name : ")

    #input player 2 name
    ply_2 = input("PLayer 2, Enter your name : ")

    #player 1 initial point
    pp1 = 0

    #player 2 initial point 
    pp2 = 0

    turn = 0

    while(1):
        if turn%2 == 0:
            #player 1 turn
            print(ply_1," your turn") 

            # ask player choice to continue
            c = int(input("Press 1 for continue ,0 for quit "))
            if c == 0:
                print(ply_1," scored ",pp1)
                print(ply_2," scored ",pp2)
                print('Quiting the game, Thanks for playing ')
                break
            dice = random.randint(1,6) 
            print('Dice showed ',dice)

            pp1 += dice
            pp1 = checkladder(pp1)
            pp1 = check_snake(pp1)

            # check if the player goes beyond the board

            if pp1 > end:
                pp1 = end

            print(ply_1, ' Your score: ',pp1)

            if reached_end(pp1):
                print(ply_1, ' Won')
                break
        else:
            #player 2 turn
            print(ply_2," your turn") 

            # ask player choice to continue
            c = int(input("Press 1 for continue ,0 for quit "))
            if c == 0:
                print(ply_1," scored ",pp1)
                print(ply_2," scored ",pp2)
                print('Quiting the game, Thanks for playing ')
                break
            dice = random.randint(1,6) 
            print('Dice showed ',dice)

            pp2 += dice
            pp2 = checkladder(pp2)
            pp2 = check_snake(pp2)

            # check if the player goes beyond the board

            if pp1 > end:
                pp1 = end

            print(ply_2, ' Your score: ',pp2)

            if reached_end(pp2):
                print(ply_2, ' Won')
                break
        turn += 1
play()