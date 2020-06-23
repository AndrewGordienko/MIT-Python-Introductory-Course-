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