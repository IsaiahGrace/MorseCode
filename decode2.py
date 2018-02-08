#! /usr/bin/env python
import sys
import enchant
import encode

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

def decode(encoded, curstring, end):
    temp = ""
    count = 0
    solutions = []
    for c in encoded:
        count = count + 1
        if morse_text.get(encoded[end:count]):
            solutions.extend(decode(encoded, curstring + morse_text.get(encoded[end:count]), count))
    solutions.append(curstring)
    return solutions

def findWords(solutions):
    dictionary = enchant.Dict("en_US")
    words = []
    for word in solutions:
        if word != "":
            if dictionary.check(word):
                print word
                words.append(word)
    return(words)

if __name__ == "__main__":
    printall = 0
    if len(sys.argv) < 2:
        print ("Usage: python decode2.py <string> (optional printall flag 0 or 1)")
        exit()
    if (len(sys.argv) > 2):
        if sys.argv[2] == 1:
            printall = 1
    teststring = sys.argv[1]
    print("\nOriginal String:\n" + teststring)
    encoded = encode.encodeMorse(teststring)
    print("Encoded String:\n" + encoded)
    solutions = decode(encoded, "", 0)
    if printall:
        print("Decoded String Possibilities:")
        print '[%s]' % ', '.join(map(str, solutions)) + "\n"
    print("Possible Words:")
    print(findWords(solutions))
