import random as rd

def cprintTitle(str):
    col = rd.randint(0, 256)
    print('\033[38;5;{}m'.format(col) + '#' * 40)
    print(str + '\033[0m')