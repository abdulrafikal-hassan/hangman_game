def hangman_game():

    name = input("What is your name? ")
    print("Hello " + name, "It is time to play hangman")
    print("Start guessing.....")

    # determine the number of turns
    turns = 10

    # create a variable for the empty variable
    guesses = ""

    # here we set the secret
    word = "secret"
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)

            else:
                print("_")
                failed += 1
        if failed == 0:
            print("You won!")
            break
        guess = input("guess a character: ")
        guesses += guess

        # Decision making using python control
        if guess not in word:
            turns -= 1
            print("Wrong guess")
        print("You have", + turns, " more guesses")
        if turns == 0:
            print("Game is Over, you lost")

    check = input("Do you want to play a game  Y/N ?")
    if check == "Y":
        hangman_game()

hangman_game()