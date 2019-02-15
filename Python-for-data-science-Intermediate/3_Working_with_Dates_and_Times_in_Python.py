## 1. Introduction ##

import csv
f = open('potus_visitors_2015.csv')
potus = list(csv.reader(f))
potus = potus[1:]

## 3. The Datetime Class ##

import datetime as dt

ibm_founded = dt.datetime(1911, 6, 16)
microsoft_founded = dt.datetime(1975, 4, 4)
man_on_moon = dt.datetime(1969, 7, 20, 20, 17)
jfk_shot = dt.datetime(1963, 11, 22, 12, 30)

## 4. Using Strptime to Parse Strings as Dates ##

date_format = "%m/%d/%y %H:%M"
for row in potus:
    start_date = row[2]
    start_date = dt.datetime.strptime(start_date, date_format)
    row[2] = start_date

## 5. Using Strftime to format dates ##

visitors_per_month = {}

for row in potus:
    month_dt = row[2]
    month_str = month_dt.strftime("%B, %Y")
    if month_str in visitors_per_month:
        visitors_per_month[month_str] += 1
    else:
        visitors_per_month[month_str] = 1

## 6. The Time Class ##

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

## 7. The Date Class ##

date_freq = {}

for row in potus:
    appt_dt = row[2]
    appt_date = appt_dt.date()
    if appt_date in date_freq:
        date_freq[appt_date] += 1
    else:
        date_freq[appt_date] = 1

max_v_num = 0
for v_date, num in date_freq.items():
    if num > max_v_num:
        max_v_num = num
        max_v_date = v_date

print(max_v_num)
print(max_v_date)

## 8. Calculations with Dates and Times ##

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

## 9. Challenge: How far ahead are appointments made ##

lead_times =  []
for row in potus:
    booking_date = dt.datetime.strptime(row[1], "%Y-%m-%dT%H:%M:%S")
    appt_date = row[2]
    lead_time = appt_date - booking_date
    lead_times.append(lead_time)
    
min_time = min(lead_times)
max_time = max(lead_times)
total_times = sum(lead_times, dt.timedelta(0))
avg_time = total_times / len(lead_times)

## 10. Challenge: Create an Appointment Summary Function ##

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

## 11. Epoch Time ##

epochs = [
           ['first', 1139444034],
           ['second', 1430583565],
           ['third', 1318037820],
           ['fourth', 751652064]
         ]

for row in epochs:
    date_epoch = row[1]
    date_dt = dt.datetime.fromtimestamp(date_epoch)
    row[1] = date_dt
