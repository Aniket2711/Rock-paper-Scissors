import random
def play():
    user = input("'r' for Rock, 'p' for Paper, 's' for Scissor\n")
    computer = random.choice(['r','p','s'])
    
    if user == computer:
        return "It\' is a tie"

    if win(user,computer):
        return "User won!"

    return "Computer won!"

def win(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
print(play())