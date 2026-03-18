import random
def rock_paper_scissor():
    rock = """
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """
    paper = """
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """
    sciccors = """
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    computer_choice = random.randint(0, 2)
    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    elif user_choice == 2:
        print(sciccors)
    else:
        print("Invalid choice. You lose!")

    print("Computer chose:")

    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    elif computer_choice == 2:
        print(sciccors)

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:    print("You lose!")
    print("Would you like to play again? (yes/no)")
    play_again = input().lower()
    if play_again == "yes":
        rock_paper_scissor()
    else:
        print("Thanks for playing! Goodbye!")
print("Welcome to Rock, Paper, Scissors!")
rock_paper_scissor()
