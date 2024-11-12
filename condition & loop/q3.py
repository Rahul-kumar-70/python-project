"""Write a Python program to guess a number between 1 and 9.
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess
is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit."""
while True:
    n=int(input("enter the number between 1 and 9 only:"))
    if n in [1,2,3,4,5,6,7,8,9]:
        print("well guessed")
        break
    else:
        print("please again this is not valid number")