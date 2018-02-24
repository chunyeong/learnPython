import random

num1 = 1
num2 = 100

number =  random.randint(num1,num2)
win = False

name1 = input("First player name: ")
print("Hello,",name1)

name2 = input("Second player name: ")
print("Hello,",name2)

guessStr = "{} have a guess, between {} to {}: "
msg = "between {} and {}"

player = ""

while not win:
    if player == "":
        player = name1
    elif player == name1:
        player = name2
    elif player == name1:
        player = name1

    guess = int(input(guessStr.format(player,num1,num2)))
    if guess == number:
        win = True
    elif guess < number:
        if guess > num1:
            num1 = guess
    elif guess > number:
        if guess < num2:
            num2 = guess

if win:
    print("Congrat, you guessed correctly. The number was {}".format(number))
