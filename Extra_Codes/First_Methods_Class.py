'''
Add a new method SuperList.append().
The method will require a single parameter to be passed to it when called.
The method will modify the SuperList._data list attribute by appending the argument to the list.
The method should not return any value.
To the SuperList definition, add a new method SuperList.reverse().
The method will require a no parameters to be passed to it when called.
The method will modify the SuperList._data list attribute by reversing the order of the items in the list.
The method should not return any value.
Create an object of the SuperList class, initializing the data in the object with [1, 2, 3, 4, 5]. Assign the object to the variable name my_list.
Use the print() function to display the my_list object.
Use the SuperList.append() method to append the integer 6 to the my_list object.
Use the print() function to display the my_list object.
Use the SuperList.reverse() method to reverse the order of the items in the my_list object.
Use the print() function to display the my_list object.
'''

class SuperList():
    """
    A Python list with some extras!
    """

    #runs upon the creation of a new object
    def __init__(self, initial_state=[]):
        self._data = initial_state
    
    #which defines a string representation of the object to be used by functions like str() and print()
    #Because of this part of code, whe didn't need to use print like: print(my_list._data), just: print(my_list)  
    def __repr__(self):
        string_representation = str(self._data)
        return string_representation
  
    #which is used to compare two objects for equality
    def __eq__(self, other):
        is_equal = self.__dict__ == other.__dict__
        return is_equal
    
    def append(self, arg_1):
        self._data = self._data + [arg_1]
        
    def reverse(self):
        self._data = self._data[::-1]
        
my_list = SuperList([1,2,3,4,5])
print(my_list)

my_list.append(6)
print(my_list)

my_list.reverse()
print(my_list)
