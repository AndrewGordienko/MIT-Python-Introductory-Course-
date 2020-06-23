def isWordGuessed(secretWord, lettersGuessed):
    count = 0

    for i in range (len(secretWord)):
      count += lettersGuessed.count(secretWord[i])

    if count >= len(secretWord):
      return True

    else:
      return False