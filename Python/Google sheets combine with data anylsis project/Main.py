# importing libaries and code
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
import pandas as pd
from tkinter import *
from Class_Code.GUI_class_code import UseageGUI


# To get google to authenticate the api
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credemtials = ServiceAccountCredentials.from_json_keyfile_name('Python Spreadsheet Project-5fc4b718993a.json', scope)
gc = gspread.authorize(credemtials) #gc is now your google account, with the access to ur google sheets

# wks is now our worksheet object, note the first var passed has to be a string of the name of the spreadsheet
# on google sheets, also the method .sheetx is to specify which sheet, number.
wks = gc.open('Test Data for github test')

# Class for worksheet interacting with G.sheets
class worksheetData:
    def __init__(self):
        self.rowChooser = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


    # get data from google sheets, save in self.data as pandas dataframe
    def getDatafromGsheets(self):
        self.data = pd.DataFrame(wks.worksheet("Sheet1").get_all_values())


    # get row and column for Gsheets, return in google sheets format
    def getGFormatNextRowandColumn(self):
        self.getDatafromGsheets()
        tempListOfRandC = [] # This is to save the R and C in a list so we can change the value ltr, rather than the data be in a tuple
        listToReturn = [] # List containing the R and C in Gsheet format
        for i in self.data.shape:
            tempListOfRandC.append(i)
        # Since row need to add one for down, as we want to add a new row
        tempListOfRandC[0] += 1
        # We want to reduce the no. of col. by one as we want the same alp., but arrays start at 1
        tempListOfRandC[1] -= 1
        # Appends the A + number and last alp. + num to listToReturn
        listToReturn.append("A"+str(tempListOfRandC[0]))
        listToReturn.append(self.rowChooser[tempListOfRandC[1]] + str(tempListOfRandC[0]))
        return listToReturn



class GUI(UseageGUI):
    def __init__(self, master=None):
        UseageGUI.__init__(self, master)
        self.updateButton.config(command= lambda :self.callme())

    def callme(self):
        print("Hi")


# root = Tk()
# root.geometry("600x250")
# a = GUI(root)
# root.mainloop()
a = pd.DataFrame(wks.worksheet("Sheet1").get_all_values())
print(a)
print(a.shape)
b = worksheetData()
b.getGFormatNextRowandColumn()
