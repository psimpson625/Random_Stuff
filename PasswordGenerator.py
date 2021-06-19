#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 11:16:26 2021

@author: patricksimpson
"""

# Creating a strong password:
import random
import math
import numpy as np
from scipy import stats


# There are 4 types of characters: lowercase, uppercase, numeric, special chars
# Can edit which characters you want available in the password:
lowercase='abcdefghijklmnopqrstuvwxyz'
uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeric='1234567890'
special='!@#$%^&*'


# We will use urn randomization to determine which character we pick
# This ensures multiple character types are used,
    # although perfect balance will not exist in small samples

# The initial urn
# If we want password of length 7:
    # 2 Lowercase, 2 Uppercase, 2 Numeric, 1 Special, etc.
# This function returns a list - [2, 2, 2, 1]
def urn(size):
    low = math.floor(size/4)
    high = math.ceil(size/4)
    if size%4 == 1:
        nums = [high, low, low, low]
    elif size%4 == 2:
        nums = [high, high, low, low]
    elif size%4 == 3:
        nums = [high, high, high, low]
    else:
        nums = [high, high, high, high]
    return(nums)


# The probabilites on choosing each category in the urn
# Initial probabilities for password of length 7:
    # (.2857, .2857, .2857, .1429)
    # This function returns a tuple

def probs(nums): # Taking a list of 4
    probs=[]
    for i in range(len(nums)):
        probs.append(nums[i]/sum(nums))
    return(tuple(probs))



# We use numbers to represent Lowercase/Uppercase/Numeric/Special
# 0/1/2/3
# If we have a list of numbers, this function converts in to a string 
# with character representation

def change(selections):
    string_selections=''
    dict={
        0:'L',
        1:'U',
        2:'N',
        3:'S'}
    for num in selections:
        string_selections=string_selections + dict.get(num)
        
    return(string_selections)


# Function to obtain what characters will be used in password
def picks(length):
    picks=[] #initializing
    
    xk = np.arange(0,4) #0 represents LC, 1 UC, 2 NC, 3 SC
    balls=urn(length)
    
    for i in range(1, length+1):
        pk=probs(balls) #initial probabilities for each character type
        custm = stats.rv_discrete(name='custm', values=(xk, pk))
        pick=custm.rvs(size=1)[0] # first selection
        picks.append(pick)
        # Now we adjust the number of balls in the urn
        # If a ball is selected, we remove it from urn
        # An additional ball is added to urn for the other 3
        # Now probabilities will be different for next selection
        for j in range(len(balls)): 
            if j == pick:
                balls[j] = balls[j] - 1
            else:
                balls[j] = balls[j] + 1
        
    #Randomizing order of list. This reduces bias of order    
    random.shuffle(picks) 
    chars=change(picks) #Changing list of numbers to string of characters     
    return(chars)


# This function returns a password. The default length is 20.
# Length can be any integer. If length <=0 an empty string is returned
def password(length=20):
    password='' #initializing the password
    # Characters
    selections=picks(length) #Obtaining string of letters ('L', 'U', 'N', 'S')
    
    for letter in selections:
        if letter == 'L':
            password = password + lowercase[random.randint(0,len(lowercase)-1)]
        elif letter == 'U':
            password = password + uppercase[random.randint(0,len(uppercase)-1)]
        elif letter == 'N':
            password = password + numeric[random.randint(0,len(numeric)-1)]
        elif letter == 'S':
            password = password + special[random.randint(0,len(special)-1)]
            
    return(password)
    
    
