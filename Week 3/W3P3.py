def getAvailableLetters(lettersGuessed):
    string = 'abcdefghijklmnopqrstuvwxyz'

    for char in lettersGuessed:
        string = string.replace(char, "")

    return string