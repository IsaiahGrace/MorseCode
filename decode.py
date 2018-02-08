#! /usr/bin/env python

#Decode an input morse code string that lacks spaces into meaningfull words

import anytree as tree
import enchant
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

def buildTree(node, code):
    for key in morse_text.keys():
        if list(key) == code[:len(key)]:
            newNode = tree.Node(morse_text[key])
            newNode.parent = node
            buildTree(newNode, code[len(key):])
    return()

def buildSolutions(solutions, node):
    if node.is_leaf:
        solution = ''
        for ancestor in node.ancestors:
            solution += ancestor.name
        solution += node.name
        solutions.add(solution)
    else:
        for child in node.children:
            buildSolutions(solutions, child)
    return(None)

def findPossible(morse):
    solutions = set()
    charList = list(morse)
    for char in charList:
        if not char == '.' and not char == '-':
            print("Error! bad morse code, only include '.' and '-'")
            return(None)
    root = tree.Node('')
    buildTree(root, charList)
    buildSolutions(solutions, root)
    #for pre,fill,node in tree.RenderTree(root):
    #    print("%s%s" % (pre, node.name))    
    return(solutions)

def findWords(solutions):
    dictionary = enchant.Dict("en_US")
    words = set()
    for word in solutions:
        if dictionary.check(word):
            words.add(word)
    return(words)

if __name__ == "__main__":
    # L = .-..
    # Possible interpretations of .-.. are:
    # L, AI, ED, RE, AEE, ENE, ETI, ETEE
    char = 'computer'
    code = encode.encodeMorse(char)
    solutions = findPossible(code)
    print("Origional input:")
    print(char + ': ' + code)
    print("Number of possible solutions:")
    print(len(solutions))
    print("Words found:")
    print(findWords(solutions))
