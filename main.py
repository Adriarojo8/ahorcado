def ahorcado():

    lword = 0
    word = ""
    wordArray = []

    print("Introduce your word: ")

    word = input()

    lword = calculateLengthWord(word)

    wordArray = createArray(lword)

    startGame(word, lword, wordArray)


def calculateLengthWord(word):

    lword = 0

    for i in word:
        lword += 1

    return lword

def createArray(lword):

    array = []

    for i in range(lword):
        array.append(False)

    return array

def checkIfFound(array):

    for i in array:
        if i == False:
            return False
    return True

def startGame(word, lword, wordArray):

    print("WELCOME TO HANGED: THE GAME!")
    print("The word that you must guess has " , lword , " letters!")
    print("LET THE FUN BEGIN!")

    maxMistakes = 10
    mistakes = 0
    wordFound = False
    letter = ""

    while(mistakes < maxMistakes and not wordFound):
        letter = input("Introduce a letter: ")
        print("You've choosed " , letter)




ahorcado()