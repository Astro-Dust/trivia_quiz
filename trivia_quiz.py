import inquirer
from inquirer.themes import GreenPassion

points = 0

q1 = [
    inquirer.Text(
    	"name", 
    	message="What's your name?", 
    	default="No one"),

    inquirer.Checkbox(
        "question_1",
        message="It is often said that humans only use 10% of their brains. Is this true or false?",
        choices=["True", "False"]
    )
]

q2 = [
    inquirer.Checkbox(
        "question_2",
        message="It's commonly believed that the character 'Monopoly Man' in the board game Monopoly wears a monocle or binoculars. True or false?",
        choices=["True", "False"]
    )
]

q3 = [
	inquirer.Checkbox(
		"question_3",
		message="Many people remember Pikachu, the iconic Pokémon, having a black tip on its tail. However, if you look at Pikachu's official artwork, you'll find that its tail is entirely yellow without any black tip. True or false?",
		choices=["True", "False"]
	)
]

responses = inquirer.prompt(q1 + q2 + q3, theme=GreenPassion())

if "False" in responses.get("question_1"):
	points += 1
if "False" in responses.get("question_2"):
	points += 1
if "True" in responses.get("question_3"):
	points += 1

name = responses["name"].strip()

if name.upper() != "NO ONE":
	print(f'You got {points} right! \nThanks for playing, {name}!')

else:
	print(f'You got {points} right! \nThanks for playing!')







