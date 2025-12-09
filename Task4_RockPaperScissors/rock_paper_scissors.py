import random
print("Rock paper scissors game")
user_input=input("choose rock,paper,or scissors: ")
user=user_input.lower()
options=["rock","paper","scissors"]
if user not in options:
    print("invalid choice. Please choose rock ,paper or scissors")
else:
    computer=random.choice(options)
    print("computer's choice:",computer)
    print("Your choice:",user)
    if user==computer:
        print("It's a tie")
    elif (user=="rock" and computer=="scissors") or(user=="paper" and computer=="rock") or (user=="scissors" and computer=="paper"):
        print("You win")
    else:
        print("computer wins")