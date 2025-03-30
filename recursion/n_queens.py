def solveNqueens(n):
    
    ans = []
    board = [[] for i in range(n)]
    s = '.'
    for i in range(n):

        for j in range(n):
            board[i].append(s)
    

    
    solve(0,board,ans,n)
    print(ans)
    
def solve(col,board,ans,n):
    
    if col == n:
        ans.append(board)
        return
    
    for row in range(n):
        if(isSafe(row,col,board,n)):
            board[row][col] = 'Q'   
            solve(col+1,board,ans,n)
            board[row][col] = '.'
            
            
def isSafe(row,col,board,n):
    duprow = row
    dupcol = col
    
    while row >= 0 and col>=0:
        if board[row][col] == 'Q':
            return False
        
        row -= 1
        col -= 1
        
    col = dupcol
    row = duprow
    
    while col >= 0:
        if board[row][col] == 'Q':
            return False
        col -= 1
        
    row = duprow
    col = dupcol
        
    while col>=0 and row<n:
        
        if board[row][col] == 'Q':
            return False
        row += 1
        col -= 1
        
    return True
    


solveNqueens(3)


