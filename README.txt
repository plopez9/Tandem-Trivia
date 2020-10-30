# Tandem Trivia! 0.1.0

Tandem Trivia is a comand line based trivia game. Compatible with Python 3, simply run the python script "Trivia Game.py" to get started in your comand prompt. The game will walk you through 10 rounds of trivia questions. To select a question, type in the coresponding letter for the question answer. Then hit enter. Once completed, the game will present you with a message and a final score. 

##Requirements and Limitations

1) Tandem Trivia is compatible with Python 3 but not compatible with Python 2.7. The name of the raw_input() function has been changed in Python 3 to input(); resulting in a breaking change. To convert the program from Python 3 to Python 2.7, simply change the input() function back to raw_input() on line 64.

	> 64	selection = str.lower(input())

2) The "Tandem_Data.json" file must be in the same directory as the python script. If having the JSON file in another folder is of convenience, change the json_location variable on line 13 to direct the program to its new location.

	> 13	self.json_location = "Tandem_Data.json"

3) Tandem Trivia will only work with trivia questions with up to 9 answers. This was an assumption as most triva games only provide 4. Adding to the alphabet array, up to the highest number of possible answers per question, will keep the code from breaking. This can be found in line 15. 

	> 13	self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]