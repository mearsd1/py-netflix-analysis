import pandas as pd
import matplotlib.pyplot as plt

# import netflix data csv.
df = pd.read_csv('viewing-activity-data.csv')

# remove coulumns you do not want to analyze by adding them to df.drop
df = df.drop(['Attributes', 'Supplemental Video Type', 'Device Type', 'Bookmark', 'Latest Bookmark', 'Country'], axis=1)