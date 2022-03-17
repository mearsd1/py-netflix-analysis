import pandas as pd
import matplotlib.pyplot as plt

# import netflix data csv.
df = pd.read_csv('viewing-activity-data.csv')

# remove coulumns you do not want to analyze by adding them to df.drop
df = df.drop(['Attributes', 'Supplemental Video Type', 'Device Type', 'Bookmark', 'Latest Bookmark', 'Country'], axis=1)

# convert Duration from object to timedelta
df['Duration'] = pd.to_timedelta(df['Duration'])

# group and sum profile watch time
df_groupby_profile = df.groupby(['Profile Name'], as_index=False)['Duration'].sum()

# rounds to days
df_groupby_profile['Duration'] = df_groupby_profile['Duration'].dt.days

# convert Duration from timedelta to numeric for graphing
df_groupby_profile['Duration'] = pd.to_numeric(df_groupby_profile['Duration'])

# create bar graph of each Profile's total Duration(watch time)
# create bar graph of each Profile's total Duration(watch time)
plt.bar(df_groupby_profile['Profile Name'], df_groupby_profile['Duration'], color = "#DE0912")
plt.title('Netflix Profiles Total Watch Time', fontweight = 'bold', fontsize = 14)
plt.xlabel('Profiles', fontweight = 'bold', fontsize = 12)
plt.ylabel('Total Watch Time', fontweight = 'bold', fontsize = 12)
plt.savefig('Netflix Profile Total Watch Time.png')