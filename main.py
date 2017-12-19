import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import os

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open(os.environ['GSheet']).sheet1

pp = pprint.PrettyPrinter()

result = sheet.col_values(3)

pp.pprint(result)