board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(bo):
    for i in range(len(bo)):
        if i % 3  == 0 and i != 0 :
            print("- - - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3  == 0:
                print(" | ", end = "")
            if j == 8:
                print( bo[i][j])
            else:
                print( bo[i][j], end = " ")
    return 

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # row, col
    return False

def Valid(bo, num, row, col):
    for i in range(len(bo[0])):
        if bo[row][i] == num and i != col :
            return False
    
    for i in range(len(bo)):
        if bo[i][col] == num and i != row:
            return False
    
    p_r = row // 3
    p_c = col // 3

    for i in range(p_r*3, p_r*3+3):
        for j in range(p_c*3, p_c*3+3):
            if bo[i][j] == num and (i != row and j != col):
                return False


    return True

def Solve(bo):
    #print(bo)
    Find = find_empty(bo)
    if not Find:
        return True
    else:
        row, col = Find

    
    for i in range(1,10):
        if Valid(bo, i, row, col):
            bo[row][col] = i
            if Solve(bo):
                return True
            bo[row][col] = 0
    

    return False


    




print_board(board)
print(Solve(board))
print("-----------")
print_board(board)