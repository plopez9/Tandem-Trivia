# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 14:37:17 2020

@author: Pedro
"""
import unittest
import mock


import Trivia_Game as tg

class TestTrivia(unittest.TestCase):
            
    
    def setUp(self):
        self.json_location = "Tandem_Data.json"
        self.data = None
        self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        self.questions = {}
        self.options = []
        self.score = 0
    
    def tearDown(self):
        self.json_location = "Tandem_Data.json"
        self.data = None
        self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        self.questions = {}
        self.options = []
        self.score = 0
    
    def test_construct_questions(self):
        
        pass
    
    def test_randomize_answers(self):
        
        pass
        
    def test_get_human_answer(self):
        self.options = ["a", "b", "c", "d"]
        
        with mock.patch("builtins.input", return_value="a"):
            selection = tg.Trivia.get_human_answer(self)
            
            assert selection == "a"
            
    
    def test_score_game(self):
        
        tg.Trivia.score_game(self, "Correct Answer", "Incorrect Answer")
        
        assert self.score == 0
        
        
        tg.Trivia.score_game(self, "Correct Answer", "Correct Answer")
        
        assert self.score == 100
        
    
    def test_base_game(self):
        pass
        
if __name__ == "__main__":
    unittest.main()