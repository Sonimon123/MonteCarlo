import numpy as np
import pandas as pd
import random
import itertools

"""Allows you to create and analyze Monte Carlo simulations"""

class Die():

    '''Creates a theoretical Die of any number of faces that can be set with various weights on each side and rolled.'''

    __faces = pd.DataFrame()

    def __init__(self, fArray):
        """Initializes dice using the Numpy ndarray of face names (with either a numeric or string dtype) provided, with all of the weights defaulting to 1"""
        assert type(fArray) == np.ndarray, "Input isn't ndarray"
        assert np.issubdtype(fArray.dtype, np.number) or np.issubdtype(fArray.dtype, np.string_) or np.issubdtype(fArray.dtype, np.unicode_), "Input does not have correct datatype"

        self.__faces = pd.DataFrame({'Face': fArray,
                                      'Weight': np.ones(fArray.size)})
    
    def setWeight(self, face, weight):
        """Sets the weight of the die face provided to the weight provided"""
        assert face in self.__faces.Face.values, "Face provided is not in list of faces"
        try:
            float(weight)
        except ValueError:
            print("Weights must be convertable to Floating Point Numbers.")
            return
        
        #Searches for the face in the list of weights with the name of the face given, then sets the weight to the given value
        self.__faces.loc[self.__faces['Face'] == face, 'Weight'] = weight

    def roll(self, count = 1):
        """'Rolls' the die you created, giving you a random face, with the chance of each face being determined by the weights in the dataframe"""
        assert type(count) == int

        out = []

        while count > 0:
            out.append(random.choices(self.__faces['Face'], self.__faces["Weight"]))
            count -= 1

        return out

    def seeDie(self):
        """Prints the faces and weights of the die"""
        return self.__faces

class Game():

    '''Allows you to save several Dice, roll them any given number of times, then see the outcome of those rolls'''

    dice = []
    __playframe = pd.DataFrame()

    def __init__(self, dList):
        #All inputs must be dice, and all die must have similar faces
        for x in dList:
            assert type(x) == Die or '__main__.Die', "All items in dList must be a Die"
            assert pd.Series.equals(x.seeDie()['Face'], dList[1].seeDie()['Face']), "All dice must have similar faces and number of faces"

        #Save list of dice
        self.dice = dList

    def play(self, runs):

        '''Rolls all of the dice in the game the specified amount of times, then saves the results to a private variable'''

        assert type(runs) == int, "Parameter must be an integer"

        #Create an Empty DataFrame with the correct Index and Column Names
        #Die Name is based on placement in list
        res = pd.DataFrame(columns=['Die ' + str(x) for x in range(1, len(self.dice)+1)], index=['Roll ' + str(x) for x in range(1, runs+1)])

        num = 1
        for x in self.dice:
            #For each die, roll it 'runs' times, then add the column to the dataframe
            runList = x.roll(runs)

            res["Die " + str(num)] = runList
            res["Die " + str(num)] = [x[0] for x in res["Die " + str(num)]]
            num += 1
        
        self.__playframe = res

    def show(self, narrow=False):

        '''Returns the results of the last game. Can either be given in a standard wide form or a stacked narrow form'''

        if narrow:
            return self.__playframe.stack()
        else:
            return self.__playframe


class Analyzer():

    '''Analyzes a Game object (that's already been played) and provides various pieces of information about it.'''

    game = Game([])
    comboDF = pd.DataFrame()
    jackpotDF = pd.Series()
    fcprDF = pd.DataFrame()
    __faceType = ''

    def __init__(self, game):
        '''Stores the game inside of itself, then stores the Numpy dtype of the Die Faces'''
        self.game = game
        self.__faceType = game.dice[0].seeDie()['Face'].dtype

    def jackpot(self):
        """Calculates how many times a roll ended in a Jackpot (all the same face), then stores this in the jackpotDF dataframe. Returns the number of successes"""
        res = pd.DataFrame(columns=['Jackpot?'], index=['Roll ' + str(x) for x in range(1, len(self.game.show().index) + 1)])
        jNum = 0
        
        for x in range(1, len(self.game.show().index) + 1):
            res.loc["Roll " + str(x), 'Jackpot?'] = (self.game.show().loc["Roll " + str(x)].astype(str).nunique() == 1)
            if res.loc["Roll " + str(x), 'Jackpot?']:
                jNum += 1
        self.jackpotDF = res
        return jNum

    def combo(self):
        """Calculates how many times each die outcome occured and stores the information in a dataframe. Returns the dataframe."""
        self.comboDF = self.game.show().value_counts()
        return self.comboDF

    def faceCounts(self):
        """Calculates how many times each face occured in each roll and stores it in a dataframe. Returns the dataframe."""
        fcprDF = self.game.show().T.apply(pd.value_counts).T
        return fcprDF

    def faceType(self):
        """Returns the Numpy dType of the die faces."""
        return self.__faceType
