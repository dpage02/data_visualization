import csv
import matplotlib.pyplot as plt
from datetime import datetime 

filename = 'csv_file_format/data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # getting the high temperatures from the file
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

    # plot the high temperatures
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    # format plot
    plt.title("Daily high temperatures - 2018", fontsize=24)
    plt.xlabel("", fontsize = 16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize = 16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()