## 1. Lists ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

## 2. Indexing ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

ratings_1 = row_1[3]
ratings_2 = row_2[3]
ratings_3 = row_3[3]
ratings_4 = row_4[3]
ratings_5 = row_5[3]

total = ratings_1 + ratings_2 + ratings_3 + ratings_4 + ratings_5

average = total/5


## 3. Negative Indexing ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

rating_1 = row_1[-1]
rating_2 = row_2[-1]
rating_3 = row_3[-1]
rating_4 = row_4[-1]
rating_5 = row_5[-1]

total_rating = rating_1 + rating_2 + rating_3 + rating_4 + rating_5

average_rating = total_rating /5




## 4. Retrieving Multiple List Elements ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

fb_rating_data = [ row_1[0], row_1[3], row_1[-1] ]
insta_rating_data = [ row_2[0], row_2[3], row_2[-1] ]
pandora_rating_data = [ row_5[0], row_5[3], row_5[-1] ]

cc_pricing_data = [row_3[0], row_3[1], row_3[2] ]
tr_pricing_data = [row_4[0], row_4[1], row_4[2] ]

print(fb_rating_data)

sum_rating = fb_rating_data[-1] + insta_rating_data[-1] + pandora_rating_data[-1]

avg_rating = sum_rating/3

sum_pricing = cc_pricing_data[1] + tr_pricing_data[1]

avg_pricing = sum_pricing/2

## 5. List Slicing ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

first_4_fb = row_1[:4]
last_3_fb  = row_1[-3:]
insta_2_4 = row_2[1:4]
pandora_3_4 = row_5[2:4]
last_2_insta = row_2[-2:]

sum_rating = last_3_fb[2] + last_2_insta[1]
avg_rating = sum_rating/2

sum_price = first_4_fb[1] + insta_2_4[0]
avg_price = sum_price/2



## 6. List of Lists ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

avg_rating = (app_data_set[0][-1] + app_data_set[1][-1] + app_data_set[2][-1] + app_data_set[3][-1] + app_data_set[4][-1]) /5


## 7. Opening a File ##

opened_file = open('AppleStore.csv')

from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

print(len(apps_data))
print(apps_data[0])
print(apps_data[1:3])

col_names = apps_data[0]

apps_data = apps_data[1:]

print(col_names)
print(apps_data[0])
      

## 9. For Loops ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

rating_sum = 0

for row in app_data_set:
    rating = row[-1]
    rating_sum += rating

avg_rating = rating_sum/5    

## 10. The Average App Rating ##

opened_file = open('AppleStore.csv')

from csv import reader
read_file = reader(opened_file)

apps_data =list(read_file)

rating_sum = 0

for r in apps_data[1:]: 
    rating = float(r[7])
    rating_sum += rating
    
avg_rating = rating_sum / len(apps_data[1:])
    



## 11. Alternative Way to Compute an Average ##

opened_file = open('AppleStore.csv')

from csv import reader
read_file = reader(opened_file)

apps_data = list(read_file)

all_ratings = []

for x in apps_data[1:]:
    rating = float(x[7])
    all_ratings.append(rating)

print(all_ratings)
    
avg_rating = sum(all_ratings) / len(all_ratings)    
    

## 12. Understanding How a CSV File Is Opened ##

dataset = open('AppleStore.csv')

read_file = dataset.read()
split_dataset = read_file.split('\n')

print(split_dataset)

header = split_dataset[0]
first_5 = split_dataset[1:6]

print(header)
print(first_5)

## 13. More on Understanding How a CSV File Is Opened ##

opened_file = open('AppleStore.csv')
read_file = opened_file.read()
split_dataset = read_file.split('\n')

final_dataset = []

for x in split_dataset:
    final_dataset.append(x.split(','))

print(final_dataset[:6])
header = final_dataset[0]
instagram = final_dataset[2]
insta_rating = instagram[7]