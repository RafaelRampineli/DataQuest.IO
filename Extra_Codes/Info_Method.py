"""
Add a new method, SuperList.info().
The method should use the print() function to print the template string provided above, inserting the four attributes in the order we provided them above.
The method does not require a return statement.
Because the method does not modify the underlying data, it does not need to call SuperList._update()
Test that your new method works correctly:
Create a new SuperList object with the value [1, 2, 3, 4, 5] and assign it to the variable name a.
Use the SuperList.info() method to display summary information about the variable a.
Create a new SuperList object with the value [1.3, -14, "hello"] and assign it to the variable name b.
Use the SuperList.info() method to display summary information about the variable b.
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
        A helper function to caluclate the .length
        attribute
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
          
    def _calc_types(self):
        """
        A helper function to calculate the .types
        attribute
        """
        types = []
        for item in self._data:
            item_type = type(item)
            if item_type not in types:
                types.append(item_type)
        self.types = types

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
    
    def info(self):
        template = '''\
List Length:     {}
Max Value:       {}
Min Value:       {}
Types Contained: {}
'''.format(self.length, self.max, self.min, self.types)
        
        print(template)
        
a = SuperList([1,2,3,4,5])
a.info()

b = SuperList([1.3, -14, "hello"])
b.info()