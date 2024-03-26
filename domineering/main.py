import time
import pygame
from chessBoard import ChessBoard
from game import Game
from window import Window
import math

pygame.init()
pygame.display.set_caption("Domineering")

screen = pygame.display.set_mode([700, 700])

the_window = Window()

(rowLen, colLen, isComputerFirst) = the_window.showInputFieldsWindow()

chessBoard = ChessBoard(pygame, screen, rowLen, colLen)

newGame = Game(rowLen, colLen, isComputerFirst)

isGameOver = False

running = True
while running and not isGameOver:
    screen.fill((255, 255, 255))

    if newGame.isComputerPlay:
        _, newMove = newGame.minimax((0, 0), 5)
        newGame.setMove(newMove)
        if(newGame.isGameOver()):
            isGameOver = True
            chessBoard.drawCurrentChessBoard(newGame.getBoard())
            pygame.display.flip()
            the_window.showWinner(newGame.isVerticalPlay)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            posx, posy = pygame.mouse.get_pos()

            if( posx > 20 and posy > 20 and posy < chessBoard.square_width*rowLen+20 and posx < chessBoard.square_width*colLen+20):
                kordy= math.ceil((posy-20)/(chessBoard.square_width)-1)
                kordx = chr(ord('A')+math.ceil((posx-20)/(chessBoard.square_width))-1)
                if(newGame.isValidMove((kordy, kordx))):             
                    newGame.setMove((kordy, kordx))
                    if(newGame.isGameOver()):
                        isGameOver = True
                        chessBoard.drawCurrentChessBoard(newGame.getBoard())
                        pygame.display.flip()
                        the_window.showWinner(newGame.isVerticalPlay)
                
        if event.type == pygame.QUIT:
            running = False
        

    chessBoard.drawCurrentChessBoard(newGame.getBoard())
    
    pygame.display.flip()

pygame.quit()