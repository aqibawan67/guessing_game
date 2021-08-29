import random
def computer_guess(ending_range):
    low = 1
    high = ending_range
    feedback =  ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = high
        feedback =  input("is this no (" + str(guess) + ") too high (h) too low (l) : ")
        if feedback == "l":
            low = guess +1
        elif feedback == "h":
            high = guess - 1
    print("you won the game")
computer_guess(100)

