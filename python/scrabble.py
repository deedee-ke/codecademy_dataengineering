# Define lists for letters of the alphabet and their corresponding points
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Create a dictionary mapping letters to their respective points
letter_to_points = dict(zip(letters, points))

# Add a space character with a point value of 0 to the dictionary
letter_to_points.update({" ": 0})

# Define a function to calculate the point total for a word
def score_word(word):
  point_total = 0
  for letter in word:
      point_total += letter_to_points.get(letter, 0)
  return point_total

# Test the score_word function with the word "BROWNIE"
brownie_points = score_word("BROWNIE")
print(brownie_points)

# Define a dictionary mapping players to the words they've played
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

# Create an empty dictionary to store the total points each player has earned
player_to_points = {}

# Iterate through each player's words and calculate their total points
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

# Print the total points earned by each player
print(player_to_points)
