import gspread # spreadsheet lib
from oauth2client.service_account import ServiceAccountCredentials # authentication
from ast import literal_eval # convert strings to literals
import pprint # debug print
import os # environment variables
import json # type of file to generate

# SET UP
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open(os.environ['GSheet']).sheet1
pp = pprint.PrettyPrinter()

inputLabel = ["_id", "name", "flags", "quotes", "created_date", "__v"]
DB = {}
MAX_LENGTH = 138 # CURRENTLY 138 CHAMPIONS
ENTRY_LENGTH = len(inputLabel)


# CLEAR THE JSON FILE
with open('output.json', 'w') as f:
        f.write("")
print(f.closed)

for i in range(2, MAX_LENGTH):
    data = sheet.row_values(i)[:ENTRY_LENGTH] # grab our data on a specific row

    # INPUT DICT
    DB["_id"] = data[0]
    DB["flags"] = data[1]
    DB["name"] = data[2]
    DB["created_date"] = data[3]
    DB["__v"] = int(data[4])
    DB["quotes"] = literal_eval(data[5])
    
    with open('output.json', 'a') as f:
        f.write(json.dumps(DB) + "\n")
    # DUMP TO JSON FILE
    print(json.dumps(DB))