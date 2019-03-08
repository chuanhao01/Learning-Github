import gspread
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
import pandas as pd


# To get google to authenticate the api
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credemtials = ServiceAccountCredentials.from_json_keyfile_name('Python Spreadsheet Project-5fc4b718993a.json', scope)
gc = gspread.authorize(credemtials) #gc is now your google account, with the access to ur google sheets

# wks is now our worksheet object, note the first var passed has to be a string of the name of the spreadsheet
# on google sheets, also the method .sheetx is to specify which sheet, number.
wks = gc.open('Test Data for github test')

# Testing some stuff, will write doc later
sheet1 = wks.worksheet("Sheet1")
sheet1Dataframe = pd.DataFrame(sheet1.get_all_records())
print(sheet1Dataframe)

sheet2 = wks.worksheet("Sheet2")
print(sheet2.get_all_records())
sheet2Dataframe = pd.DataFrame(sheet2.get_all_records())
print(sheet2Dataframe)
test_list = sheet2.range("A1:F2")
print(test_list)
print(type(test_list))
print(type(test_list[0]))
print(test_list[0])
test_list[0].value = "Z"
print(test_list[0])