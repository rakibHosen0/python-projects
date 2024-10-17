import  random as ra

randomNumber = ra.randint(1,100);

while True :
    try:
        guessNumber = int(input("Guess the number between 1 and 100: "))
        if guessNumber == randomNumber:
            print("Congratulation! You guessed the number.")
            break
        elif guessNumber > randomNumber:
            print("Too High!")
        elif guessNumber < randomNumber:
            print("Two low!")
        else:
            print("Please enter a valid number")
    except ValueError:
        print("Please Enter a valid Number")



