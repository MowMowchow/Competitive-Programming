import sys

knightx, knighty = sys.stdin.readline().split()
finalx, finaly = sys.stdin.readline().split()
knightx, knighty, finalx, finaly = int(knightx), int(knighty), int(finalx), int(finaly)

board = [[100, 100, 100, 100, 100, 100, 100, 100, 100],
        [100, 100, 100, 100, 100, 100, 100, 100, 100],
        [100, 100, 100, 100, 100, 100, 100, 100, 100],
        [100, 100, 100, 100, 100, 100, 100, 100, 100],
        [100, 100, 100, 100, 100, 100, 100, 100, 100],
        [100, 100, 100, 100, 100, 100, 100, 100, 100],
        [100, 100, 100, 100, 100, 100, 100, 100, 100],
        [100, 100, 100, 100, 100, 100, 100, 100, 100],
        [100, 100, 100, 100, 100, 100, 100, 100, 100]]

def play(knightx, knighty, finalx, finaly, turn):
    if knightx < 9 and knighty > 0 and knighty < 9 and knightx > 0 and turn < board[knightx][knighty]:
        board[knightx][knighty] = turn
        if knighty == finaly and knightx == finalx:
            return

        else:
            play(knightx+1, knighty+2, finalx, finaly, turn+1)
            play(knightx+2, knighty+1, finalx, finaly, turn+1)
            play(knightx+2, knighty-1, finalx, finaly, turn+1)
            play(knightx+1, knighty-2, finalx, finaly, turn+1)
            play(knightx-1, knighty-2, finalx, finaly, turn+1)
            play(knightx-2, knighty-1, finalx, finaly, turn+1)
            play(knightx-2, knighty+1, finalx, finaly, turn+1)
            play(knightx+1, knighty+2, finalx, finaly, turn+1)


play(knightx, knighty, finalx, finaly, 0)
print(board[finalx][finaly])