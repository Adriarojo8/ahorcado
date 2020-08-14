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

def checkIfContains(letter,word):

    for i in word:
        if i == letter:
            return True
    return False

def updateArray(array,word,letter):

    index = 0
    for i in word:
        if i == letter:
            array[index] = letter
        index += 1

    return array

def showWord(array):

    word = ""
    for i in array:
        if i == False:
            word += " _ "
        else:
            word += " " + i + " "

    return word

def arrayToString(array):

    string = ""

    for i in array:
        string += i + " "

    return string

def checkIfLetterUsed(array,letter):

    for i in array:
        if i == letter:
            return True
    return False

def startGame(word, lword, wordArray):

    print("WELCOME TO HANGED: THE GAME!")
    print("The word that you must guess has " , lword , " letters!")
    print("LET THE FUN BEGIN!")

    maxMistakes = 10
    mistakes = 0
    wordFound = False
    letter = ""
    wordToShow = ""
    lettersArray = []
    lettersUsed = ""

    while(mistakes < maxMistakes and not wordFound):
        letter = input("Introduce a letter: ")
        #lettersArray.append(letter)
        #if(checkIfLetterUsed(letter)):
        while(checkIfLetterUsed(lettersArray,letter)):
            print("You've used this letter before!")
            print("Choose another please")
            print("remember you used this letters: ")
            lettersUsed = arrayToString(lettersArray)
            print(lettersUsed)
            letter = input("Introduce a letter: ")
        lettersArray.append(letter)
        print("You've choosed " , letter)
        if (checkIfContains(letter,word)):
            print("Nice, you're right!")
            wordArray = updateArray(wordArray,word,letter)
        else:
            print("Ouch, you're wrong!")
            mistakes += 1
            print("You have", 10-mistakes, "mistakes left")
        wordToShow = showWord(wordArray)
        print("You are at this point:")
        print(wordToShow)
        print("You used these letters: ")
        lettersUsed = arrayToString(lettersArray)
        print(lettersUsed)

        if(checkIfFound(wordArray)):
            wordFound = True

    if(wordFound):
        print("CONGRATULATIONS!")
        print("YOU'VE FOUND THE WORD!")
        print("As you saw, the word was", word)
        print("I hope you enjoyed, see you soon!")
    else:
        print("I'm sorry, but you've reached the maximum of tries...")
        print("The word you were looking for was", word)
        print("If you want to try again, start again!")
        print("See you soon!")

ahorcado()


#añadir cola para saber que letras se han intentado, printar esa cola a cada ronda para no repetir - DONE
#tambien habra que tener en cuenta que no se puedan repetir letras ya dichas y que no esten en la cola, es decir, las acertadas
#añadir espacio entre jugadas, texto en color...
#a la cola para mostrar las letras usadas, hay que añadir la modificacion de que si la letra se ha acertado, no se muestre
#en la lista pero que si sea añadida a la cola, para evitar que los usuarios retrasados se equivoquen
#añadir separacion entre jugadas para evitar confusion