import requests
from bs4 import BeautifulSoup
import model
import pandas as pd
from datetime import date
import sqlite3

# Create a Response object called r
r_passing = requests.get(
    'https://www.nfl.com/stats/team-stats/offense/passing/2022/reg/all', timeout=1.0)

r_receiving = requests.get(
    'https://www.nfl.com/stats/team-stats/offense/receiving/2022/reg/all', timeout=1.0)

r_rushing = requests.get(
    'https://www.nfl.com/stats/team-stats/offense/rushing/2022/reg/all', timeout=1.0)

r_scoring = requests.get(
'https://www.nfl.com/stats/team-stats/offense/scoring/2022/reg/all', timeout=1.0)

r_defensive_interception = requests.get(
    'https://www.nfl.com/stats/team-stats/defense/interceptions/2022/reg/all', timeout=1.0)

# # Create a Beautiful Soup object called soup
soup_passing = BeautifulSoup(r_passing.text, 'html.parser')
soup_receiving = BeautifulSoup(r_receiving.text, 'html.parser')
soup_rushing = BeautifulSoup(r_rushing.text, 'html.parser')
soup_scoring = BeautifulSoup(r_scoring.text, 'html.parser')
soup_defensive_interception = BeautifulSoup(r_defensive_interception.text, 'html.parser')

print("The HTML from the NFL Website done being parsed")

# Get the table
passing_table_in_html = soup_passing.find('table')
receiving_table_in_html = soup_receiving.find('table')
rushing_table_in_html = soup_rushing.find('table')
scoring_table_in_html = soup_scoring.find('table')
defensive_interception_table_in_html = soup_defensive_interception.find('table')

# Get data from the table head and table body
passing_table_head = model.get_table_head_fields_as_list(passing_table_in_html)
receiving_table_head = model.get_table_head_fields_as_list(receiving_table_in_html)
rushing_table_head = model.get_table_head_fields_as_list(rushing_table_in_html)
scoring_table_head = model.get_table_head_fields_as_list(scoring_table_in_html)
defensive_interception_table_head = model.get_table_head_fields_as_list(defensive_interception_table_in_html)

passing_table_body = model.get_table_body_as_lists(passing_table_in_html)
receiving_table_body = model.get_table_body_as_lists(receiving_table_in_html)
rushing_table_body = model.get_table_body_as_lists(rushing_table_in_html)
scoring_table_body = model.get_table_body_as_lists(scoring_table_in_html)
defensive_interception_table_body = model.get_table_body_as_lists(defensive_interception_table_in_html)

print("The data is extracted from the HTML now, next up is the joining of the header and body!")

# Join the table head data and table body data
passing_table_data = [passing_table_head] + passing_table_body
receiving_table_data = [receiving_table_head] + receiving_table_body
rushing_table_data = [rushing_table_head] + rushing_table_body
scoring_table_data = [scoring_table_head] + scoring_table_body
defensive_interception_table_data = [defensive_interception_table_head] + defensive_interception_table_body

# Add the data to a python list
passing_data = []
for row in passing_table_data:
    passing_data.append(row)

receiving_data = []
for row in receiving_table_data:
    receiving_data.append(row)

rushing_data = []
for row in rushing_table_data:
    rushing_data.append(row)

scoring_data = []
for row in scoring_table_data:
    scoring_data.append(row)

defensive_interception_data = []
for row in defensive_interception_table_data:
    defensive_interception_data.append(row)

# Create a Pandas DataFrame
passing_df = pd.DataFrame(data=passing_data)
receiving_df = pd.DataFrame(data=receiving_data)
rushing_df = pd.DataFrame(data=rushing_data)
scoring_df = pd.DataFrame(data=scoring_data)
defensive_interception_df = pd.DataFrame(data=defensive_interception_data)

print("The data is now in a Pandas DataFrame, next up is the cleaning of the data!")

# Make the first row the column names
passing_columns = passing_df.iloc[0]
receiving_columns = receiving_df.iloc[0]
rushing_columns = rushing_df.iloc[0]
scoring_columns = scoring_df.iloc[0]
defensive_interception_columns = defensive_interception_df.iloc[0]

passing_df = passing_df[1:]
receiving_df = receiving_df[1:]
rushing_df = rushing_df[1:]
scoring_df = scoring_df[1:]
defensive_interception_df = defensive_interception_df[1:]

passing_df.columns = passing_columns
receiving_df.columns = receiving_columns
rushing_df.columns = rushing_columns
scoring_df.columns = scoring_columns
defensive_interception_df.columns = defensive_interception_columns

# Grab todays date and format it for the Date logging
today = date.today()
d1 = today.strftime("%m-%d-%y")

# Add a new field in each df that shows a time stamp
passing_df['Date'] = d1
receiving_df['Date'] = d1
rushing_df['Date'] = d1
scoring_df['Date'] = d1
defensive_interception_df['Date'] = d1

print("The data is now cleaned up, next up is the writing of the data to the database!")

# Append new data to the sqlite3 database
conn = sqlite3.connect('nfl.db')
passing_df.to_sql('offensive_passing', conn, if_exists='append', index=False)
receiving_df.to_sql('offensive_receiving', conn, if_exists='append', index=False)
rushing_df.to_sql('offensive_rushing', conn, if_exists='append', index=False)
scoring_df.to_sql('offensive_scoring', conn, if_exists='append', index=False)
# defensive_interception_df.to_sql('defensive_interception', conn, if_exists='append', index=False)

# Close the connection
conn.close()

scoring_df.to_csv('scoring.csv')
print("The program is complete!")