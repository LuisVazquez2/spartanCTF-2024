import numpy as np
import pandas as pd

#import dates from dates file
dates = pd.read_csv('../files/dates.csv', header=None)
# sort the dates
np_dates = np.sort(dates[0].values)
#convert the numbers in dates to datetime
np_dates = pd.to_datetime(np_dates, format='%Y%m%d')
print(np_dates)
#find the day than doesn't exist in the array of dates
for i in range(1, len(np_dates)):
    if np_dates[i] - np_dates[i-1] != pd.Timedelta(days=1):
        print(f"Missing date: {np_dates[i-1] + pd.Timedelta(days=1)}")
        print(f"D1: {np_dates[i-1] } D2: {np_dates[i]}")
        break