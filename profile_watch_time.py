import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

# Import data and create data frame.
# If you are using your own Netlix data, replace the .csv below.
df = pd.read_csv('viewing-activity-data.csv')

# Remove unnecessary columns.
df = df.drop(['Attributes', 'Supplemental Video Type', 'Device Type',
              'Bookmark', 'Latest Bookmark', 'Country'],axis=1)

# Convert 'Duration' from an object to timedelta using pd.to_timedelta().
df['Duration'] = pd.to_timedelta(df['Duration'])

# Group and sum profile watch times using .groupby() and .sum().
df_groupby_profile = df.groupby(
    ['Profile Name'], as_index=False)['Duration'].sum()

# Round 'Duration' to days using dt.days.
df_groupby_profile['Duration'] = df_groupby_profile['Duration'].dt.days

# Convert 'Duration' from a timedelta to numeric using pd.to_numeric.
df_groupby_profile['Duration'] = pd.to_numeric(
    df_groupby_profile['Duration'])

'''
Retrieves the current date and calculates how many days have passed since
the Netflix data was requested. The variable is then converted to a
string and formatted to include only days.
'''
days_removed = dt.date.today() - dt.date(2022, 2, 21)
days_removed = str(days_removed.days)

# Create bar graph of each profile's summed 'Duration' using plt.bar().
plt.bar(
    df_groupby_profile['Profile Name'],
    df_groupby_profile['Duration'],
    color = "#DE0912")

plt.title(
    'Netflix Profiles Total Watch Time\n Data Requested ' + days_removed
     + ' Days Ago',
    fontweight = 'bold',
    fontsize = 14)

plt.xlabel('Profiles',
    fontweight = 'bold',
    fontsize = 12)

plt.ylabel(
    'Total Watch Time (Days)',
    fontweight = 'bold',
    fontsize = 12)

plt.show()