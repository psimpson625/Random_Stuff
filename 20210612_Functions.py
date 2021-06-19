# Question 1: Implement a function 'ingredients' that takes a recipe
# and returns a dictionary of the ingredients needed.



def ingredients(recipe):
    """
   >>> ganache = 'semi-sweet chocolate: 224g\\nheavy cream: 224g\\nChop chocolate, place in a bowl. Heat cream until it simmers.\\nAdd cream to bowl, let stand for 3 minutes, then whisk until smooth.'

   >>> sourdoughStarter= 'Mix\\nflour: 113g\\nwater: 113g\\nCover loosely and let sit for 24 hours.\\nDiscard 1/2 of the starter and add\\nflour: 113g\\nwater: 113g\\nMix and let sit for 24 hours. \\nDiscard 1/2 of the starter and add\\nflour: 113g\\nwater: 113g\\nMix and let sit for 24 hours. \\nRepeat a bunch of times ...' 

   {'semi-sweet chocolate': '224', 'heavy cream': '224'}

   >>> ingredients(sourdoughStarter)
   {'flour': '339', 'water': '339'}

    """

    my_dict = dict()

    steps = recipe.split('\n')  # Splitting recipe into list of steps

    for step in steps:
        if step[-1] == 'g':  # This is an ingredient line - ends in 'g'
            colon_index = step.find(':')
            ingredient = step[0:colon_index]
            # amount is rest of string. remove :, spaces, and g
            amount = step[colon_index:].replace('g', '').replace(': ', '')

            # Checking if ingredient already exists in dictionary
            if ingredient in my_dict:
                # adding to current amount
                current_amount = int(my_dict.get(ingredient)) + int(amount)
                # updating value for this key
                my_dict[ingredient] = str(current_amount)

            else:
                my_dict[ingredient] = amount
    return my_dict



# Question 2: pairsThatSum
# Implement a function that accepts two arguments: A target number and a list
# of numbers. The function then returns a list of tuples that contains all pairs
# of number from the list that sum to the given target number. Note:
    # the pair can be two numbers with the same value, e.g. (2,2) but these must
    # be different items in the list
    
    # each pair should be reported only once
    
    # each pair's values should be listed in the order that they occur in the list
    # e.g. if 0 comes before 4 the pair recorded should be (0,4)

def pairsThatSum(target, number_list):
    """
    >>> pairsThatSum(3, [0,1,2,3])
    [(0, 3), (1, 2)]
    
    >>> pairsThatSum(6, [0,1,2,3])
    []
    
    >>> pairsThatSum(4, [0,1,2,3,4,2])
    [(0, 4), (1, 3), (2, 2)]
    """
    tuple_list = []
    
    for i in range(len(number_list)):
        for j in range(i+1, len(number_list)):
            if number_list[i] + number_list[j] == target:
                a_tuple = (number_list[i], number_list[j])
                tuple_list.append(a_tuple)
        
    return tuple_list








# Question 3: rollsToRepeat:
# Implement a function rollsToRepeat that simulates a dice game in which a pair
# of dice are rolled repeatedly until some total on the dice occurs the
# specified number of times

def rollsToRepeat(n):
    """
   >>> import random
   >>> random.seed(85)
   >>> rollsToRepeat(1)
   1
   >>> random.seed(85)
   >>> rollsToRepeat(2)
   4
   >>> random.seed(85)
   >>> rollsToRepeat(3)
   6
   >>> [ (i, random.seed(i), rollsToRepeat(i+1)) for i in range(10)]
   [(0, None, 1), (1, None, 7), (2, None, 8), (3, None, 8), (4, None, 19), (5, None, 29), (6, None, 31), (7, None, 30), (8, None, 36), (9, None, 39)]
    """
    
    import random
    
    rolls = []

    while True:
        dice1 = random.randint(1,6) # Dice 1 roll
        dice2 = random.randint(1,6) # Dice 2 roll
        the_sum = dice1 + dice2
        rolls.append(the_sum)
        if rolls.count(the_sum) == n:
            break

    return len(rolls)




# Question 4: KitKat
# Implement a class KitKat that represents a KitKat candy bar
# Each KitKat object will keep track of the flavor of the candy bar as well
# as the number of fingers (sections) remaining, an integer that defaults
# to 4

class KitKat:
    def __init__(self, flavor='Milk Chocolate', fingers=4):
        """
        flavor - defaults to 'Milk Chocolate'
        fingers - number of fingers remaining, defaults to 4
                  given non-negative
                  
        >>> candy = KitKat() #using both defaults
        >>> candy
        KitKat('Milk Chocolate', 4)
        
        >>> candy = KitKat('Green Tea', 3) # flavor and fingers both specified
        >>> candy
        KitKat('Green Tea', 3)
        
        >>> candy = KitKat('Mint') #flavor specified, fingers default to 4
        
        >>> candy
        KitKat('Mint', 4)
        """
        self.flavor = flavor
        self.fingers = fingers
        
    def __repr__(self):
        return f"KitKat('{self.flavor}', {self.fingers})"
    
    def eat(self, number=1):
        """
        Allows one to eat one or more fingers/sections of a KitKat
        Accepts one optional argument, the number of fingers to eat
            Defaults to 1 if no argument is supplied
        Returns a list containing copies of the flavor, one per finger that
        was eaten
        
        >>> candy = KitKat('Green Tea', 4)
        
        >>> candy.eat() # defaults to 1
        ['Green Tea']
        
        >>> candy
        KitKat('Green Tea', 3)
        
        >>> candy.eat(4) # try to eat 4, but only 3 there, so eat 3
        ['Green Tea', 'Green Tea', 'Green Tea']
        
        >>> candy
        KitKat('Green Tea', 0)
        
        >>> candy.eat() # nothing left to eat
        []
        
        >>> candy
        KitKat('Green Tea', 0)
        """
        if number > self.fingers:
            number = self.fingers
        output = []
        for i in range(0, number):
            output.append(self.flavor)
            self.fingers -= 1
        return output
    
    def __eq__(self, other):
        """
        Accepts two KitKat objects and returns True iff the have same # of fingers
        
        >>> KitKat('Green Tea', 3) == KitKat('Mint', 3)
        True
        
        >>> KitKat('Green Tea', 3) == KitKat('Mint', 2)
        False
        """
        if self.fingers == other.fingers:
            return True
        else:
            return False
        
    def __gt__(self, other):
        """
        Accepts two KitKat objects and returns True if the first KitKat
        has strictly more fingers than the second KitKat
        
        >>> KitKat('Green Tea', 3) > KitKat('Mint', 3)
        False
        
        >>> KitKat('Green Tea', 3) > KitKat('Mint', 2)
        True
        
        >>> KitKat('Green Tea', 2) > KitKat('Mint', 4)
        False
        """
        if self.fingers > other.fingers:
            return True
        else:
            return False
    
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
            
            