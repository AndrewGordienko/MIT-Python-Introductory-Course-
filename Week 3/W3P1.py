'''
secretWord: string, the word the user is guessing
lettersGuessed: list, what letters have been guessed so far
returns: boolean, True if all the letters of secretWord are in lettersGuessed;
False otherwise
'''

def isWordGuessed(secretWord, lettersGuessed):
    count = 0

    for i in range (len(secretWord)):
      count += lettersGuessed.count(secretWord[i])

    if count >= len(secretWord):
      return True

    else:
      return False
