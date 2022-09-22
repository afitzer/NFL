import pandas as pd
# from datetime import datetime, timedelta

# today = datetime.now()
# yesterday = today - timedelta(days=1)
# two_days_ago = today - timedelta(days=2)
  
#Reading two Excel Sheets
sheet1 = pd.read_csv(f'./Offensive_Teams/Passing/team_passing_09-20-22.csv')
sheet2 = pd.read_csv(f'./Offensive_Teams/Passing/team_passing_09-21-22.csv')
  
# Iterating the Columns Names of both Sheets
for i,j in zip(sheet1,sheet2):
     
    # Creating empty lists to append the columns values    
    a,b =[],[]
  
    # Iterating the columns values
    for m, n in zip(sheet1[i],sheet2[j]):
  
        # Appending values in lists
        a.append(m)
        b.append(n)
  
    # Sorting the lists
    a.sort()
    b.sort()
  
    # Iterating the list's values and comparing them
    for m, n in zip(range(len(a)), range(len(b))):
        if a[m] != b[n]:
            print('Column name : \'{}\' and Row Number : {}'.format(i,m))