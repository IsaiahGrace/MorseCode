#! /usr/bin/env python

#Encode given input string into a morse code string without spaces

def encodeMorse(text):
    #Define dictionary to convert char to morse
    morse = {'a':'.-',
             'b':'-...',
             'c':'-.-.',
             'd':'-..',
             'e':'.',
             'f':'..-.',
             'g':'--.',
             'h':'....',
             'i':'..',
             'j':'.---',
             'k':'-.-',
             'l':'.-..',
             'm':'--',
             'n':'-.',
             'o':'---',
             'p':'.--.',
             'q':'--.-',
             'r':'.-.',
             's':'...',
             't':'-',
             'u':'..-',
             'v':'...-',
             'w':'.--',
             'x':'-..-',
             'y':'-.--',
             'z':'--..',
             '1':'.----',
             '2':'..---',
             '3':'...--',
             '4':'....-',
             '5':'.....',
             '6':'-....',
             '7':'--...',
             '8':'---..',
             '9':'----.',
             '0':'-----'}
    #prepare input string, convert to lowercase and strip whitespace
    text = text.lower()
    words = text.split()
    wordsList = [word.strip() for word in words]
    text = ''.join(wordsList)
    code = []
    #iterate through the text and encode the characters
    for char in text:
        if not char in morse.keys():
            print("Error! invalid input, only letters and numbers allowed")
            return(None)
        code.append(morse[char])
        
    return(''.join(code))


if __name__ == "__main__":
    print(encodeMorse("Test One"))
