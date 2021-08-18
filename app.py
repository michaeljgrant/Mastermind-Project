import random


#Computer guess selects random number 4 digit number from 1000 to 10000
computer_number = random.randrange(1000, 10000)
print(computer_number)
player_guess = int(input("Guess the 4 digit number:"))

#Does the players guess equal the commputers choice? If not check how many numbers are correct.
if (player_guess == computer_number):
	print("Great! You guessed the number in a single try! You're a Mastermind!")
else:
	#initialize counter for number of guesses made
	guess_counter = 0

	#while loop to make the player guess again until they get all digits correct
	while (player_guess != computer_number):
		# guess count +1 after player incorrect guess at full 4 digit number
		guess_counter += 1

		count = 0

		# convert number to string to make iteration easier
		player_guess = str(player_guess)
		computer_number = str(computer_number)

		#array store of correct digits
		correct = ["X","X","X","X"]
        
		# loop over index
		for i in range(0, 4):

			# checking for equality of digits
			if (player_guess[i] == computer_number[i]):
				# number of digits guessed correctly increments
				count += 1
				#
				correct[i] = player_guess[i]
			else:
				continue

		# when not all the numbers correct
		if (count < 4) and (count != 0):
			print(f"Incorrect! You have gotten: {count} correct so far.. Here's the gameboard")
			for numbers in correct:
				print(numbers, end=' ')
			print('\n')
			print('\n')
			player_guess = int(input("Enter your next choice of numbers: "))
		# when no numbers correct
		elif (count == 0):
			print("None of the numbers in your guess match.")
			player_guess = int(input("Enter your next choice of numbers: "))

	# Win condition met
	if player_guess == computer_number:
		print("You've become a Mastermind!")
		print(f"It only took you {guess_counter} tries.")

