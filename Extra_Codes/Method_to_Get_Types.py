"""
Add a new helper method, SuperList._calc_types(), which implements the logic from the function in our example code and creates the SuperList.types attribute.
Call the new helper method from any place(s) that it needs to be called to accurately update the attribute.
Test that your new attribute works correctly:
Create a new SuperList object with the value ["one", 2, "three"] and assign it to the variable name multiple_types.
Use the print() function to display the SuperList.types attribute for the multiple_types variable.
Append the value 4.0 to the multiple_types variable.
Use the print() function to display the updated value of the SuperList.types attribute.
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
  
    def _calc_max(self):
        """
        A helper function to calculate the .max
        attribute.
        """
        is_empty = len(self._data) == 0
      
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
  
    def _calc_min(self):
        """
        A helper function to calculate the .min
        attribute.
        """
        is_empty = len(self._data) == 0
      
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

    def _update(self):
        """
        A helper method to call other helper methods
        and update attributes when underlying
        data changes.
        """
        self._calc_length()
        self._calc_min()
        self._calc_max()
        self._calc_types()

    def _calc_types(self):
        types =[]
        
        for item in self._data:
            item_type = type(item)
            
            if item_type not in types:
                types.append(item_type)
           
        self.types = types         
  
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
        
multiple_types = SuperList(["one", 2, "three"])
print(multiple_types.types)

multiple_types.append(4.0)
print(multiple_types.types)