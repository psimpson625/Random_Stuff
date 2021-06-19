#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 22:09:38 2021

@author: patricksimpson
"""

# Develop a class Volume that stores the volume for a stereo that has a value
# between 0 and 11. You must guarantee that:
    # The numeric value of the Volume is set to a number between 0 and 11. Any
    # attempt to set the value to greater than 11 will set it to 11 instead.
    # Any attempt to set a negative value will instead set it to 0.

class Volume:
    def __init__(self, volume=0):
        """
        Sets to a given numeric value, defaults to 0
        
        >>> v = Volume()
        >>> v
        Volume(0)
        
        >>> v = Volume(20)
        >>> v
        Volume(11)
        
        >>> v = Volume(-1)
        >>> v
        Volume(0)
        """
        if volume < 0:
            volume = 0
        elif volume > 11:
            volume = 11

        self.volume = volume
        
    def __repr__(self):
        """
        Converts Volume to a str for display
        """
        return "Volume({self.volume})".format(self=self)
    
    def __eq__(self, other):
        """
        Returns True if the two Volumes have the same value
        
        >>> v = Volume(5)
        >>> v.up(1.1)
        >>> v == Volume(6.1)
        True
        
        >>> Volume(3.1) == Volume(3.2)
        False
        """
        if self.volume == other.volume:
            return True
        else:
            return False

    def get(self):
        """
        Returns the numeric value of the Volume
        """
        return self.volume

    def set(self, amount):
        """
        Sets the volume to the specified argument
        Subject to 0 <= vol <= 11 constraint
        
        >>> v = Volume()
        >>> v.set(5.3)
        >>> v
        Volume(5.3)
        
        >>> v.get()
        5.3
        
        >>> v.get() == 5.3
        True
        """
        if amount > 11:
            self.volume = 11
        elif amount < 0:
            self.volume = 11
        else:
            self.volume = amount

    def up(self, amount1):
        """
        Given a numeric amount, increases the Volume by that amount.
        Subject to 0 <= vol <= 11 constraint
        
        >>> v = Volume(4.5)
        >>> v
        Volume(4.5)
        
        >>> v.up(1.4)
        >>> v
        Volume(5.9)
        
        >>> v.up(6)
        >>> v
        Volume(11)
        """
        if self.volume + amount1 > 11:
            self.volume = 11
        elif self.volume + amount1 < 0:
            self.volume = 0
        else:
            self.volume = self.volume + amount1

    def down(self, amount):
        """
        Given a numeric amount, decreases the Volume by that amount.
        Subject to 0 <= vol <= 11 constraint
        
        >>> v = Volume(11)
        >>> v
        Volume(11)
        
        >>> v.down(3.5)
        >>> v
        Volume(7.5)
        
        >>> v.down(10)
        >>> v
        Volume(0)
        """
        if self.volume-amount > 11:
            self.volume = 11
        elif self.volume-amount < 0:
            self.volume = 0
        else:
            self.volume = self.volume - amount


# Write a standalone function partyVolume() that takes accepts one argument, 
# a string containing the name of a file. The objective of the function is to 
# determine the a Volume object that is the result of many people at a party 
# turning the Volume up and down. More specifically: the first line of the file is a
# number that indicates the initial value of a Volume object. The remaining lines 
# consist of a single character followed by a space followed by a number. 
# The character will be one of ‘U” or ‘D’ which stand for “up” and “down” respectively. 
# The function will create a new Volume object and then process each line of the 
# file by calling the appropriate method of the Volume object which changes the 
# value of the Volume. The function then returns the final Volume object.



def partyVolume(filepath):
    """
    >>> partyVolume('party1.txt')
    Volume(6.35)
    
    >>> partyVolume('party2.txt')
    Volume(3.75)
    
    >>> partyVolume('party3.txt')
    Volume(0.75)
    
    >>> partyVolume('party1.txt') == Volume(6.35)
    True
    
    >>> partyVolume('party2.txt') == Volume(3.75)
    True
    
    >>> partyVolume('party3.txt') == Volume(0.75)

    """
    file = open(filepath, "r").readline() #first line of file
    start_volume = Volume(float(file[:file.find('\n')])) #Initializing Volume
    file_rest=open(filepath, "r").readlines() #Each line of file
    
    for i in range(1, len(file_rest)): #Starting with second line
        if file_rest[i][0] == 'U': #if 'U' we use up, else down
            start_volume.up(float(file_rest[i][2:]))
        else:
            start_volume.down(float(file_rest[i][2:]))
            
    return(start_volume)
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()