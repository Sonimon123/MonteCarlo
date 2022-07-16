# Monte Carlo Simulator

By JR Kargbo


# Synopsis
This class allows the user to create and run Monte Carlo Simulations with customizable Dice and Weights, as well as giving some options to analyze the results of your game in various ways.

## Installing
```bash
pip install -e <Path where you saved MonteCarlo>
```
Note that you must have Numpy and Pandas installed in order to use MonteCarlo.

## Importing
```python
import MonteCarlo
```
The 3 MonteCarlo classes (Die, Game, and Analyzer) are automatically imported when you import MonteCarlo.

## Creating Dice
```python
coinArray = np.array(['heads', 'tails'])

coin = MonteCarlo.Die(coinArray)
```
Input to initialize a Die must be in np.array format.

## Setting the Weight of a Face
```python
coin.setWeight(<Face>, <Weight>)
```
'Face' should be replaced with a value that exists in the ndarray you initialized the Die with, otherwise it will give you an error. Weight can be any numeric value.

## Seeing the Die Faces and Weights
```python
coin.seeDie()
```
This returns the Faces and Weights of the Die in a DataFrame Format.

## Rolling the Die
```python
coin.roll(<number of outcomes=1>)
```
By default, rolling the die will give you a single result in a list. However, if you enter an integer as a parameter, it will return a list of results of that length. A result is a single face from the die, pulled at random based on the assigned weights.

## Creating a Game
```python
coinGame = MonteCarlo.Game([coin, coin])
```
You can create a game with multiple dice by passing them as a list into MonteCarlo. Note that all Dice must be of the same data type and have the same faces, though their weights can be different.

## Playing a Game
```python
coinGame.play(<number of rolls>)
```
This will let you roll all of the dice in your game the number of times specified, and then saves the results to a private DataFrame.

## Seeing the results of the Game
```python
coinGame.show(<narrow=False>)
```
This lets you view the results of your game. If you provide True to the narrow parameter, it will give you the results in a narrower, stacked format.

## Creating an Analyzer
```python
analyzer1 = MonteCarlo.Analyzer(coinGame)
```
You can create an Analyzer object to give stats about a game by passing the game as an argument. Please only pass a single game. You must play the game and generate results before creating the analyzer.

## Getting Jackpot information
```python
analyzer1.jackpot()
analyzer1.jackpotDF
```
The Jackpot method calculates the amount of time that a roll ended with all die having the same face. It returns the number of jackpots that occurred. If you need the actual table of results, after creating the results, they can be referenced again with analyzer.jackpotDF


## Getting Combo information
```python
analyzer1.combo()
analyzer1.comboDF
```
The Combo method calculates and displays unique combinations of outcomes created by the game as a Series. If you wish to see this information later, it's saved in analyzer.comboDF.


## Getting Face Count Information
```python
analyzer1.faceCounts()
analyzer1.fcDF
```
The faceCounts method returns the amount of times each face gets rolled and displays it as a DataFrame. If you wish to see this information later, it's saved in analyzer.fcprDF

## Getting Data Type of dice used in Analyzer
```python
analyzer1.faceType()
```
This returns the dType of the dice used in the current game.

# API Description

## Class: Die

Creates a theoretical Die of any number of faces that can be set with various weights on each side and rolled.

### .setWeight()
Sets the weight of the die face provided to the weight provided
```python
<die>.setWeight(<face>, <int weight>)
returns None
```
### .roll()
'Rolls' the die you created, giving you a random face, with the chance of each face being determined by the weights in the dataframe
```python
<die>.roll(<int count = 1>)
returns [int]
```
### .seeDie()
Prints the faces and weights of the die
```python
<die>.seeDie()
returns pandas.DataFrame
```

## Class Game
Allows you to save several Dice, roll them any given number of times, then see the outcome of those rolls

### .dice
List of dice in the game. Is a public Python list.

### .play()
Rolls all of the dice in the game the specified amount of times, then saves the results to a private variable
```python
<game>.play(<int runs>)
returns None
```

###.show()
Returns the results of the last game. Can either be given in a standard wide form or a stacked narrow form
```python
<game>.show(<bool narrow>)
returns pandas.DataFrame
```

## Class: Analyzer
Analyzes a Game object (that's already been played) and provides various pieces of information about it.

### .game
The game currently being analyzed

### .comboDF
DataFrame containing calculated Combos information

### .jackpotDF
Series containing calculated Jackpot information

### .fcprDF
DataFrame containing calculated Face Counts information


### .jackpot()
Calculates how many times a roll ended in a Jackpot (all the same face), then stores this in the jackpotDF dataframe. Returns the number of successes
```python
<analyzer>.jackpot()
returns pandas.Series
```

### .combo()
Calculates how many times each die outcome occured and stores the information in a dataframe. Returns the dataframe.
```python
<analyzer>.combo()
returns pandas.DataFrame
```
### .faceCounts()
Calculates how many times each face occured in each roll and stores it in a dataframe. Returns the dataframe.
```python
<analyzer>.faceCounts()
returns pandas.DataFrame
```
### .faceType()
Returns the Numpy dType of the die faces.
```python
<analyzer>.faceType()
returns numpy.dtype
```

# Manifest

 - MonteCarlo
	 - test
		 - montecarlo_test.py
	 - MonteCarlo.py
- LICENSE
- montecarlo_scenarios.ipynb
- README.md
- setup.py
