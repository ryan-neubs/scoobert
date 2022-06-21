# tictactoe.py
# by Ryan Neubauer
# simple terminal tik tak toe game
# Note: hoping to use this for the scoobert bot in the future
from random import randint
from time import sleep

class TicTacToe:

    def __init__(self, firstplayer):
        self.tiles = {'t1':" ", 't2':" ", 't3':" ", 't4':" ", 't5':" ", 
        't6':" ", 't7':" ", 't8':" ", 't9':" "}
        self.table = f"""
        -------------
        |[{self.tiles['t1']}]|[{self.tiles['t2']}]|[{self.tiles['t3']}]|
        -------------
        |[{self.tiles['t4']}]|[{self.tiles['t5']}]|[{self.tiles['t6']}]|
        -------------
        |[{self.tiles['t5']}]|[{self.tiles['t8']}]|[{self.tiles['t9']}]|
        -------------
        """
        self.turn = firstplayer
        
    def mark(self, player, spot):
        self.tiles[spot] = player
        self.updatetable()
        self.switchturn()

    def validmove(self, move):
        try:
            if self.tiles[move] == 'X' or self.tiles[move] == 'O' or (move not in self.tiles):
                return False
            return True
        except KeyError:
            return False

    def switchturn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

    def gameover(self):
        # Yeah I know there is definitely a way to do this better but its 1:00am and I can't fuckin thing of it
        if ((((self.tiles['t1'] == self.tiles['t2'] == self.tiles['t3'] == "X") or (self.tiles['t1'] == self.tiles['t4'] == self.tiles['t7'] == "X") or 
        (self.tiles['t1'] == self.tiles['t5'] == self.tiles['t9'] == "X") or (self.tiles['t4'] == self.tiles['t5'] == self.tiles['t6'] == "X") or
        (self.tiles['t7'] == self.tiles['t8'] == self.tiles['t9'] == "X") or (self.tiles['t3'] == self.tiles['t5'] == self.tiles['t7'] == "X") or
        (self.tiles['t2'] == self.tiles['t5'] == self.tiles['t8'] == "X") or (self.tiles['t3'] == self.tiles['t6'] == self.tiles['t9']  == "X"))) or 
        (((self.tiles['t1'] == self.tiles['t2'] == self.tiles['t3'] == "O") or (self.tiles['t1'] == self.tiles['t4'] == self.tiles['t7'] == "O") or 
        (self.tiles['t1'] == self.tiles['t5'] == self.tiles['t9'] == "O") or (self.tiles['t4'] == self.tiles['t5'] == self.tiles['t6'] == "O") or
        (self.tiles['t7'] == self.tiles['t8'] == self.tiles['t9'] == "O") or (self.tiles['t3'] == self.tiles['t5'] == self.tiles['t7'] == "O") or
        (self.tiles['t2'] == self.tiles['t5'] == self.tiles['t8'] == "O") or (self.tiles['t3'] == self.tiles['t6'] == self.tiles['t9']  == "O")))):
            return True
        # Fuck that's ugly code ^^^
        return False

    def checktie(self):
        # Loop through the tile dictionary and check for empty spaces.
        # If all tiles aren't empty that means there is a draw.
        # Note, this fun
        for value in self.tiles:
            if self.tiles[value] == " ":
                return False
        return True

    def updatetable(self):
        self.table = f"""
        -------------
        |[{self.tiles['t1']}]|[{self.tiles['t2']}]|[{self.tiles['t3']}]|
        -------------
        |[{self.tiles['t4']}]|[{self.tiles['t5']}]|[{self.tiles['t6']}]|
        -------------
        |[{self.tiles['t7']}]|[{self.tiles['t8']}]|[{self.tiles['t9']}]|
        -------------
        """

def main():
    rematch = True
    print("Welcome to TicTacToe!")
    print("Tiles are labeled like so:")
    print("""
    ----------------
    |[t1]|[t2]|[t3]|
    ----------------
    |[t4]|[t5]|[t6]|
    ----------------
    |[t7]|[t8]|[t9]|
    ----------------
    """)
    print("Game will start in 10 seconds...")
    sleep(10)
    while rematch != False:
        print("\nAssigning Symbols...")
        sleep(3)
        turn = randint(0,1)
        if turn == 0:
            game = TicTacToe('X')
            print('X will go first.')
        else:
            game = TicTacToe('O')
            print('O will go first.')
        # Fancy countdown thing to make sure player is ready, just cuz
        sleep(1)
        print("\nGame begins in:")
        print("5...")
        sleep(1)
        print("4...")
        sleep(1)
        print("3...")
        sleep(1)
        print("2...")
        sleep(1)
        print("1...")
        sleep(1)

        # Start of game
        while game.gameover() == False and game.checktie() == False:
            print(game.table)
            print("Turn:", game.turn)
            move = str(input("What is your move? (t1, t3, t6, etc):"))
            while True:
                if game.validmove(move):
                    game.mark(game.turn, move)
                    break
                else:
                    print(game.table)
                    print("Tile is taken or input was incorrect, try again.")
                    print("Turn:", game.turn)
                    move = str(input("What is your move? (t1, t3, t6, etc):"))
        
        # Code to execute once gameover == True
        if game.checktie() == True and game.gameover() == False:
            print(game.table)
            print("Game has ended in a draw!")
        else:
            game.switchturn()
            print(game.table)
            print(game.turn, 'Wins!')
        restart = str(input("Play again? (Y/n):"))
        if restart == 'Y' or restart == 'y':
            rematch = True
        else:
            rematch = False
            print("Goodbye!")

if __name__ == '__main__':
    main()
