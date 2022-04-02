# %%
import csv
from pathlib import Path 

# %%
#cache of data

data = []



# %%

csv_file=Path("PyBank/Resources/budget_data.csv")
with open(csv_file,"r") as file:
    csv_reader=csv.reader(file)
    header=next(csv_reader)
    
    for row in csv_reader:
        row[1] = float(row[1])
        data.append(row)
print(data)

# %%
total_months = len(data)

total_months

# %%
total_months = 86

# %%
total = 0
change = []

for i in range(total_months):
    total +=data[i][1] 
    if i != 0:
        change = data[i][1]-data[i-1][1] 
        print
total





