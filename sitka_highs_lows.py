import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'csv_file_format/data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # get dates, and high/low temperatures
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    # plot the high/low temps
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c="red", alpha=.5)
    ax.plot(dates, lows, c='blue', alpha=.5)
    plt.fill_between(dates, highs, lows, facecolor='blue',alpha=.1)

    # format plot
    plt.title("Daily high and low temperatures -2018", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
