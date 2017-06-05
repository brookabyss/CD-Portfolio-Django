def checker_board(rows,cols):
    board=[]
    for j in range(0,rows):
        row=[]
        for i in range(0,cols):
            if j%2==0:
                if i%2==0:
                    row+="*"
                else:
                    row+=" "
            else:
                if i%2==0:
                    row+=" "
                else:
                    row+="*"
        board.append(row)
    for i in board:
        s=""
        print s.join(i)
checker_board(7,8)
