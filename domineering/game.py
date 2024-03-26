facts = {
    "winning_move": [["not_possible_moves"]],
    "partizan_game": [["rectangular_table"]],
    "impartial_game": [["square_game"]],
    "vertical_dominant": [["partizan_game", "height_greater"]],
    "horizontal_dominant": [["partizan_game", "width_greater"]]
}

class Game:
    def __init__(self, rowLen, colLen, isComputerPlay):
        self.rowLen = rowLen
        self.colLen = colLen
        self.isVerticalPlay = True
        self.matrix = self.setInitialState()
        self.isComputerPlay = isComputerPlay
        self.moves = []
    
    def isGameOver(self):
        for row in range(self.rowLen):
            for col in range(self.colLen):
                if self.isValidMove((row, chr(ord('A')+col))):
                    return False
        return True

    def isValidMove(self, move):
        if move in self.moves:
            return False

        col_as_number = ord(move[1])-ord('A')

        if move[0] >= self.rowLen or col_as_number >= self.colLen:
            return False

        if self.isVerticalPlay:
            if not move[0]:
                return False
            return not self.matrix[move[0]][col_as_number] and not self.matrix[move[0]-1][col_as_number]

        if col_as_number >= self.colLen-1:
            return False
        
        return not self.matrix[move[0]][col_as_number] and not self.matrix[move[0]][col_as_number+1]

    def setInitialState(self):
        chessMatrix = [[0 for _ in range(self.colLen)] for _ in range(self.rowLen)]
        return chessMatrix

    def setAnyState(self, moves):
        self.matrix = self.setInitialState()

        for move in moves:
            self.setMove(move)
    
    def getBoard(self):
        return self.matrix

    def setMove(self, move):
        if not self.isValidMove(move):
            return

        self.moves.append(move)
        
        if self.isVerticalPlay:
            self.matrix[move[0]][(ord(move[1])-ord('A'))] = "x"
            self.matrix[move[0]-1][(ord(move[1])-ord('A'))] = "x"
        else:
            self.matrix[move[0]][(ord(move[1])-ord('A'))] = "o"
            self.matrix[move[0]][(ord(move[1])-ord('A'))+1] = "o"

        self.isVerticalPlay = not self.isVerticalPlay
        self.isComputerPlay = not self.isComputerPlay

    def createNewState(self, move):
        newState = Game(self.rowLen, self.colLen, self.isComputerPlay)
        newState.setAnyState(self.moves)
        newState.setMove(move)

        return newState

    def getAllCurrentPossibleStates(self):
        listMovesStates = []
        for row in range(self.rowLen):
            for col in range(self.colLen):
                if self.isValidMove((row, chr(ord('A')+col))):
                    move = (row, chr(ord('A')+col))
                    newState = self.createNewState(move)
                    listMovesStates.append((move, newState))
        return listMovesStates

    def getFacts(self):
        moveFacts = []
        if(self.isGameOver()):
            moveFacts.append("not_possible_moves")
        moveFacts.append("rectangular_table" if self.colLen != self.rowLen else "square_table")
        if(self.colLen != self.rowLen):
            moveFacts.append("height_greater" if self.rowLen > self.colLen else "width_greater")
        moveFacts.append("vertical_play" if self.isVerticalPlay else "horizontal_play")
        return moveFacts

    def evaluate(self):
        moveFacts = self.getFacts()
        visitedFacts = []

        while True:
            isAddedRule = False
            for fact in facts.keys():
                for factSet in facts[fact]:
                    if set(factSet).issubset(set(moveFacts)):
                        if fact not in visitedFacts:
                            isAddedRule = True
                            moveFacts.append(fact)
                            visitedFacts.append(fact)
                            break
                if isAddedRule:
                    break
            if not isAddedRule:
                break

        return len(moveFacts)

    def minimax(self, state, depth, alpha=float('-inf'), beta=float('inf')):
        if not depth:
            return self.evaluate(), state
        
        if self.isVerticalPlay:
            maxEval = float('-inf')
            bestMove = None
            for move in self.getAllCurrentPossibleStates():
                evaluation = move[1].minimax(move[1], depth-1, alpha, beta)[0]
                maxEval = max(maxEval, evaluation)
                if maxEval == evaluation:
                    bestMove = move[0]
                    alpha = max(alpha, maxEval)
                    if alpha >= beta:
                        break
            return maxEval, bestMove
        else:
            minEval = float('inf')
            bestMove = None
            for move in self.getAllCurrentPossibleStates():
                evaluation = move[1].minimax(move[1], depth-1, alpha, beta)[0]
                minEval = min(minEval, evaluation)
                if minEval == evaluation:
                    bestMove = move[0]
                    beta = min(beta, minEval)
                    if beta <= alpha:
                        break
            return minEval, bestMove
