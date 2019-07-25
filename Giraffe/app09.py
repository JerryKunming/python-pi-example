secret_word = "giraffe"
guess_word = " "

guess_limit = 3
guess_count = 0
guess_status = True

while guess_word != secret_word and guess_status:
    if guess_count < guess_limit:
        guess_word = input("Please input your guesses: ")
        guess_count += 1
    else:
        guess_status = False
if not(guess_status):
    print("Out of guesses, YOU LOSE")
else:
     print("YOU WIN!")