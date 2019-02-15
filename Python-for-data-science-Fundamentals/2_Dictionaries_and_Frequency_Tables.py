## 1. Storing Data ##

content_ratings = {'4+':4433,'9+':987,'12+':1155,'17+':622}

over_4 = content_ratings['4+']
over_9 = content_ratings['9+']
over_12 = content_ratings['12+']
over_17 = content_ratings['17+']

top_genres = {'Games':3862,'Entertainment':535,'Education':453,'Photo & Video':349, 'Utilities':248}

number_of_gaming_apps = top_genres['Games']


## 2. Dictionaries ##

content_ratings = {'4+':4433,'9+':987,'12+':1155,'17+':622}

print(content_ratings)

## 3. Indexing ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

over_9 = content_ratings['9+']
over_17 = content_ratings['17+']

## 4. Alternative Way of Creating a Dictionary ##

content_ratings = {}

content_ratings['4+'] = 4433
content_ratings['9+'] = 987
content_ratings['12+'] = 1155
content_ratings['17+'] = 622

over_12_n_apps = content_ratings['12+']

top_genres = {'Games':3862, 'Entertainment':535, 'Education':453, 'Photo & Video':349, 'Utilities': 248}

n_apps_education = top_genres['Education']


## 6. Checking for Membership ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

is_in_dictionary_1 = '4+' in content_ratings
is_in_dictionary_2 = '20+' in content_ratings
is_in_dictionary_3 = 4433 in content_ratings
is_in_dictionary_4 = 987 in content_ratings

if '17+' in content_ratings:
    result = "'17+' exists in content_ratings"
    
print(result)


## 7. Counting with Dictionaries ##

opened_file = open('AppleStore.csv')

from csv import reader
read_file = reader(opened_file)

apps_data = list(read_file)

content_ratings = {'4+': 0, '9+': 0, '12+': 0, '17+': 0}

for c_rating in apps_data[1:]:
    if c_rating[10] in content_ratings:
        content_ratings[c_rating[10]] += 1

print(content_ratings)
    
     

## 8. Finding the Unique Values ##

content_ratings = {}
genre_counting = {}

for c_rating in apps_data[1:]:
    if c_rating[10] in content_ratings:
        content_ratings[c_rating[10]] +=1
    else:
        content_ratings[c_rating[10]] = 1

    if c_rating[11] in genre_counting:
        genre_counting[c_rating[11]] +=1
    else:
        genre_counting[c_rating[11]] = 1
      
        
print(content_ratings)
print(genre_counting)

most_common_genre = 'Games'



    
    

## 10. Looping over Dictionaries ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
genre_counting = {'Social Networking': 167, 'Photo & Video': 349, 'Games': 3862, 'Music': 138, 'Reference': 64, 'Health & Fitness': 180, 'Weather': 72, 'Utilities': 248, 'Travel': 81, 'Shopping': 122, 'News': 75, 'Navigation': 46, 'Lifestyle': 144, 'Entertainment': 535, 'Food & Drink': 63, 'Sports': 114, 'Book': 112, 'Finance': 104, 'Education': 453, 'Productivity': 178, 'Business': 57, 'Catalogs': 10, 'Medical': 23}

total_number_of_apps = 7197


for n in content_ratings:
    content_ratings[n] /= total_number_of_apps
    content_ratings[n] *= 100
    
percentage_17_plus = content_ratings['17+']
percentage_15_allowed = content_ratings['4+'] + content_ratings['12+'] + content_ratings['9+']

for x in genre_counting:
    genre_counting[x] /= total_number_of_apps
    genre_counting[x] *= 100
        
percentage_games = genre_counting['Games']
percentage_non_games = 100 - percentage_games




## 11. Keeping the Dictionaries Separate ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
genre_counting = {'Social Networking': 167, 'Photo & Video': 349, 'Games': 3862, 'Music': 138, 'Reference': 64, 'Health & Fitness': 180, 'Weather': 72, 'Utilities': 248, 'Travel': 81, 'Shopping': 122, 'News': 75, 'Navigation': 46, 'Lifestyle': 144, 'Entertainment': 535, 'Food & Drink': 63, 'Sports': 114, 'Book': 112, 'Finance': 104, 'Education': 453, 'Productivity': 178, 'Business': 57, 'Catalogs': 10, 'Medical': 23}

total_number_of_apps = 7197

c_ratings_proportions = {}
c_ratings_percentages = {}

genre_proportions = {}
genre_percentages = {}

for rating in content_ratings:
    c_ratings_proportions[rating] = content_ratings[rating] / total_number_of_apps
    c_ratings_percentages[rating] = (content_ratings[rating] / total_number_of_apps ) * 100
    

for genre in genre_counting:
    genre_proportions[genre] = genre_counting[genre] / total_number_of_apps
    genre_percentages[genre] = (genre_counting[genre] / total_number_of_apps) * 100




## 12. Frequency Tables for Numerical Columns ##

data_sizes = []

for x in apps_data[1:]:
    data_sizes.append(float(x[2]))

   
min_size = min(data_sizes)
max_size = max(data_sizes)