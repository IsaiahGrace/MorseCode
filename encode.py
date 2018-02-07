#! /usr/bin/env python

#Encode given input string into a morse code string without spaces

def encodeMorse(text):
    text = text.lower()
    words = text.split()
    wordsList = [word.strip() for word in words]
    text = ''.join(wordsList)
    
    return(text)


if __name__ == "__main__":
    print(encodeMorse("Test One"))
