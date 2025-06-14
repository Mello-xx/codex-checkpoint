# Rock Paper Scissors

import random

a= "rock"
b= "paper"
c= "scissors"

user= input("Enter a choice (a = rock,b = paper,c = scissors): ")
cpu= random.choice([a,b,c])

if (user== a and cpu== c) or (user== b and cpu== a) or (user== c and cpu== b):
    print("You win!")
else:
    print("You lose!")

print(f'User chose {user}, CPU chose {cpu}')