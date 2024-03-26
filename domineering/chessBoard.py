class ChessBoard:
    def __init__(self, pygame, screen, rowLen, colLen) -> None:
        self.rowLen = rowLen
        self.colLen = colLen
        self.offset = 20
        self.pygame = pygame
        self.screen = screen
        self.square_width = min((self.screen.get_width() - self.offset * 2) / self.rowLen, (self.screen.get_height() - self.offset * 2) / self.colLen)
        self.font = self.pygame.font.SysFont("timesnewroman", 20)
        self.grayFieldColor = (160, 160, 160)
        self.whiteFieldColor = (240, 240, 240)
        self.verticalDominoColor = (255, 132, 0)
        self.horizontalDominoColor = (0, 0, 0)

    def drawChessTable(self):
        isBlackField = True

        for row in range(self.rowLen):
            for col in range(self.colLen):
                self.pygame.draw.rect(self.screen, self.grayFieldColor if isBlackField else self.whiteFieldColor, self.pygame.Rect(self.square_width * col + self.offset, self.square_width * row + self.offset, self.square_width, self.square_width))
                isBlackField = not isBlackField
            if(self.colLen % 2 == 0):
                isBlackField = not isBlackField
        
        for row in range(self.rowLen):
            textX = self.offset / 2
            textY = row * self.square_width + self.offset + self.square_width / 2
            text = self.font.render(f"{self.rowLen - row}", True, (0, 0, 0), None)
            textRect = text.get_rect()
            textRect.center = (textX, textY)

            self.screen.blit(text, textRect)
        
        for col in range(self.colLen):
            textX = col * self.square_width + self.offset + self.square_width / 2
            textY = (self.square_width * self.rowLen + self.offset) + self.offset / 2
            text = self.font.render(f"{chr(ord('a')+col)}", True, (0, 0, 0), None)
            textRect = text.get_rect()
            textRect.center = (textX, textY)

            self.screen.blit(text, textRect)
    
    def drawCurrentChessBoard(self, matrix):
        self.drawChessTable()
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if col:
                    self.pygame.draw.rect(self.screen, self.verticalDominoColor if col == "x" else self.horizontalDominoColor, self.pygame.Rect(self.square_width * j + self.offset, self.square_width * i + self.offset, self.square_width, self.square_width))