import io 
import pandas as pd
import os 
import numpy as np
# clear the screen

os.system("clear")

# random file, but use this url: 

#url = "https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv"
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/nile.csv"
table_1 = pd.read_csv(url)

result= table_1.describe()

print(result)

result = table_1.head()

print(result)

# load data from the computer 

"""

import pandas as pd
import io 

#dialog to upload from computer:

uploaded = files.upload()
file_name = next(iter(uploaded))
table_1 = pd.read_csv(io.BytesIO(uploaded[file_name]))
print(table_1)

"""
"""
# WPct

wins = np.array(table_1["Wins"])
losses = np.array(table_1["Losses"])
avg = wins/(wins+losses)

#print(avg)

table_1["Average"] = avg
print(table_1[["Manager","WPct"]])
"""

