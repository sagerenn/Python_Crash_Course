import os
import csv
from datetime import datetime
import traceback

os.chdir(os.path.dirname(__file__))

filename = 'sitka_weather_07-2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    print(header_row.index('TMAX'))
    print(header_row.index('TMIN'))
    print(header_row.index('PRCP'))
    print(header_row.index('DATE'))
    # print(next(reader))
    # print(next(f))
    print(dict(enumerate(header_row)))
    highs, dates, lows, minus, prcps = {}, [], {}, [], {}
    for row in reader:
        station_name = row[header_row.index('NAME')]
        try:
            high = int(row[header_row.index('TMAX')])
            low = int(row[header_row.index('TMIN')])
            prcp = float(row[header_row.index('PRCP')])
            date = datetime.strptime(row[header_row.index('DATE')], '%Y-%m-%d')

        except ValueError:
            # print(row)
            print(reader.line_num)
            traceback.print_exc()
            # high = None
            # low = None
            # minus_tmp = None
        else:

            if date not in dates:
                dates.append(date)
            
            if date not in highs:
                highs[date] = []

            if date not in lows:
                lows[date] = []

            if date not in prcps:
                prcps[date] = []

            highs[date].append(high)
            prcps[date].append(prcp)
            lows[date].append(low)

    dates.sort()
    date_highs, date_lows, date_prcps = [], [], []
    for date in dates:
        all_high = 0
        all_low = 0
        all_prcp = 0
        for high in highs[date]:
            all_high += high

        for low in lows[date]:
            all_low += low

        for prcp in prcps[date]:
            all_prcp += prcp

        avg_high = all_high/len(highs[date])
        avg_low = all_low/len(lows[date])
        avg_prcp = all_prcp/len(prcps[date])
        date_highs.append(avg_high)
        date_lows.append(avg_low)
        date_prcps.append(avg_prcp)
        minus.append(avg_high - avg_low)

# print(highs)


import matplotlib.pyplot as plt 

# Plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, date_highs, c='red', alpha=0.5)
ax.plot(dates, date_lows, c='blue', alpha=0.5)
ax.plot(dates, minus, c='green', alpha=0.5)
plt.fill_between(dates, date_lows, date_highs, facecolor='blue', alpha=0.1)

# ax.plot(dates, date_prcps, c='blue', alpha=0.5)
ax.set_ylim([0,150])

# format plot
plt.title(f"Daily High Temperatures\n{station_name}", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig('test.png')

