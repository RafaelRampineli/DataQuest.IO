## 1. If Statements ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_apps_ratings = []

for row in apps_data[1:]:   
    rating = float(row[7])
    price = float(row[4])
    if price == 0.0:
        free_apps_ratings.append(rating)
                  
avg_rating_free = sum(free_apps_ratings) / len(free_apps_ratings)

n_free_apps = len(free_apps_ratings)

percentage_free_apps = (len(free_apps_ratings)/ len(apps_data[1:])) * 100


## 2. Booleans ##

a_price = 0
prices = [0, 2, 0, 0, 0]
app_and_price = [['Facebook', 0], ['Instagram', 0], ['Plants vs. Zombies', 0.99],
                 ['Minecraft: Pocket Edition', 6.99], ['Temple Run', 0],
                 ['Plague Inc.', 0.99]]

if a_price == 0:
    print('This is free.')

if a_price == 1:
    print('This is not free.')

free =[]

for price in prices:
    if price == 0:
        free.append(price)

n_free_prices = len(free)

free_apps = []

for t in app_and_price:
    name = t[0]
    
    if t[1] == 0:
        free_apps.append(name)

print(free_apps)        
    

## 3. The Average Rating of Non-free Apps ##

non_free_apps_ratings = []

for n in apps_data[1:]:
    rating = float(n[7])
    price = float(n[4])
    
    if price != 0.0:
        non_free_apps_ratings.append(rating)

        
avg_rating_non_free = sum(non_free_apps_ratings) / len(non_free_apps_ratings)


## 4. The Average Rating of Gaming Apps ##

non_games_ratings = []

for n in apps_data[1:]:
    rating = float(n[7])
    genre = n[11]
    
    if genre != 'Games':
        non_games_ratings.append(rating)

avg_rating_non_games = sum(non_games_ratings) / len(non_games_ratings)



## 5. Multiple Conditions ##

free_games_ratings = []

for n in apps_data[1:]:
    rating = float(n[7])
    price = float(n[4])
    genre = n[11]
    
    if price == 0.0 and genre == 'Games':
        free_games_ratings.append(rating)

avg_rating_free_games = sum(free_games_ratings) / len(free_games_ratings)

## 6. The or Operator ##

games_social_ratings = []

for n in apps_data[1:]:
    rating = float(n[7])
    genre = n[11]
    
    if genre == 'Social Networking' or genre == 'Games':
        games_social_ratings.append(rating)

avg_games_social = sum(games_social_ratings) / len(games_social_ratings)
    
    

## 7. Combining Logical Operators ##

free_games_social_ratings = []
for row in apps_data[1:]: # apps_data is already saved from previous screens
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])
    
    if (genre == 'Social Networking' or genre == 'Games') and price == 0:
        free_games_social_ratings.append(rating)
              
# Write your code below
avg_free = sum(free_games_social_ratings) / len(free_games_social_ratings)

nonfree_games_social_ratings = []

for row2 in apps_data[1:]:
    rating = float(row2[7])
    genre = row2[11]
    price = float(row2[4])
    
    if (genre == 'Social Networking' or genre == 'Games') and price != 0:
        nonfree_games_social_ratings.append(rating)

avg_non_free = sum(nonfree_games_social_ratings) / len(nonfree_games_social_ratings)

## 8. Comparison Operators ##

price_greather =[]
price_less = []

for n in apps_data[1:]:
    rating = float(n[7])
    price = float(n[4])
    
    if price > 9:
        price_greather.append(rating)
        
    if price <= 9:
        price_less.append(rating)

avg_rating = sum(price_greather) / len(price_greather)

n_apps_more_9 = len(price_greather)
n_apps_less_9 = len(price_less)

## 9. The else Clause ##

for n in apps_data[1:]:
    if float(n[4]) == 0.0:
        n.append('free')
    else:
        n.append('non-free')
        

apps_data[0].append('free_or_not')

print(apps_data[:6])
        
        
    

## 10. The elif Clause ##

for n in apps_data[1:]:
    if float(n[4]) == 0.0:
        n.append('free')
    elif float(n[4]) > 0.0 and float(n[4]) < 20.0:
        n.append('affordable')
    elif float(n[4]) >= 20.0 and float(n[4]) < 50.0:
        n.append('expensive')
    elif float(n[4]) >= 50.0:
        n.append('very expensive')

apps_data[0].append('price_label')

print(apps_data[:6])

        