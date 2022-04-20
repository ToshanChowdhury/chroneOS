from words import list
import random

print(list)

def game():
	choice = random.choice(list)
	answer = choice
	guess_word = input("What Can Be The Word?: ")

	if choice == guess_word:
		print("You Win!!")
		print("")
	else:
		print("The Correct Word was: " + answer)
		print("")


while True:
	game()
