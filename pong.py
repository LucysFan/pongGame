import sys
from random import randint
from time import sleep
from os import system

import keyboard


updateScreen = sys.stdout.write("\x1b[1A\x1b[2K") # moves the cursor 1 row up and clears entire line, it's ASCII symbol

flag = 1
global flag

class GameField:
    def __init__(self, field):
        self.field = field
        self.score = 0, 0

    def play(self, playerPaddle, robotPaddle, pongBall):
        print('''           +++                                                         +++
         ||   ||                                                     ||   ||
         ||   ||                                                     ||   ||
           ===                                                         === ''')
        for _ in self.field:
            print(*_)
        while True:
            # player's paddle movement
            y_paddle, x_paddle = playerPaddle.position
            y_robot, x_robot = robotPaddle.position
            y_ball, x_ball = pongBall.position

            self.field[y_paddle][x_paddle] = ' '
            self.field[y_robot][x_robot] = ' '
            self.field[y_ball][x_ball] = ' '

            playerPaddle.moveObject(y_paddle, self)
            pongBall.moveObject(y_ball, self)
            robotPaddle.moveObject(y_robot, self)

            if keyboard.is_pressed('Up'):
                if playerPaddle.position[0] != 23:
                    playerPaddle.position[0] += 1
            if keyboard.is_pressed('Down'):
                if playerPaddle.position[0] != 1:
                    playerPaddle.position[0] -= 1

            y_paddle, x_paddle = playerPaddle.position
            self.field[y_paddle][x_paddle] = '|'
            #ball's movement

            if y_ball == 1 or y_ball == 23:
                pongBall.velocity[0] *= -1

            if x_ball == 2 or x_ball == 39:
                if y_ball == y_paddle:
                    pongBall.velocity[1] *= -1
                    ctg = pongBall.velocity[1] / pongBall.velocity[0]
                    l = pongBall.position[1] * ctg
                    pongBall.finalPosition = (24 - (
                    (l - (((l - pongBall.position[0]) / 25) * 24) - pongBall.position[0]))).__ceil__() - 2
                    robotPaddle.velocity[0] *= (-pongBall.finalPosition + robotPaddle.position[0]) // (
                                robotPaddle.position[0] - pongBall.finalPosition)
                if y_ball == y_robot:
                    pongBall.velocity[1] *= -1
                    robotPaddle.flag = 'start'
                else: ...

            try:
                pongBall.finalPosition + 1
                deadTime = abs(pongBall.finalPosition - robotPaddle.position[0]) // robotPaddle.velocity[0]
                if abs(pongBall.position[1] // pongBall.velocity[1]) / 5  <= deadTime:
                    if robotPaddle.position[0] != pongBall.finalPosition:
                        robotPaddle.position[0] += robotPaddle.velocity[0]
                    else:
                        print(1)
                        robotPaddle.flag = 'stop'
                #     else:
                #         robotPaddle.position[0] = robotPaddle.position[0]
                else:
                    middlePostion = randint(-1, 1)
                    if robotPaddle.flag == 'start':
                        if robotPaddle.position[0] != 1 and robotPaddle.position[0] != 23:
                            robotPaddle.position[0] += middlePostion
                    if robotPaddle.flag == 'stop':
                        ...
                #     if not flag:
                #         if robotPaddle.position[0] != 1 and robotPaddle.position[0] != 23:
                #             robotPaddle.position[0] += middlePostion
                #         print(1)
                #     else:
                #         if robotPaddle.position[0] != pongBall.finalPosition:
                #             robotPaddle.position[0] += robotPaddle.velocity[0]
                #         else:
                #             robotPaddle.position[0] = robotPaddle.position[0]
            except Exception:
                middlePostion = randint(-1, 1)
                if robotPaddle.position[0] != 1 and robotPaddle.position[0] != 23:
                    robotPaddle.position[0] += middlePostion

            y_robot, x_robot = robotPaddle.position
            self.field[y_robot][x_robot]  = '|'
            pongBall.position[0] += pongBall.velocity[0]
            pongBall.position[1] += pongBall.velocity[1]

            y_ball, x_ball = pongBall.position
            self.field[y_ball][x_ball] = '◯'


            playerPaddle.moveObject(y_paddle, self)
            pongBall.moveObject(y_ball, self)
            robotPaddle.moveObject(y_robot, self)

            sleep(0.1)

class FieldObject:
    def __init__(self, appearance : str,
                 position : [int, int],  # position [y, x], velocity [y,x]
                 velocity: [int, int]):
        self.appearance = appearance
        self.position = position
        self.velocity = velocity

    def stickObject(self, field):
        y, x = self.position
        field.field[y][x] = self.appearance

    def moveObject(self, y, field):
        sys.stdout.write(f"\x1b[{y + 1}A\x1b[2K")
        print(*field.field[y])
        sys.stdout.write(f"\x1b[{y}B")


class PongBall(FieldObject):

    def moveBall(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

class robotPaddle(FieldObject):
    ...

if __name__ == "__main__":

    pongField = [[' ' for i in range(41)] for j in range(25)] # create field map
    pongField[0] = ['+' for _ in range(41)]
    pongField[-1] = ['~' for _ in range(41)]
    pongField = GameField(pongField) # initialize object
    # create game objects
    playerPad = FieldObject('|', [12, 39], [1, 0]) # moves only up/down
    robotPad = FieldObject('|', [12, 2], [1, 0]) # moves only up/down
    pongBall = FieldObject('◯', [12, 20], [1, 1]) # can move in any direction in 2D space, spawns in the center

    playerPad.stickObject(pongField)
    robotPad.stickObject(pongField)
    pongBall.stickObject(pongField)

    system('cls')
    pongField.play(playerPad, robotPad, pongBall)

# os.system('cls')
#
# print(1234)
# print(4567)
# print('Hello')
# sys.stdout.write("\x1b[1A")
# print(3, '8')