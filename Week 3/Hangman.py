# Hangman game with all the pieces together


import random

WORDLIST_FILENAME = "C:/Users/andrew/Desktop/New Folder/words.txt"

def loadWords():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    count = 0

    for i in range (len(secretWord)):
      count += lettersGuessed.count(secretWord[i])

    if count >= len(secretWord):
      return True

    else:
      return False


def getGuessedWord(secretWord, lettersGuessed):
    endresult = ''

    for i in range(len(secretWord)):
      count = lettersGuessed.count(secretWord[i])
      if count > 0:
        endresult += secretWord[i]
      else:
        endresult += ' _'
      count = 0
    
    return (endresult)


def getAvailableLetters(lettersGuessed):
    string = 'abcdefghijklmnopqrstuvwxyz'

    for char in lettersGuessed:
        string = string.replace(char, "")

    return string


def hangman(secretWord):
  guesses = 8
  init_guesses = guesses
  lettersGuessed = ''
  count = 0

  print ("Welcome to the game, Hangman!")
  print ("I am thinking of a word that is {} letters long".format(len(secretWord)))

  while True:
    if isWordGuessed(secretWord, lettersGuessed) == True:
      print ("------------")
      print ("Congratulations, you won!")
      break

    for i in range(guesses):
      print ("You have {} guesses left.".format(init_guesses))
      print ("Available letters: {}".format(getAvailableLetters(lettersGuessed)))
      print ("Please guess a letter")

      value = input()

      for i in range(len(lettersGuessed)):
        if value == lettersGuessed:
          print ("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, lettersGuessed)))
          print ("------------")
          guesses += 1
          init_guesses += 1
        

      for i in range (len(secretWord)):
        if secretWord[i] == value:
          count += 1
      
      lettersGuessed += value
      
      if count > 0:
        print ("Good Guess: {}".format(getGuessedWord(secretWord, lettersGuessed)))
        print ("------------")
      else:
        print ("Oops! That letter is not in my word: {}".format(getGuessedWord(secretWord, lettersGuessed)))
        print ("------------")
      
      init_guesses -= 1
      
    if init_guesses == 0:
      print ("------------")
      print ("Sorry, you have run out of guesses!")
      break

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
