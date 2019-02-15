## 2. Default Arguments ##

def open_dataset(csv_name='AppleStore.csv'):
    opened_file = open(csv_name)
    
    from csv import reader
    read_file = reader(opened_file)
    
    return list(read_file)

apps_data = open_dataset()

print(apps_data)
    
    

## 3. The Official Python Documentation ##

one_decimal = round(3.43, 1)
two_decimals = round(0.23321, 2)
five_decimals = round(921.2225227, 5)

## 4. Multiple Return Statements ##

def open_dataset(file_name='AppleStore.csv',header=True):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[1:]
    else:        
        return data

apps_data = open_dataset()    

## 5. Returning Multiple Variables ##

def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[1:], data[0]
    else:
        return data

all_data = open_dataset()

header = all_data[1]
apps_data = all_data[0]

## 6. More About Tuples ##

def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[1:], data[0]
    else:
        return data
    
apps_data, header = open_dataset()    

## 8. Scopes — Global and Local ##

e = 'mathematical constant'
a_sum = 1000
length = 50

def exponential(x):
    e = 2.72
    print(e)
    return e**x
    
result = exponential(5)

def divide():
    print(a_sum)
    print(length)
    return a_sum/length
    
    
result_2 = divide()    

## 9. Scopes — Searching Order ##

file_name = 'AppleStore.csv'

def open_iOS_dataset():        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    global apps_data
    apps_data = data[1:]
    global header_row
    header_row = data[0]
    

open_iOS_dataset()    
print(header_row)
first_five = apps_data[:5]

## 10. Functions — More Quirks ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

def relative_freqs(freq_table):
    total_reg = sum(freq_table.values())

    for key in freq_table:        
        freq_table[key] = (freq_table[key] / total_reg) * 100 
        print(freq_table)
    return freq_table


c_ratings_percentages = relative_freqs(content_ratings)
print(content_ratings)
changed = True
    

    

## 11. Mutable and Immutable Types ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

def relative_freqs(freq_table):
    total = 0 
    for key in freq_table:
        count = freq_table[key]
        total += count
    
    for key in freq_table:
        freq_table[key] = (freq_table[key] / total) * 100
    
    return freq_table

relative_freqs(content_ratings.copy())
print(content_ratings)
changed = False