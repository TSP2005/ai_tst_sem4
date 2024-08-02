import random


class Game:
    def __init__(self, stones=50):
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
        return -1  # Player 1 loses
    return 0


def ai_move(game):
    best_move = None
    best_eval = float('-inf')
    for move in game.get_legal_moves():
        game.make_move(move)
        eval = minimax(game, 3, float('-inf'), float('inf'), False)
        game.make_move(-move)
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move


def play_game():
    game = Game()
    print("Initial stones:", game.stones)

    while not game.is_game_over():
        if game.current_player == 1:
            move = ai_move(game)
            print("AI removes", move, "stones.")
        else:
            move = int(input("Your turn. Enter 1 or 2 to remove stones: "))
            while move not in game.get_legal_moves():
                move = int(input("Invalid move. Enter 1 or 2: "))

        game.make_move(move)
        print("Stones left:", game.stones)
        game.current_player = 3 - game.current_player  # Switch players

    if game.stones <= 0 and game.current_player == 1:
        print("You win!")
    else:
        print("AI wins!")


play_game()
