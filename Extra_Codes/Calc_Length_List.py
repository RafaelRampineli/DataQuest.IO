"""
Add a helper method called _calc_length() to our SuperList class, which calculates the length of the list stored in the object and stores it in a new SuperList.length attribute.
Add the helper method to the end of the init method, as well as append() and reverse().
Test that the new attribute works as expected by:
Creating a new SuperList object containing the list [1, 1, 2, 3, 5] and assigning it to the variable name fibonacci.
Use the print() function to display the length attribute of the fibonacci object.
Append the value 8 to fibonacci
Use the print() function to display the updated length attribute of the fibonacci object.
"""

class SuperList():
    """
    A Python list with some extras!
    """
    def __init__(self, initial_state=[]):
        self._data = initial_state
        self._calc_length()
      
    def __repr__(self):
        string_representation = str(self._data)
        return string_representation
  
    def __eq__(self, other):
        is_equal = self.__dict__ == other.__dict__
        return is_equal
  
    def append(self, new_item):
        """
        Append `new_item` to the SuperList
        """
        self._data = self._data + [new_item]
        self._calc_length()            
            
    def reverse(self):
        """
        Reverse the order of items in the SuperList
        """
        self._data = self._data[::-1]
        _calc_length()
        
    def _calc_length(self): # When a method start using _(underscore) means that method is private 
        """
        Calc object itens length
        """
        length = 0
        for item in self._data:
            length += 1
       
        self.length = length
              
    
fibonacci = SuperList([1,1,2,3,5])

print(fibonacci.length)

fibonacci.append(8)
print(fibonacci.length)