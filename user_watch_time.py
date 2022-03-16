import pandas as pd
import matplotlib.pyplot as plt

# import netflix data csv.
df = pd.read_csv('viewing-activity-data.csv')

# remove coulumns you do not want to analyze by adding them to df.drop
df = df.drop(['Attributes', 'Supplemental Video Type', 'Device Type', 'Bookmark', 'Latest Bookmark', 'Country'], axis=1)

# convert Start Time from object to datetime
# attach UTC to datetime format 
df['Start Time'] = pd.to_datetime(df['Start Time'], utc=True)

# change Start Time column into the dataframe's index
df = df.set_index('Start Time')

# convert from UTC to eastern time
df.index = df.index.tz_convert('US/Eastern')

# reset the index so that Start Time becomes a column again
df = df.reset_index()

# convert Duration from object to timedelta
df['Duration'] = pd.to_timedelta(df['Duration'])