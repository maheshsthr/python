scores = {"mahesh": 32, "shubham": 26, "riddhi": 29, "vinesh": 38}
print("Scores:", scores)
name = input("Enter player name to check score: ")
print(f"{name}'s score:", scores.get(name, "Player not found"))