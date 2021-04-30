#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 20:41:01 2021

@author: patricksimpson
"""

# Implement function cheer() that takes as input a team name (as a string) 
#and prints a cheer as shown:
#>>> cheer('Huskies')
#How do you spell winner?
#I know, I know!
#H U S K I E S!
#And that's how you spell winner! Go Huskies!

def cheer(teamname):
    """ Cheer for Huskies:
    >>> cheer('Huskies')
    How do you spell winner?
    I know, I know!
    H U S K I E S!
    And that's how you spell winner!
    Go Huskies!
    """
    start='How do you spell winner?' #line 1 of chant
    second='I know, I know!' #line 2 of chant 
    third="And that's how you spell winner!" #line 3 of chant
    newline='\n' #used to create linebreaks while using f-string
    
    #getting teamchant eg. 'H U S K I E S!'
    teamchant=''
    for letter in teamname:
        teamchant=teamchant+' '+letter.upper()
    
    #Our printed chant using f-string
    message=(
        f"{start}{newline}"
        f"{second}{newline}"
        f"{teamchant.lstrip()+'!'}{newline}"
        f"{third}{newline}"
        f"{'Go '+teamname+'!'}"
        )
    return(print(message))
    
    
#The cryptography function crypto() takes as input a string 
#(i.e., the name of a file in the current directory). 
#The function should print the file on the screen with this modification: 
#Every occurrence of string 'secret' in the file should be replaced with string 'xxxxxx'

def crypto(filepath):
    with open(filepath, 'r') as file:
        data=file.read().replace('secret', 'xxxxxx').replace('\n','')
    return(data)

    

#Implement function links() that takes as input the name of an HTML file 
#(as a string) and returns the number of hyperlinks in that file. 
#To do this you will assume that each hyperlink appears in an
#anchor tag. You also need to know that every anchor tag ends with the substring </a>. 

def links(htmlpath):
    import codecs
    as_string=codecs.open(htmlpath, 'r').read()
    return(as_string.count('</a>')) #returning number of hyperlinks
    


#Implement function duplicate() that takes as input the name (a string) of a 
#file in the current directory and returns True if the file contains duplicate words 
#and False otherwise.

def duplicate(filepath):
    listOfWords = [] #Going to add all words in .txt file to a list
    with open(filepath, "r") as f:
        listOfWords = f.read().lower().replace('.','').replace(',','').replace('?','').split()
                                        #lower makes everything lowercase
                                        #Getting rid of punctuation with replace
                                        #Split at end puts words to list
    
    setOfwords=set() #will add word to setOfWords if not already in setOfWords
    for word in listOfWords:
        if word in setOfwords:
            return True #if the word is already in set, we have a duplicate!-return True
        else:
            setOfwords.add(word)
    return False #if we never find a match when adding word to set, no duplicates-False
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    