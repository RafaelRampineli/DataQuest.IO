## 2. Reading our MoMA Data Set ##

# import the python csv module
import csv

# use the python built-in function open()
# to open the children.csv file
f = open('children.csv')

# use csv.reader() to parse the data from
# the file
reader = csv.reader(f)

# use list() to convert the data
# into a list of lists format
children = list(reader)

# remove the first row of the data, which
# contains the column names
children = children[1:]

# Write your code here
f = open('artworks.csv')
reader = csv.reader(f)
moma = list(reader)
moma = moma[1:]

## 4. Cleaning the Nationality and Gender Columns ##

# Variables you create in previous screens
# are available to you, so you don't need
# to read the CSV again

# remove parentheses from the nationality column
for row in moma:
    nationality = row[2]
    nationality = nationality.replace("(","")
    nationality = nationality.replace(")","")
    row[2] = nationality
    
for row in moma:
    gender = row[5]
    gender = gender.replace("(","").replace(")","")
    row[5] = gender
    

## 5. String Capitalization ##

for row in moma:
    gender = row[5]
    # convert the gender to title case
    gender = gender.title()
    # if there is no gender, set a descriptive value
    if not gender:
        gender = "Gender Unknown/Other"
    row[5] = gender
    
for row in moma:
    Nationality = row[2]
    Nationality = Nationality.title()
    
    if not Nationality:
        Nationality = "Nationality Unknown"
    
    row[2] = Nationality

## 6. Errors During Data Cleaning ##

def clean_and_convert(date):
    date = date.replace("(", "")
    date = date.replace(")", "")
    if date != "":
        date = int(date)
    return date

for row in moma:
    BeginDate = row[3]
    EndDate = row[4]
    
    row[3] = clean_and_convert(BeginDate)
    row[4] = clean_and_convert(EndDate)

## 7. Parsing Numbers from Complex Strings, Part One ##

test_data = ["1912", "1870-79", "1929",
             "1913\\-1923", "(1951)", "1994",
             "1934", "c. 1915", "2009", "1978",
             "1947", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "1964\\-65", "c. 1955.",
             "c. 1970's", "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","\\","s","'"]

def strip_characters(string_input):
    for row in bad_chars:
        string_input = string_input.replace(row,"")
    string_input = string_input.strip()
    return string_input

    
stripped_test_data = []

for row in test_data:
    cleaned_data = strip_characters(row)
    #cleaned_data = cleaned_data.strip()
    stripped_test_data.append(cleaned_data)

        
        
        
    

## 8. Parsing Numbers from Complex Strings, Part Two ##

bad_chars = ["(",")","c","C",".","\\","s","'"]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    string = string.strip()
    return string

stripped_test_data = ['1912', '1870-79', '1929',
                      '1913-1923', '1951', '1994', 
                      '1934', '1915', '2009', '1978',
                      '1947', '1995', '1912', '1988',
                      '2002', '1957-1959', '1964-65',
                      '1955', '1970', '1990-1999']

def process_date(string):
    if "-" in string:
        string_splitted = string.split("-")
        
        if len(string_splitted[1]) == 2:
            string_splitted[1] = string_splitted[0][:2] + string_splitted[1]
            
        avg_date = round((int(string_splitted[0]) + int(string_splitted[1])) / 2)
    
        return avg_date            
    
    else:
        return int(string)

processed_test_data = []

for date in stripped_test_data:
    processed_test_data.append(process_date(date))
    
print(processed_test_data)


for date in moma:
    var_date = date[6]
    var_date = strip_characters(var_date)
    date[6] = process_date(var_date)


## 9. Summarizing Numeric Data ##

def calculate_decades(decades):
    decade_ranges = {}
    for d in decades:
        if d in decade_ranges:
            decade_ranges[d] += 1
        else:
            decade_ranges[d] = 1
    return decade_ranges

decades = []

for row in moma:
    birth_year = row[3]
    artwork_year = row[6]
    decade_ranges = ""
    
    if birth_year is not "":
        artist_age = int(artwork_year) - int(birth_year)
        
        if artist_age < 20:
            decade_ranges = "Unknown"
        
        elif artist_age >= 20:
            decade_ranges = str(artist_age)[:-1] + "0s"
            
    else:
        decade_ranges = "Unknown"
    
    decades.append(decade_ranges)
    
decade_summary = calculate_decades(decades)
        
            
    
    



## 10. String Formatting ##

def parse_birth_year(artist):
    """
    For a given artist, return the birth year on the first
    artwork found.
    """
    for row in moma:
        if row[1] == artist:
            birth_date = row[3]
            if birth_date == "":
                birth_date = "unknown"
            return birth_date
        
def artist_summary(artist):
    birth_date = parse_birth_year(artist)
    
    result = "{}'s birth year is {}".format(artist,birth_date)
    
    return result


print(artist_summary("Louise Bourgeois"))
     


## 11. Formatting Numbers Inside Strings ##

# create frequency table dists for both the number
# of artists and number of artworks by gender,
# excluding unknown/other genders
gender_artworks_count = {}
gender_artist_list = {}

for row in moma:
    gender = row[5]
    artist = row[1]
    if gender != "Gender Unknown/Other":
        if gender in gender_artworks_count:
            gender_artworks_count[gender] += 1
            if artist not in gender_artist_list[gender]:
                gender_artist_list[gender].append(artist)
        else:
            gender_artworks_count[gender] = 1
            gender_artist_list[gender] = [artist]


# Combine the two frequency tables into a list
# of lists which summarizes the data
gender_data = []

for gender in gender_artworks_count:
    artworks_count = gender_artworks_count[gender]
    artists_count = len(gender_artist_list[gender])
    average_works = artworks_count / artists_count
    gender_data.append([gender, artworks_count, average_works])
   
for row in gender_data:
    text = "There are {:,} artworks by {} artists at an average of {:.1f} each.".format(row[1],row[0],row[2])
    print(text)  



## 12. Creating a Function to Summarize Data ##
"""
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