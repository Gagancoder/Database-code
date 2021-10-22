import csv
import plotly.graph_objects as go
import pandas as pd

daf = pd.read_csv('data.csv')

student_name = input('Enter The STUDENT ID :-')

student_df = daf.loc[daf['student_id']==student_name]
print(student_df)
print(student_df.groupby('level')['attempt'].mean())



fig = go.Figure(go.Bar(
    x = student_df.groupby('level')['attempt'].mean(),
    y = ['level1','level2','level3','level4'],
    orientation = 'h'
))
fig.show()