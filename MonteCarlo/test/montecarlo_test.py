import numpy as np
import pandas as pd
import unittest
import montecarlo

class MonteCarloTestSuite(unittest.TestCase):

    faces1 = np.array([1,2,3,4,5,6])
    faces2 = np.array(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
    faces3 = np.array(['heads', 'tails'])

    die1 = montecarlo.Die(faces1)

    def test_01_die_init_1(self):
        '''Ensure that all weights are equal after initialization'''
        
        self.assertTrue(self.die1.seeDie()['Weight'].unique().size == 1, "Dice are being initialized with imperfect weights")
    
    def test_02_die_init_2(self):
        '''Ensure that all weights are 1'''
        self.assertTrue(self.die1.seeDie()['Weight'].unique()[0] == 1, "Dice are being initialized with weights other than 1")

    def test_03_die_roll(self):
        '''Ensure that 'roll' rolls the die the correct number of times'''
        self.assertTrue(len(self.die1.roll(10)) == 10 , "Die.Roll doesn't return the right number of results")

    def test_04_die_seeDie(self):
        '''Ensure that seeDie is the correct dimensions'''
        self.assertTrue(self.die1.seeDie().shape == (self.faces1.size, 2), "Die.seeDie returns the wrong number of faces.")

    die2 = montecarlo.Die(faces2)
    die3 = montecarlo.Die(faces3)

    def test_05_game_init(self):
        '''Ensure that a Game Object will not be created with non-matching dice'''
        with self.assertRaises(AssertionError):
            game0 = montecarlo.Game([self.die1, self.die2, self.die3])
    
    game1 = montecarlo.Game([die1, die1, die1, die1, die1])

    def test_06_game_play(self):
        '''Ensure that the dataframe created when a game is played has the correct shape given a known number of dice and rolls'''
        self.game1.play(10)
        self.assertTrue(self.game1.show().shape == (10, 5), "Shape of game results dataframe incorrect. Implies missing/incorrect data")

    def test_07_game_play(self):
        '''Check that shape of stacked dataframe is correct'''
        self.assertTrue(self.game1.show(True).shape == (50,), "Stacked data gives incorrect shape")

    game2 = montecarlo.Game([die3, die3, die3, die3])
    game2.play(10)
    analyzer1 = montecarlo.Analyzer(game2)

    def test_08_analyzer_init(self):
        '''Check that dtype of correct subtype is given when creating analyzer (Strings become object dtype)'''
        self.assertTrue(np.issubdtype(self.analyzer1.faceType(), np.object_), "Analyzer somehow saving incorrect dType information")

    def test_09_analyzer_jackpot(self):
        '''Check that the jackpot returns possible result'''
        self.assertTrue(0 <= self.analyzer1.jackpot() <= 10 , "Jackpot giving impossible result")

    def test_10_analyzer_combo(self):
        '''Check that sum of combo values adds up to number of rolls'''
        self.assertTrue(sum(self.analyzer1.combo()) == 10, "Combo is returning the wrong amount of values")

    def test_11_analyzer_faceCounts(self):
        '''Check that number of faceCounts columns equals number of known die faces'''
        self.assertTrue(self.analyzer1.faceCounts().columns.size == 2, "faceCounts has an incorrect number of die faces")

    def test_12_analyzer_faceType(self):
        '''Check that faceType is returning correct FaceType'''
        self.assertTrue(np.issubdtype(self.analyzer1.faceType(), np.object_), "Analyzer storing faceType incorrectly")

if __name__ == '__main__':
    
    unittest.main(verbosity=3)