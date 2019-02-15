"""
Dat aQuest.IO mission using artworks.csv Dataset.

Goal: Format the  output data result, to be much easier to read and understand.

Create a function that takes a single argument specifying the column index number, and prints a frequency table in the format shown at above.
Start by creating the frequency table:
Create an empty dictionary to store the frequency table
Iterate over the moma list of lists and checking the value at the specified column is in the dictionary.
If it is in the dictionary, increment it.
If it isn't in the dictionary, add it with a value of 1.
Use the widest_key_value() function to calculate the width of the both the widest key and value in your frequency table dictionary.
Add 1 to the value width to account for the comma separator.
Iterate over the keys and values in the frequency table dictionary using sorted(), and for each pair, print in a single line:
The key left aligned, padded to the width of the widest key
The substring " : " to separate the key from the values
The value right aligned, padded to the width of the widest value, with a comma separator.
Run the function you have created to display a summary of the Department column (row index 7).
"""

def widest_key_value(dictionary):
    """
    Returns the width of the string representation
    for the longest key and value in the dict.
    """
    max_key_width = 0
    max_val_width = 0

    for key, value in dictionary.items():
        key_width = len(str(key))
        val_width = len(str(value))
        
        if key_width > max_key_width:
            max_key_width = key_width
        
        if val_width > max_val_width:
            max_val_width = val_width

    return max_key_width, max_val_width 
	
	
def function_teste(Column_Index):
    freq_table = {}
    
    for row in moma:
        if row[Column_Index] in freq_table:
            freq_table[row[Column_Index]] +=1
        else:
            freq_table[row[Column_Index]] = 1
        
    key_width, val_width = widest_key_value(freq_table)
    val_width += 1
        
    for key, value in sorted(freq_table.items()):
        print("{:<{}} : {:>{},}".format(key,key_width, value, val_width))
            
function_teste(7) #Index Number	