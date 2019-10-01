# Author: Raihan Shafique
# This code has been tried in Python version 3.6


import sqlalchemy as db
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, select
import PIL.Image
import io
import os

# Get Current Directory to save file later in this location.
cwd = os.getcwd()

# Connect to SQL Server DB - Python3.6 virtual env
server = 'YourServerName'
database = 'YourSQLDBName'
username = 'YouUserName'


f=open(cwd+'\email_password.txt', "r")
password = f.readline()


#SQL alchemy engine details
engineString = 'mssql+pyodbc://'+username+':'+password+'@'+server+':1433/'+database+'?driver=SQL Server Native Client 11.0'

engine = db.create_engine(engineString)
conn = engine.connect()

# Run your sql commmand to extract the varbinary image data - change accordingly
result = conn.execute("Select Top(2) * from PApps_IssueReporting_FACT_Room_Faults_Attachments")

# Extract the data from result.
for row in result:
    print(row)
    print(row[1])

imagedata = row[2]
result.close()

# An unnecessary step because I was lazy :)
s = imagedata


# Wrap the bytes in a memory stream that can be read like a file.
bytes = io.BytesIO(s)


# Use pillow to read the memory stream into an image (it autodetects the format).
im = PIL.Image.open(bytes)
# And show it. Or you could .save() it.
im.show()

im.save(cwd+'\image.bmp')




