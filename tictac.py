
board1 = """
                 TIC-TAC-TOE
     
       
                 |       |       
              1  |   2   |   3    
          -------|-------|-------
                 |       |       
              4  |   5   |   6    
          -------|-------|-------
                 |       |       
              7  |   8   |   9
                 |       |
"""
allowed_chars = ["1","2","3","4","5","6","7","8","9"]
already_played = []

x = "X"
o = "O"
number = 0

#[score]
xscore = {
"123":0,
"456":0,
"789":0,
"147":0,
"258":0,
"369":0,
"159":0,
"357":0,
}

oscore = {
"123":0,
"456":0,
"789":0,
"147":0,
"258":0,
"369":0,
"159":0,
"357":0,
}


def adjust_score(who_score,num):
    if num == "1":
        who_score["123"] += 1
        who_score["147"] += 1
        who_score["159"] += 1
    elif num == "2":
        who_score["123"] += 1
        who_score["258"] += 1
    elif num == "3":
        who_score["123"] += 1
        who_score["357"] += 1
        who_score["369"] += 1
    elif num == "4":
        who_score["147"] += 1
        who_score["456"] += 1
    elif num == "5":
        who_score["159"] += 1
        who_score["456"] += 1
        who_score["357"] += 1
        who_score["258"] += 1
    elif num == "6":
        who_score["456"] += 1
        who_score["369"] += 1
    elif num == "7":
        who_score["789"] += 1
        who_score["147"] += 1
        who_score["357"] += 1
    elif num == "8":
        who_score["789"] += 1
        who_score["258"] += 1
    elif num == "9":
        who_score["789"] += 1
        who_score["369"] += 1
        who_score["159"] += 1

def check_score(who_score,who):
    for combo,score in who_score.items():
        if score >=3:
            print(who,"Wins")
            no_winner = False
            return no_winner
#[/score]


def remove_number(num):
    already_played.append(num)

def check_if_open(num):
    if num in already_played or num not in allowed_chars:
        print("That move is not allowed \n")
        checking = True
        return checking
    elif num not in already_played:
        remove_number(num)  
        checking = False
        return checking
        
def move(num,token):
    if token == x:
            num = input("Player 1, Choose a Square \n")
            return num
    elif token == o:
            num = input("Player 2, Choose a Square \n")
            return num
        

def board_refresh(last_board,next_board,num,token):
    num = str(num)
    next_board = last_board.replace(num,token)
    print(next_board)
    return next_board

no_winner = True
while no_winner == True:

    print(board1)

    checking = True
    while checking:
        board2 = None
        number = move(number,x)
        checking = check_if_open(number)
        if checking == False:
            break
    board2 = board_refresh(board1,board2,number,x)
    adjust_score(xscore,number)
    no_winner = check_score(xscore,x)
    
#-----------------------------------------
    board3 = None    
    checking = True
    while checking:
        number = move(number,o)
        checking = check_if_open(number)
        if checking == False:
            break
    board3 = board_refresh(board2,board3,number,o)
    adjust_score(oscore,number)
    no_winner = check_score(oscore,o)
    if no_winner == False:
        break
#---------------------------------------
    board4 = None
    checking = True
    while checking:
        number = move(number,x)
        checking = check_if_open(number)
        if checking == False:
            break
    board4 = board_refresh(board3,board4,number,x)
    adjust_score(xscore,number)
    no_winner = check_score(xscore,x)
    if no_winner == False:
        break
#--------------------------------------
    board5 = None
    checking = True
    while checking:
        number = move(number,o)
        checking = check_if_open(number)
        if checking == False:
            break
    board5 = board_refresh(board4,board5,number,o)
    adjust_score(oscore,number)
    no_winner = check_score(oscore,o)
    if no_winner == False:
        break
#------------------------------------
    board6 = None
    checking = True
    while checking:
        number = move(number,x)
        checking = check_if_open(number)
        if checking == False:
            break
    board6 = board_refresh(board5,board6,number,x)
    adjust_score(xscore,number)
    no_winner = check_score(xscore,x)
    if no_winner == False:
        break
#-------------------------------------
    board7 = None
    checking = True
    while checking:
        number = move(number,o)
        checking = check_if_open(number)
        if checking == False:
            break
    board7 = board_refresh(board6,board7,number,o)
    adjust_score(oscore,number)
    no_winner = check_score(oscore,o)
    if no_winner == False:
        break
#-------------------------------------
    board8 = None
    checking = True
    while checking:
        number = move(number,x)
        checking = check_if_open(number)
        if checking == False:
            break
    board8 = board_refresh(board7,board8,number,x)
    adjust_score(xscore,number)
    no_winner = check_score(xscore,x)
    if no_winner == False:
        break
#---------------------------------------
    board9 = None
    checking = True
    while checking:
        number = move(number,o)
        checking = check_if_open(number)
        if checking == False:
            break
    board9 = board_refresh(board8,board9,number,o)
    adjust_score(oscore,number)
    no_winner = check_score(oscore,o)
    if no_winner == False:
        break
#--------------------------------------
    board10 = None
    checking = True
    while checking:
        number = move(number,x)
        checking = check_if_open(number)
        if checking == False:
            break
    board10 = board_refresh(board9,board10,number,x)
    adjust_score(xscore,number)
    no_winner = check_score(xscore,x)
    if no_winner == False:
        break
