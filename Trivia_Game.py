# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 17:22:14 2020

@author: Pedro
"""
import json
import random
import os 

class Trivia:
    def __init__(self):
        self.json_location = "Tandem_Data.json"
        self.data = None
        self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        self.questions = {}
        self.options = []
        self.score = 0

    def randomize_questions(self, parsed_json):
        selected_questions = []
        questions_left = parsed_json
        
        for i in range(10):
            current_question = random.choice(questions_left)
            selected_questions.append(current_question)
            questions_left.remove(current_question)
        
        return selected_questions
            
    def construct_questions(self):
        with open(self.json_location) as j_file:
            self.data = json.load(j_file)
            trivia_questions = self.randomize_questions(self.data)
            self.questions = trivia_questions
        
        
    def randomize_answers(self, question_index):
        possible_answer = self.questions[question_index][
            "incorrect"]
        possible_answer.append(self.questions[question_index][
            "correct"])
        
        random.shuffle(possible_answer)
        
        answer_key = {}
        
        for i in range(len(possible_answer)):
            print(self.alphabet[i].upper() + ": " + 
                  possible_answer[i])
            
            answer_key[self.alphabet[i]] = possible_answer[i]
        
        for key in answer_key:
            self.options.append(key)
        
        return answer_key
        
    def get_human_answer(self):
            selection = None
            print("You may choose your answer now!")
            
            while selection is None:
                selection = str.lower(input())
                
                if selection in self.options:
                    self.options = []
                    return selection
                    
                else:
                    selection = None
                    print("Please Select One of the Answers Above")
    
    def score_game(self, correct, picked):
        
        if picked == correct:
            self.score = self.score + 100
            os.system('clear')
            
            print("Correct! " + correct)
            print("Your New Score is " + str(self.score))
            print("")
        
        else:
            os.system('clear')
            print("I'm Sorry the Correct Answer is ... " + 
                  correct)
            print("Your Point Total Remains " + str(self.score))
            print("")
        
    def base_game(self):
        print("This is Trivia!")
        self.construct_questions()
        
        for i in range (len(self.questions)):
            correct_answer = self.questions[i]["correct"]
            
            print("Round " + str(i + 1))
            print(self.questions[i]["question"])
            
            possible_answer = self.randomize_answers(i)
            
            picked_answer = self.get_human_answer()
            
            self.score_game(correct_answer, 
                            possible_answer[picked_answer])

        if self.score == 1000:
            print ("Wow You are a Trivia Genius! 100%!")
            print("Final Score: " + str(self.score))
            
        if self.score < 1000 and self.score >= 800:
            print("Pretty Good! But can you get 100%")
            print("Final Score: " + str(self.score))
            
        if self.score <= 700 and self.score >= 400:
            print("Well Done!")
            print("Final Score: " + str(self.score))
            
        if self.score < 400:
            print("Better Luck Next Time!")
            print("Final Score: " + str(self.score))
        
        
if __name__ == "__main__":
    trivia = Trivia()
    trivia.base_game()