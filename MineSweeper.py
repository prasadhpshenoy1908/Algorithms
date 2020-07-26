class Solution:
    def updateBoard(self, board, click):
        #if clicked on Mine return
        x = click[0]
        y = click[1]
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        else:
            self.dfs(board,x,y)
            return board
    
    def dfs(self, board, xPos,yPos):
        #check boundry conditions
        if xPos < 0 or yPos < 0 or xPos >= len(board) or yPos >= len(board[0]):
            return

        #avoid visiting visited cells
        if board[xPos][yPos] == 'B' or board[xPos][yPos] == '1' or board[xPos][yPos] == '2' or board[xPos][yPos] == '3' or board[xPos][yPos] == '4' or board[xPos][yPos] == '5' or board[xPos][yPos] == '6' or board[xPos][yPos] == '7' or board[xPos][yPos] == '8' or board[xPos][yPos] == '9':
            return
        #check if neighbours have mine. 
        #if neighbours have mines, increment count
        iCount = self.MinesFound(board, xPos, yPos)
        if (iCount) > 0:
            board[xPos][yPos] = iCount
            return
        
        board[xPos][yPos] = 'B'

        self.dfs(board,xPos,yPos+1)
        self.dfs(board,xPos+1,yPos)
        self.dfs(board,xPos,yPos-1)
        self.dfs(board,xPos-1,yPos)
        self.dfs(board,xPos+1,yPos+1)
        self.dfs(board,xPos-1,yPos-1)
        self.dfs(board,xPos+1,yPos-1)
        self.dfs(board,xPos-1,yPos+1)

    def MinesFound(self, board, xPos, yPos):
        MineCounter = 0
        if xPos+1 < len(board):
            if(board[xPos+1][yPos] == 'M'):
                MineCounter+=1
            if yPos+1 < len(board):
                if(board[xPos][yPos+1] == 'M'):
                    MineCounter+=1
                if(board[xPos+1][yPos+1] == 'M'):
                    MineCounter+=1
            if yPos - 1 >= 0:
                if(board[xPos+1][yPos-1] == 'M'):
                    MineCounter+=1
        if xPos -1 >= 0:
            if(board[xPos-1][yPos] == 'M'):
                MineCounter+=1
            if yPos -1 >=0:
                if(board[xPos][yPos-1] == 'M'):
                    MineCounter+=1
                if(board[xPos-1][yPos-1] == 'M'):
                    MineCounter+=1
            if yPos +1 < len(board[0]):
                if(board[xPos-1][yPos+1] == 'M'):
                    MineCounter+=1
        return MineCounter

def main():
    oSol = Solution()
    board = [['E', 'E', 'E', 'E', 'E'],['E', 'E', 'M', 'E', 'E'], ['E', 'E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E', 'E']]
    click = [3,0]
    print (board)
    newBoard = oSol.updateBoard(board,click)
    print (newBoard)
main()