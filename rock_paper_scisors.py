import random

def play(): 
    user = input("Whats your choice? 'r' for rock, 'p' for paper 's' for scissors\n")
    user = user.lower()
    
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "You and the computer have both chosen {}. It's a tie".format(computer)

    # r > s, s > p, p > r
    if is_win(user, computer):
        return "You have chosen {} and the computer has chosen {}. You won!".format(user, computer)

    return "You have chosen {} and the computer has chosen {}. You won!".format(user, computer)

def is_win(player, opponent):
    # return true is the player beats the opponent
    # winning conditions: r > s, p > s, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

if __name__ == '__main__':
    print(play())