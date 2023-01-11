def guess_number(num):
    while num != 42:
        if( num < 42):
            num = int(input("Too low! Guess again: "))
        else:
            num = int(input("Too high! Guess again: "))

num = int(input("I'm think of number! Try to guess the number I'm thinking of: "))
guess_number(num)



op = input("That's it! Would you like to play again? (y/n) ")
while op == 'y':
    num = int(input("I'm think of number! Try to guess the number I'm thinking of: "))
    guess_number(num)

else:   
    print('Thanks for palying!')