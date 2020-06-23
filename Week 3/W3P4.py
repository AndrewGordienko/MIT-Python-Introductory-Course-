'''
secretWord: string, the secret word to guess.

Starts up an interactive game of Hangman.

* At the start of the game, let the user know how many 
letters the secretWord contains.

* Ask the user to supply one guess (i.e. letter) per round.

* The user should receive feedback immediately after each guess 
about whether their guess appears in the computers word.

* After each round, you should also display to the user the 
partially guessed word so far, as well as letters that the 
user has not yet guessed.

Follows the other limitations detailed in the problem write-up.
'''

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
