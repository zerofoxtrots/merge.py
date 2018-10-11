import glob
import pandas as pd

# Path where your input files are being kept
path = "C:\\Users\\<USER>\\Desktop\\MergeFiles\\"

# Use this to adjust the extensions you'll be dealing with
file_identifier = "*.xls*"

# Create Data Frame objects to store all data for each Worksheet we want
Sheet1 = pd.DataFrame()
Sheet2 = pd.DataFrame()

# Loop through all files in your input directory
for f in glob.glob(path + "/*" + file_identifier):

    # Pull your excel file object into memory
    xls = pd.ExcelFile(f)

    # Read current worksheets into their own separate data frames
    df1 = pd.read_excel(xls, 'Sheet 1', skiprows=3)
    df2 = pd.read_excel(xls, 'Sheet 2', skiprows=3)

    # Append current worksheets to the master data frames
    Sheet1 = Sheet1.append(df1,ignore_index=True)
    Sheet2 = Sheet2.append(df2,ignore_index=True)

# Create writer object and give it path where you want file to be written
writer = pd.ExcelWriter('C:\\Users\<USER>\\Desktop\\MergeFiles\\merged.xlsx', engine='xlsxwriter')

# Write master data frames to the new file under their respective worksheet names
Sheet1.to_excel(writer, sheet_name='Sheet 1')
Sheet2.to_excel(writer, sheet_name='Sheet 2')

# Save the changes and release the file handle
writer.save()
