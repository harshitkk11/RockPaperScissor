import random

user_score, computer_score, rounds = 0, 0, 0
options = ["rock", "paper", "scissors"]

while rounds < 5:
    user_input = input("Input one of the option to play : \n\"Rock\", \"Paper\", \"Scissors\" | \"Quit\" to "
                       "quit the game : ").lower()

    if user_input == "quit":
        break

    elif user_input in options:
        computer_guess = options[random.randint(0, 2)]
        print(f"\nRound : {rounds+1}\nYou: {user_input} | Computer : {computer_guess}")

        # When computer wins
        if ((user_input == "rock") and (computer_guess == "paper")) or \
                ((user_input == "paper") and (computer_guess == "scissors")) or \
                ((user_input == "scissors") and (computer_guess == "rock")):
            computer_score += 1
            rounds += 1
            print("Your Score : " + str(user_score) + "| Computer's score : " + str(computer_score) +
                  "\n....Computer Wins....\n")

        # When user wins
        elif ((user_input == "paper") and (computer_guess == "rock")) or \
                ((user_input == "scissors") and (computer_guess == "paper")) or \
                ((user_input == "rock") and (computer_guess == "scissors")):
            user_score += 1
            rounds += 1
            print("Your Score : " + str(user_score) + "| Computer score : " + str(computer_score) + "\n....You Win....\n")

        # When no one wins
        elif ((user_input == "rock") and (computer_guess == "rock")) or \
                ((user_input == "paper") and (computer_guess == "paper")) or \
                ((user_input == "scissors") and (computer_guess == "scissors")):
            print("Your Score : " + str(user_score) + "| Computer score : " + str(computer_score) + "\n....Tie....\n")

    else:
        print("Type a valid option.")

if user_score > computer_score:
    print("Congrats, You won this game!!")


elif computer_score > user_score:
    print("Computer won this game!!, Better luck next time")

else:
    print("Its Draw!!")
