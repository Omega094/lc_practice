import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in raw_input().split()]
n = int(raw_input())  # maximum number of turns before game over.
x, y = [int(i) for i in raw_input().split()]
left, right, up, down = 0, w-1, 0, h-1
# game loop
while True:
    bomb_dir = raw_input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    if bomb_dir == 'U':
        down = y - 1
    elif bomb_dir == 'D':
        up = y + 1
    elif bomb_dir == 'L':
        right = x - 1
    elif bomb_dir == 'R':
        left = x + 1
    elif bomb_dir == 'UR':
        down = y - 1
        left = x + 1
    elif bomb_dir == 'DR':
        up = y + 1
        left = x + 1
    elif bomb_dir == 'DL':
        up = y + 1
        right = x - 1
    elif bomb_dir == 'UL':
        down = y - 1
        right = x - 1
    x = (left + right )//2
    y = (up + down) // 2
    # the location of the next window Batman should jump to.
    print x, y
