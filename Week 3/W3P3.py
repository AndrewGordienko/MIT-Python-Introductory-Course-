'''
lettersGuessed: list, what letters have been guessed so far
returns: string, comprised of letters that represents what letters have not
yet been guessed.
'''

def getAvailableLetters(lettersGuessed):
    string = 'abcdefghijklmnopqrstuvwxyz'

    for char in lettersGuessed:
        string = string.replace(char, "")

    return string
