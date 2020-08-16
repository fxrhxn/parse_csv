import csv  
import pandas as pd


# Get the path 
file_path = "CancelReport - 2020-06-09T121501.787.xls" 

# Read data, file is corrupted as an XLS but it works perfectly with a cvs 
data_xls = pd.read_html(file_path)


# Loop through list and write to csv. 
for i, table in enumerate(data_xls):
    print('Break --------')

    ## Break it off in to different files and format. 
    table.to_csv('list{}.csv'.format(i))

