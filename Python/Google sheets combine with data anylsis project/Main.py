# importing libaries and code
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
import pandas as pd
from tkinter import *
from GUI_class_code.py import UseageGUI


# To get google to authenticate the api
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credemtials = ServiceAccountCredentials.from_json_keyfile_name('Python Spreadsheet Project-5fc4b718993a.json', scope)
gc = gspread.authorize(credemtials) #gc is now your google account, with the access to ur google sheets

# wks is now our worksheet object, note the first var passed has to be a string of the name of the spreadsheet
# on google sheets, also the method .sheetx is to specify which sheet, number.
wks = gc.open('Test Data for github test')

class GUI(UseageGUI):
    def __init__(self):
        



root = Tk()
root.geometry("600x250")
GUI(root)
root.mainloop()