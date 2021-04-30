#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 18:29:34 2021

@author: patricksimpson
"""

#Write a function vowelIndex that accepts a word (a str) 
#as an argument and returns the index of the first vowel in the word. 
#If there is no vowel, -1 is returned. For this problem, both upper and lower case v
#owels count, and 'y' is not considered to be a vowel.

def vowelIndex(word):
    vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] #list of vowels
    for letter in word: #iterating through each letter of word
        if letter in vowels: #if the letter is a vowel...
            output=word.index(letter) #finding index of vowel
            break #Ending loop and outputting index of first vowel
        else: #if not a vowel, setting output to -1. Note: this will not be the output unless no vowels exist in word. (Will eventually be overwritten in loop)
            output=-1
    return(output)

            
#Write a function flipCase that accepts a word as an argument and returns 
#the same word but with each upper case letter switched to lower case and vice-versa. 

def flipCase(word):
    output='' #null string to store our output
    for letter in word: #iterating through each letter in the word
        if letter.isupper(): #if letter is uppercase:
            output=output+letter.lower() #making it lowercase and adding it to output
        else: #if letter is lowercase:
            output=output+letter.upper() #making it uppercase and adding it to output
    return(output) #returning out flipped word


#Write a function palindromes that accepts a sentence as an argument. 
#The function then returns a list of all words in the sentence that are palindromes, 
#that is they are the same forwards and backwards.

def palindromes(sentence):
    import string
    no_punctuation=sentence.translate(str.maketrans('','', string.punctuation)) #stripping punc.
    list_of_words=no_punctuation.split(' ') #creating list of words in sentence
    output_list=[] #we will put each palindrome in this list
    for word in list_of_words: #iterating through each word
        if word.lower()==word[::-1].lower(): #checking to see if word forward=word backward (Note: must make sure every character is either lower/uppercase)
            output_list.append(word) #if palindrome, add to our list
    return(output_list)


#Write a function squares that accepts a 2-dimensional list of integers or 
#a list of ranges as an input, and that returns the count of all the integers 
#that are perfect squares.

def squares(nested): #input is a nested list
    import math
    count=0 #will accumulate the number of perfect squares 
    for nest in nested: #there are multiple nests within the nested list
        for number in nest: #there are multiple numbers within each nest
            if math.floor(math.sqrt(number))==math.ceil(math.sqrt(number)):#if this is true we have a perfect square
                count=count+1 #we have another perfect square-add to counter   
    return(count)
    

#Write a function rps that returns the result of a game of "Rock, Paper, Scissors". 
#The function accepts two arguments, each one of 'R','P','S' , that represents the 
#symbol played by each of the two players. The function returns:
#  -1 if the first player wins
# 0 if a tie
# 1 if the second player wins

def rps(a,b):
    a_b=a+b #Concatenating each "move"
    mydict = { #Dictionary will store outputs if we have a winner
    'RP': 1,
    'RS': -1,
    'PR': 1,
    'PS': -1,
    'SR': -1,
    'SP': 1}
    if a==b: #if players make same move output=0 (tie)
        output=0
    else: #else we go into created dictionary to get output
        output=mydict.get(a_b)
    return(output)
    
