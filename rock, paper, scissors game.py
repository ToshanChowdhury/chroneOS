import random

choices = ["rock", "paper", "scissors"]

def start():
	computer = random.choice(choices)
	player = None

	while player not in choices:
		player = input("rock, paper or scissors?: ").lower()

	if player == computer:
		print(computer)
		print(player)
		print("Tie!!")
		input()
	elif player == "rock":
		if computer == "paper":
			print(computer)
			print(player)
			print("You Lose!!")
			input()

		if computer == "scissors":
			print(computer)
			print(player)
			print("You Win!!")
			input()
	elif player == "paper":
		if computer == "rock":
			print(computer)
			print(player)
			print("You Win!!")
			input()

		if computer == "scissors":
			print(computer)
			print(player)
			print("You Lose!!")
			input()
	elif player == "scissors":
		if computer == "rock":
			print(computer)
			print(player)
			print("You Lose!!")
			input()

		if computer == "paper":
			print(computer)
			print(player)
			print("You Win!!")
			input()

while True:
	start()