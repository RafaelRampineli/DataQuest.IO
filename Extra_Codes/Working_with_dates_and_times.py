"""
Import the csv module.
Use the csv.reader() function module to open the CSV file potus_visitors_2015.csv and convert it to a list of lists format.
Assign the list of lists to the variable name potus.
Remove the first row of the data set, which contains the column names.
"""
import csv
f = open('potus_visitors_2015.csv') #DataFile was provided from DataQuest.IO
potus = list(csv.reader(f))
potus = potus[1:]

##############################################################################################################################

"""
Import the datetime class using the alias dt.
Instantiate a datetime object representing midnight on June 16th, 1911 and assign the object to the variable name ibm_founded.
Instantiate a datetime object representing midnight on April 4th, 1975 and assign the object to the variable name microsoft_founded.
Instantiate a datetime object representing 8:17pm on July 20th, 1969 and assign the object to the variable name man_on_moon.
Instantiate a datetime object representing 12:30pm on November 22nd, 1963 and assign the object to the variable name jfk_shot.
"""

#datetime.datetime(year, month, day, hour=0, minute=0, second=0)

import datetime as dt

ibm_founded = dt.datetime(1911, 6, 16)
microsoft_founded = dt.datetime(1975, 4, 4)
man_on_moon = dt.datetime(1969, 7, 20, 20, 17)
jfk_shot = dt.datetime(1963, 11, 22, 12, 30)

##############################################################################################################################

"""
Look at the values for the appt_start_date column from the 'learn' section of this mission, and create a string that uses format codes to specify the format of the dates in that column.
Iterate over each row in the potus list of lists:
Assign the appt_start_date column, found at index 2 of each row, to a variable.
Use the datetime.strptime() constructor to convert the variable from a string to a datetime object, using the format codes you calculated earlier.
Assign the datetime object back to index 2 of the row.

(http://strftime.org/)
"""

date_format = "%m/%d/%y %H:%M"
for row in potus:
    start_date = row[2]
    start_date = dt.datetime.strptime(start_date, date_format)
    row[2] = start_date

##############################################################################################################################

# strptime >> str-p-time >> string parse time
# strftime >> str-f-time >> string format time

"""
Initialize an empty dictionary, visitors_per_month.
Iterate over the rows in the potus list of lists. In each iteration:
Assign the datetime object from the appt_start_date column (index 2) to a variable.
Use datetime.strftime() to create a string in the format "January, 1901" from the datetime object.
Check whether the string exists as a key in the visitors_per_month dictionary.
If it exists, increment the value of that key-value pair.
If it does not exist, assign a value of 1 to that key-value pair.
"""

visitors_per_month = {}

for row in potus:
    month_dt = row[2]
	#We can use %A, %I, %M, and %p to represent the day of the week, the hour of the day, the minute of the hour, and am/pm:    
    month_str = month_dt.strftime("%B, %Y")  # %B Represent the month as a word. 
    if month_str in visitors_per_month:
        visitors_per_month[month_str] += 1
    else:
        visitors_per_month[month_str] = 1

##############################################################################################################################
"""
Instantiate a dictionary appt_times to store the frequency table.
Iterate over each row in the potus list of lists. For each iteration:
Assign the datetime object stored at index value 2 to a variable
Create a time object from the datetime object
Check whether the time object exists in the appt_times dictionary, and increment or assign to create a frequency table
Assign the earliest appointment time from the appt_times dictionary to the variable min_time.
Assign the latest appointment time from the appt_times dictionary to the variable max_time.
"""

# datetime.time(hour=0, minute=0, second=0, microsecond=0)        

appt_times = {}

for row in potus:
    appt_dt = row[2]
    appt_t = appt_dt.time()
    if appt_t in appt_times:
        appt_times[appt_t] += 1
    else:
        appt_times[appt_t] = 1

min_time = min(appt_times)
max_time = max(appt_times)

"""
Iterate over each row in potus and use datetime.strptime() to parse the appointment end dates (at index 3) to datetime objects, assigning them back to the same position in each row.
Calculate the length of each appointment:
Initialize an empty list appt_lengths.
Iterate over each row in the potus list of lists, and:
Use an operation to calculate the length of each appointment as a timedelta object.
Append the timedelta object to the appt_lengths list.
Analyze the data in the appt_lengths list by:
Calculating the minimum value in the and assigning it to min_length
Calculating the maximum value in the and assigning it to max_length
Calculating the average value in the and assigning it to avg_length
After you run your code, use the variable inspector to look at the minimum, maximum, and average values and think about what those values mean.
"""

for row in potus:
    end_date = row[3]
    end_date = dt.datetime.strptime(end_date, "%m/%d/%y %H:%M")
    row[3] = end_date

appt_lengths = []

for row in potus:
    start_date = row[2]
    end_date = row[3]
    length = end_date - start_date
    appt_lengths.append(length)

min_length = min(appt_lengths)
max_length = max(appt_lengths)
total_lengths = sum(appt_lengths, dt.timedelta(0))
avg_length = total_lengths / len(appt_lengths)

"""
Create a function appt_summary, which takes three integer arguments representing the year, month, and day.
The function should print the date formatted as shown in the example in the learn section above, with a blank line following it.
The function should then print a line for each appointment from the potus dataset from the date provided:
The appointments should be printed in the same order that they appear in the potus data set.
The output should start with the visitee name in title case, followed by the time using the format shown in the example in the learn section above.
Use the function to display the appointment summary for the date May 20, 2015.
"""

def appt_summary(year, month, day):
    target_date = dt.date(year, month, day)
    print("Appointments for {:%A %B %-d, %Y}:\n".format(target_date))
    
    template = "{} at {:%-I:%M %p}."
    for row in potus:
        visitee = row[0].title()
        appt_time = row[2]
        
        if appt_time.date() == target_date:
            print(template.format(visitee, appt_time))

appt_summary(2015, 5, 20)