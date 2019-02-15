"""
Add two helper methods, SuperList._calc_min() and SuperList._calc_max(), which implement the logic from the functions in the code example above.
They should assign the minimum and maximum values to the attributes SuperList.min and SuperList.max respectively.
Add a SuperList._update() helper method which calls the two new helper methods, as well as the existing SuperList._calc_length() method.
Add code to call the SuperList._update() method from the init method, as well as the two public methods that modify the underlying data.
Remove the code that calls SuperList._calc_length() method from these places, so it is not run twice.
Test that your new attributes work and update correctly, by:
Create a new SuperList object with the value [18, 28, 35] and assign it to the variable name temperatures.
Use the print() function to display the SuperList.min and SuperList.max attributes for the temperatures variable.
Use the SuperList.append() method to append the value -12 to temperatures.
Use the print() function to display the SuperList.min and SuperList.max attributes for the temperatures variable.
Use the SuperList.append() method to append the value 42 to temperatures.
Use the print() function to display the SuperList.min and SuperList.max attributes for the temperatures variable.
"""

class SuperList():
    """
    A Python list with some extras!
    """
    def __init__(self, initial_state=[]):
        self._data = initial_state
        self._update()
      
    def __repr__(self):
        string_representation = str(self._data)
        return string_representation
  
    def __eq__(self, other):
        is_equal = self.__dict__ == other.__dict__
        return is_equal
  
    def _calc_length(self):
        """
        A helper function to calculate the .length
        attribute.
        """
        length = 0
        for item in self._data:
            length += 1
        self.length = length
  
    def append(self, new_item):
        """
        Append `new_item` to the SuperList
        """
        self._data = self._data + [new_item]
        self._update()
  
    def reverse(self):
        """
        Reverse the order of items in the SuperList
        """
        self._data = self._data[::-1]
        self._update()
        
    def _update(self):
        
        self._calc_length()
        self._calc_max()
        self._calc_min()
        
    def _calc_min(self):
        """
        Calculates the minimum value in a list.

        When lists have values of more than
        one type or are empty, it is not possible
        to calculate a minimum value.  In these
        cases the function will return None
        """
        
        is_empty = len(self._data) == 0 # min() will fail if our list is empty

        types = []
        for i in self._data:
            i_type = type(i)
            if i_type not in types:
                types.append(i_type)
        more_than_one_type = len(types) > 1

        if is_empty or more_than_one_type:
            self.min = None
        else:
            self.min = min(self._data)

    def _calc_max(self):
        """
        Calculates the maximum value in a list.

        When lists have values of more than
        one type or are empty, it is not possible
        to calculate a maximum value.  In these
        cases the function will return None
        """
        
        is_empty = len(self._data) == 0 # max() will fail if our list is empty
        types = []
        for i in self._data:
            i_type = type(i)
            if i_type not in types:
                types.append(i_type)
        more_than_one_type = len(types) > 1

        if is_empty or more_than_one_type:
            self.max = None
        else:
            self.max = max(self._data)
        

temperatures = SuperList([18,28,35])
print(temperatures._calc_min())
print(temperatures._calc_max())

temperatures.append(-12)
print(temperatures._calc_min())
print(temperatures._calc_max())

temperatures.append(42)
print(temperatures._calc_min())
print(temperatures._calc_max())


        