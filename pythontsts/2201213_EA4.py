import random

class Game:
    def start(self, stones=50):
        self.stones = stones
        self.current_player = random.choice([1, 2])

    def get_legal_moves(self):
        return [1, 2]

    def make_move(self, move):
        self.stones -= move

    def is_game_over(self):
        return self.stones <= 0

def minimax(game, depth, alpha, beta, maximizing_player):
    if depth == 0 or game.is_game_over():
        return evaluate(game)

    if maximizing_player:
        max_eval = float('-inf')
        for move in game.get_legal_moves():
            game.make_move(move)
            eval = minimax(game, depth - 1, alpha, beta, False)
            game.make_move(-move)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in game.get_legal_moves():
            game.make_move(move)
            eval = minimax(game, depth - 1, alpha, beta, True)
            game.make_move(-move)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def evaluate(game):
    if game.stones <= 0 and game.current_player == 1:
        return -1
    return 0

def ai_move(game):
    if game.stones % 3 == 0:
        move = random.choice(game.get_legal_moves())
    else:
        move = game.stones % 3
    print("AI removes", move, "stones.")
    return move


def play_game():
    game = Game()
    game.start()
    print("Initial stones:", game.stones)

    while not game.is_game_over():
        if game.current_player == 1:
            move = ai_move(game)
        else:
            move = int(input("Your turn. Enter 1 or 2 to remove stones: "))
            while move not in game.get_legal_moves():
                move = int(input("Invalid move. Enter 1 or 2: "))

        game.make_move(move)
        print("Stones left:", game.stones)
        game.current_player = 3 - game.current_player

    if game.stones <= 0 and game.current_player == 1:
        print("You win!")
    else:
        print("AI wins!")

play_game()
