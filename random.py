#1. Import Random & creat a list of words
#2. randomly pick a word from list (import random) and assign it to a variable
#3. get user guess and assign to variable
#4. compare gueess with random word
#5. display success or failure message

import random
words=["hope","faith","love"]
choice=random.choice(words)
user_guess=input("guess if hope, faith or love is randomly selecte: ")
while choice!=user_guess:
    print("failure")
    user_guess=input("guess again: ")
else:
    print("success")
