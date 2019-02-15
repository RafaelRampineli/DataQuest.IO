## 1. Introduction ##

l = [1, 2, 3]
s = "string"
d = {"a": 1, "b": 2}
i = 21
f = 3.5

print(type(l))
print(type(s))
print(type(d))
print(type(i))
print(type(f))

## 3. Defining a Class ##

class MyClass():
    pass

mc_1 = MyClass()

mc_2 = MyClass()

print(type(mc_1))

## 4. Creating Methods ##

class MyClass():
    def add_two_numbers(self, first, second):
        return first+second

    
mc = MyClass()

answer = mc.add_two_numbers(3,4)

## 5. Attributes and the 'Init' Method ##

class SuperList():
    def __init__(self,arg_1 = []):
        self.data = arg_1

my_list = SuperList([1,2,3,4,5])
print(type(my_list))
print(my_list.data)

## 6. Dunder Methods ##

class SuperList():
    def __init__(self,arg_1 = []):
        self._data = arg_1
        
    def __repr__(self):
        return str(self._data)
    
    def __eq__(self,other):
        is_equal = self.__dict__ == other.__dict__
        return is_equal
    
sl_1 = SuperList([1,2,3,4,5])
sl_2 = SuperList([1,2,3,4,5])
sl_3 = SuperList([1,2,3])

compare_1_2 = sl_1 == sl_2
compare_2_3 = sl_2 == sl_3


## 7. Creating First Methods ##
"""
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
"""

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

        

## 8. Creating and Updating Our First Attribute ##

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
        
    def _calc_length(self):
        length = 0
        for item in self._data:
            length += 1
       
        self.length = length
              
    
fibonacci = SuperList([1,1,2,3,5])

print(fibonacci.length)

fibonacci.append(8)
print(fibonacci.length)

## 9. Creating Attributes for Minimum and Maximum Values ##

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

## 10. Creating An Attribute That Checks for Types ##

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

## 11. Creating an Info Method ##

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