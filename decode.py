#! /usr/bin/env python

#Decode an input morse code string that lacks spaces into meaningfull words

import encode
#Define dictionary to convert morse to char
morse_text = {'.-':'a',
              '-...':'b',
              '-.-.':'c',
              '-..':'d',
              '.':'e',
              '..-.':'f',
              '--.':'g',
              '....':'h',
              '..':'i',
              '.---':'j',
              '-.-':'k',
              '.-..':'l',
              '--':'m',
              '-.':'n',
              '---':'o',
              '.--.':'p',
              '--.-':'q',
              '.-.':'r',
              '...':'s',
              '-':'t',
              '..-':'u',
              '...-':'v',
              '.--':'w',
              '-..-':'x',
              '-.--':'y',
              '--..':'z',
              '.----':'1',
              '..---':'2',
              '...--':'3',
              '....-':'4',
              '.....':'5',
              '-....':'6',
              '--...':'7',
              '---..':'8',
              '----.':'9',
              '-----':'0'}


def findPossible(morse):
    
    solutions = []
    charList = list(morse)
    for char in charList:
        if not char == '.' and not char == '-':
            print("Error! bad morse code, only include '.' and '-'")
            return(None)

    ## The longest interpretation of the morse code will be all e and t with length = len(charList)
    for count in range(0,len(charList)):
        first = ''.join(charList[:len(charList) - count])
        solution = morse_text.get(first,'')
        if solution:
            solutions.append(solution)
            solution = ''
        
    return(solutions)



if __name__ == "__main__":
    # L = .-..
    # Possible interpretations of .-.. are:
    # L, AI, ED, RE, AEE, ENE, ETI, ETEE
    char = 'L'
    code = encode.encodeMorse(char)
    print("Origional input:")
    print(char + ': ' + code)
    print("Possible inputs:")
    print(findPossible(code))
