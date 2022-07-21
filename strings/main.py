# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# 
# UEFA Euro 1988 Final
# Create a variable for every player that scored 

player1 = "Ruud Gullit"
player2 = "Marco van Basten"

#Create a variable for each minute of the match that a goal was scored in
#Using the +-operator, create a string that reports on who scored when, according to the format:
goal_0 = 32
goal_1 = 54
scorers = (f"{player1} {goal_0}, {player2} {goal_1}")
print(scorers)

#Use f-strings or the +-operator to create a single string with information about who scored when in the format:
report = f"{player1} scored in the {goal_0}nd minute\n{player2} scored in the {goal_1}th minute"
print(report)

#Choose a player that played in the soccer match and store his name as a string in the variable player.

player = "Frank Rijkaard"
#first_name: use slicing and the find-method (help) to isolate and store the player's first name.
a = player.find(" ")
first_name = (player[:a])
last_name = (player[a+1:])

#last_name_len: use find, slicing and len to isolate and store the length of their last name.
last_name_len = len(last_name)
print(last_name_len)

#name_short: isolate and store the player's name in this format: G. von Examplestein
name_short = (f'{player[0]}. {last_name}')

print(name_short)

#chant: this is what the crowd chants when it looks like your player is going to score a goal -- their first name plus an exclamation mark(!), x-times, where x is the number of characters in their first name. Make sure the last character of this string is not a space! For our example player:
txt = ((first_name + "! ") * len(first_name))
chant = txt.rstrip(" ")
print(chant)

#good_chant: Make super-sure the last character of chant is not a space by using the inequality operator (!=). Try this in your REPL for an example: print(2 != 3). Also try: print(2 != 2).
good_chant = chant != " "
print(good_chant)
