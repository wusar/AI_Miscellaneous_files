from board import *

def save(self,chessboard):
    ans=[]
    for i in range(8):
        for j in range(8):
            if chessboard.queenMatrix[i][j]:
                ans.append(j)
    self.solves.append(ans)
    print(ans)

def legalpos(self,x,chessboard):
    if x>=8:
        save(chessboard)
        return False
    chessboard_copy=copy.deepcopy(chessboard)
    for j in range(8):
        if not chessboard.setQueen(x,j,False):
            continue
        if legalpos(x+1,chessboard):
            return True
        else:
            chessboard=copy.deepcopy(chessboard_copy)
            
    return False


chessboard=Chessboard(False)

legalpos(0,chessboard)
        
#chessboard.printChessboard()

