from GN0.alpha_zero_general.Game import Game
from graph_game.shannon_node_switching_game import Node_switching_game
from graph_game.graph_tools_games import Hex_game
from typing import List

class HexGame(Game):
    def __init__(self,size=11):
        super().__init__()
        self.size = size

    def getInitBoard(self) -> Node_switching_game:
        game = Hex_game(self.size)
        return game

    def getBoardSize(self,game:Node_switching_game) -> int:
        return game.view.num_vertices()-2

    def getActionSize(self,game:Node_switching_game) -> int:
        return game.view.num_vertices()-2

    def getActions(self,game:Node_switching_game) -> List[int]:
        return game.get_actions()

    def getNextState(self,game:Node_switching_game,action:int):
        # Does not modify the current board
        game2 = game.copy(withboard=False)
        game2.make_move(action)
        return game2

    def getValidMoves(self,game:Node_switching_game):
        return game.get_actions()

    def getGameEnded(self,game:Node_switching_game,player:int):
        res = game.who_won()
        if res is None:
            return 0
        else:
            if player==1 and res=="m" or player==-1 and res=="b":
                return 1
            else:
                return -1

    def getHash(self, game:Node_switching_game):
        return game.hashme()
