#!usr/bin/env python3

secret_word = "Mancy"
guess = ""
guess_count = 0
guess_limit = 2
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("The password is a name. Guess it: ")
        guess_count += 1
    if guess_count == 1:
        guess = input("Come on. Try it again. It starts with an M: ")
        guess_count += 1
    elif guess_count == guess_limit:
        guess = input("Hint: N as in Nancy, M as in...: ")
        guess_count += 1
    else:
        out_of_guesses = True
        print(":(")

if out_of_guesses:
    print("Come on. Mancy was so obvious!")
else:
    print("You got it! M as in Mancy!")
