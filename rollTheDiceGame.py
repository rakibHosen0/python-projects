import random as rn

while True:
    userInput = input("Roll the dice? (Y/N): ").lower()
    if userInput == 'y':
        print(f"({rn.randint(1, 9)}, {rn.randint(1, 9)})")
    elif userInput == 'n':
        print("Thanks for playing")
        break
    else:
        print("Invalid")


