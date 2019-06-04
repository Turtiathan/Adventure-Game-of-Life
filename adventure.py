import random

class Person:
	def __init__(self, name, age=18, income=1000):
		self.name = name
		self.age = age
		self.income = income

	def updateIncome(self, eventChoice):
		howMuchMoney = eventChoice.returnIncomeChange()
		self.income += howMuchMoney

	def updateAge(self, eventChoice):
		yearsPassed = eventChoice.returnAgeChange()
		self.age += yearsPassed

class Event:
	def __init__(self, eventName, description, outcome):
		self.eventName = eventName
		self.description = description
		self.outcome = outcome

class TimeEvent(Event):
	def __init__(self, eventName, description, outcome, yearsPassed):
		Event.__init__(self, eventName, description, outcome)
		self.yearsPassed = yearsPassed

	def returnAgeChange(self):
		return self.yearsPassed

class MoneyEvent(Event):
	def __init__(self, eventName, description, outcome, howMuchMoney, profit_or_cost):
		Event.__init__(self, eventName, description, outcome)
		self.howMuchMoney = howMuchMoney
		self.profit_or_cost = profit_or_cost

	def returnIncomeChange(self):
		if self.profit_or_cost == True:
			return self.howMuchMoney
		else:
			return self.howMuchMoney * -1

def adventureGame():
	"""
	This is a text-based adventure game. The player inputs choices that represent life decisions.
	This is just a demo version.
	"""
	print("Hello and welcome to a game of Adventure. This is a game of life.")
	print("You are now 18 years old and you have $1000 from your parents who kicked you out.")
	print("It is time to survive. Choose the correct events to see if you will have a positive outcome.")
	name = raw_input("Let's get your name first: ")

	player = Person(name)

	print("Hello " + player.name + ". Your life adventure has begun. You are now 18 years old and you have $1000.")
	print("")
	print("Now that you are by yourself, you need to find a place to live.")

	firstHomeChoice = MoneyEvent("Event A", "You rent an apartment with your friends.", "Congratulations. You saved some money.", 500, False)
	secondHomeChoice = MoneyEvent("Event B", "You rent an apartment by yourself.", "You get a whole place for yourself but you are in debt now.", 2000, False)
	thirdHomeChoice = MoneyEvent("Event C", "You just sleep on the streets for the time being.", "You saved money but is it worth it?", 0, False)

	eventChoices = {'a': firstHomeChoice, 'b': secondHomeChoice, 'c': thirdHomeChoice}

	print("Here are the three choices you can make. Enter 'a', 'b', or 'c' to choose one of the following choices.")
	print(firstHomeChoice.eventName + ": " + firstHomeChoice.description)
	print(secondHomeChoice.eventName + ": " + secondHomeChoice.description)
	print(thirdHomeChoice.eventName + ": " + thirdHomeChoice.description)

	while True:
		try:
			decision = raw_input("Make a choice now.").lower()

			print(eventChoices[decision].outcome)
			break
		except:
			print("You did not enter a valid choice. Please try again.")

	player.updateIncome(eventChoices[decision])
	print("You now have $" + str(player.income) + ".")
	print("")

	print("Now that you have a place to stay. You must now decide what to do to make money. Make a decision to see what happens in the next six years.")

	firstJobChoice = TimeEvent("Event A", "You just take up a part-time job making $15 an hour.", "You start making money right away even though it is the minimum.", 6)
	secondJobChoice = TimeEvent("Event B", "You decide to get a four-year degree. For the next four years, you are studying for the hopes it will all pay off in the end.", "You'll have a chanve to make lots of money in the future. Or do you?", 6)
	thirdJobChoice = TimeEvent("Event C", "You decide to learn a trade and so need two years of learning before getting a good job.", "You invest two years to learn a skill. Unlike the college student, you can start making more money sooner.", 6)

	eventChoices['a'] = firstJobChoice
	eventChoices['b'] = secondJobChoice
	eventChoices['c'] = thirdJobChoice

	print("Here are the three choices you can make. Enter 'a', 'b', 'c' to choose one of the following choices.")
	print(firstJobChoice.eventName + ": " + firstJobChoice.description)
	print(secondJobChoice.eventName + ": " + secondJobChoice.description)
	print(thirdJobChoice.eventName + ": " + thirdJobChoice.description)

	while True:
		try:
			decision = raw_input("Make a choice now.").lower()

			print(eventChoices[decision].outcome)
			break
		except:
			print("You did not enter a valid choice. Please try again.")

	player.updateAge(eventChoices[decision])
	print("You are now " + str(player.age) + " years old.")
	print("")

	print("Thanks for playing. Stay tuned for the full release of the game to see what happens next in your life.")

while True:
	adventureGame()
	
	continueGame = raw_input("Do you want to play again? Press 'n' to end the game. Otherwise enter any key.").lower()
	if continueGame == 'n':
		break
