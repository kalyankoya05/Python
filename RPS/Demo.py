import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock,paper,or scissors:? ").lower()

    if player == computer:
        print("Player Choice: "+player)
        print("Computer Choice: "+computer)
        print("Tie!!")
    elif player == "rock":
        if computer == "paper":
            print("Player Choice: "+player)
            print("Computer Choice: "+computer)
            print("Lose!!")
        if computer == "scissors":
            print("Player Choice: "+player)
            print("Computer Choice: "+computer)
            print("Win!!")
    elif player == "scissors":
        if computer == "rock":
            print("Player Choice: "+player)
            print("Computer Choice: "+computer)
            print("Lose!!")
        if computer == "paper":
            print("Player Choice: "+player)
            print("Computer Choice: "+computer)
            print("Win!!")
    elif player == "paper":
        if computer == "scissors":
            print("Player Choice: "+player)
            print("Computer Choice: "+computer)
            print("Lose!!")
        if computer == "rock":
            print("Player Choice: "+player)
            print("Computer Choice: "+computer)
            print("Win!!")
    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("Bye!!")