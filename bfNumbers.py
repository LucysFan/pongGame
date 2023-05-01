import sys
from os import system
from time import sleep

import keyboard


def typingPrint(regime, interval = 0.15, *args):
    '''
    function for immitating machine typing
    note that your arguments should be list format,
    equal size and for any unprognisable results
    shouldn't be plugged with an asteriks
    '''

    length = len(args[0])
    
    if not(any([len(i) == length for i in args])):
        raise ValueError("Check the sizes of an arrays or arrays format")
 
    bfArray = [[] for _ in range(length)]
 
    match regime:
        case 1:
            for el in args:
                for idx in range(length):
                    bfArray[idx] += [''] + el[idx]  
            for bfSegment in bfArray:        
                for obj in bfSegment:
                    for el in obj:
                        print(el, end = '', flush = True)
                        sleep(interval)
                print(end = '\n')  
        case 2:
            for el in args:
                bfArray += el
            for bfSegment in bfArray:        
                for obj in bfSegment:
                    for el in obj:
                        print(el, end = '', flush = True)
                        sleep(interval)
            print(end = '\r') 

    return None

def startGame(fraze, blank, game, 
              cube1, cube2, cube3,
              n0, n1, n2, n3, n4,
              n5, n6, n7, n8, n9):

    system('cls')

    pictures = ['image1.txt', 'image2.txt',
                'image3.txt','image4.txt',]
    prelude = []
    
    for picture in pictures:
        with open(picture, 'r', encoding = 'utf-8') as film:
            prelude.append(film.readlines())

    while not(keyboard.is_pressed('Enter')):
        for frame in prelude:
            print("".join(frame))
            sleep(.25)
            system('cls')
    
    system('cls')

    typingPrint(1, 0.01, fraze, blank, game)
    sys.stdout.write("\x1b[3A")
    typingPrint(2, 0.05, fraze[0], cube1[0], n0[0], n0[0], procent[0], blankGame[0])
    sys.stdout.write("\x1b[1B")
    typingPrint(2, 0.05, fraze[1], cube1[1], n0[1], n0[1], procent[1], blankGame[1])
    sys.stdout.write("\x1b[1B")
    typingPrint(2, 0.05, fraze[2], cube1[2], n0[2], n0[2], procent[2], blankGame[2])
    
    _array = [[n0,n0], [n0,n5], [n1,n0],
              [n1,n5], [n2,n0], [n2,n5],
              [n3,n0], [n3,n5], [n4,n0],
              [n4,n5], [n5,n0], [n5,n5],
              [n6,n0], [n6,n5], [n7,n0],
              [n7,n5], [n8,n0], [n8,n5],
              [n9,n0], [n9,n5],
              ]
    
    for el in range(19):
        
        for _ in range(3):
            print(*fraze[2], '□□ ', sep = '', end = '\r')
            sleep(0.1)
            print(*fraze[2], '□□□', sep = '', end = '\r')
            sleep(0.1)
            print(*fraze[2], '□□ ', sep = '', end = '\r')
            sleep(0.1)
            print(*fraze[2], '□  ', sep = '', end = '\r')
            sleep(0.1)
        sys.stdout.write("\x1b[3A")
        typingPrint(2, 0.001, fraze[0], cube1[0], _array[el+1][0][0], _array[el+1][1][0], procent[0], blankGame[0])
        sys.stdout.write("\x1b[1B")
        typingPrint(2, 0.001, fraze[1], cube1[1], _array[el+1][0][1], _array[el+1][1][1], procent[1], blankGame[1])
        sys.stdout.write("\x1b[1B")
        typingPrint(2, 0.001, fraze[2], cube1[2], _array[el+1][0][2], _array[el+1][1][2], procent[2], blankGame[2])


    
    
blank = [
 ['   '],
 ['   '],
 ['   '],
 ]
 
procent = [
 ['□ /'],
 [' / '],
 ['/ □'],
 ]
 
cube1 = [
 ['   '],
 ['   '],
 ['□  '],
 ]
 
cube2 = [
 ['   '],
 ['   '],
 ['□□'],
 ]
 
cube3 = [
 ['   '],
 ['   '],
 ['□□□'],
 ]
 
n0 = [
 ['|‾‾|'],
 ['|  |'],
 ['|__|'],
 ]
n1 = [
 [' | '],
 [' | '],
 [' | '],
 ]
n2 = [
 ['‾‾|'],
 ['/‾'],
 ['|__'],
 ]
n3 = [
 ['‾‾|'],
 [' =|'],
 ['__|'],
 ]
n4 = [
 ['| '],
 ['|_|'],
 ['  |'],
 ]
n5 = [
 ['|‾‾'],
 [' \\ '],
 ['__|'],
 ]
n6 = [
 ['|‾‾'],
 ['|__'],
 ['|__|'],
 ]
n7 = [
 ['‾‾|'],
 ['  |'],
 ['  |'],
 ]
n8 = [
 ['|‾|'],
 ['|=|'],
 ['|_|'],
 ]
n9 = [
 ['|‾|'],
 [' ‾|'],
 [' _|'],
 ]
 
fraze = [
            ['| |\  | |  |  |   /\   |   | ‾‾/ | |\  | /‾‾|'],
            ['| | \ | | -+- |  /==\  |   |  /  | | \ | | _ '],
            ['| |  \| |  |  | /    \ |__ | /__ | |  \| |__\\'],
        ]

blankGame = [
                ['           '],
                ['           '],
                ['           '],
                ['           '],
            ]


game = [
            ['/‾‾|   /\   |\  /| |‾‾'],
            ['| _   /==\  | \/ | |= '],
            ['|__\\ /    \ |    | |__'],
        ]
