'''
secretWord: string, the word the user is guessing
lettersGuessed: list, what letters have been guessed so far
returns: string, comprised of letters and underscores that represents
what letters in secretWord have been guessed so far.
'''

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
