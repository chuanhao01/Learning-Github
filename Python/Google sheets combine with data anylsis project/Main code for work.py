import gspread
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
import pandas as pd
import tkinter as tk

# To get google to authenticate the api
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credemtials = ServiceAccountCredentials.from_json_keyfile_name('Python Spreadsheet Project-5fc4b718993a.json', scope)
gc = gspread.authorize(credemtials)

# wks is now our worksheet object, note the first var passed has to be a string of the name of the spreadsheet
# on google sheets, also the method .sheetx is to specify which sheet, number.
wks = gc.open('Test Data for github test').sheet1
# method to get all data from the sheet
print(wks.get_all_records())

