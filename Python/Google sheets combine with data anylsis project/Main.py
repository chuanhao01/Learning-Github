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
    def __init__(self,wks):
        self.wks = wks
        self.worksheet = self.wks.worksheet("Sheet1")
        self.rowChooser = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


    # get data from google sheets, save in self.data as pandas dataframe
    def getDatafromGsheets(self):
        self.data = pd.DataFrame(self.wks.worksheet("Sheet1").get_all_values())
        return self.data


    # get row and column for Gsheets, return next row in google sheets format
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

    # This method is called when the update button is pushed from the GUI
    def updateGSheetsWithData(self, updateData):
        print(self.getDatafromGsheets())
        listOfNextRandC = []
        listOfNextRandC = self.getGFormatNextRowandColumn()
        # the slice string to get GObject for next Row
        stringOfNextRandC = listOfNextRandC[0] + ":" + listOfNextRandC[1]
        self.nextRowGObject = self.worksheet.range(stringOfNextRandC)
        for i in range(len(self.nextRowGObject)):
            self.nextRowGObject[i].value = updateData[i]
        self.worksheet.update_cells(self.nextRowGObject)





class GUI(UseageGUI, worksheetData):
    def __init__(self, master=None):
        UseageGUI.__init__(self, master)
        worksheetData.__init__(self,wks)
        self.updateButton.config(command= lambda :self.getData())

    # Method to get data in the Entry of the GUI, and place the data in a list, then calling another method to check
    def getData(self):
        self.listofdata = []
        self.listofdata.append(self.dateEntry.get())
        self.listofdata.append(self.monthEntry.get())
        self.listofdata.append(self.yearEntry.get())
        self.listofdata.append(self.amountEntry.get())
        self.listofdata.append(self.categoryEntry.get())
        print(self.listofdata)
        self.checkData()

    # Method to check if the data var type is correct, then calling another method to format the data if the data is correct
    def checkData(self):
        for i in range(5):
            if i < 3:
                try:
                    self.listofdata[i] = int(self.listofdata[i])
                except:
                    return
            elif 2<i<4:
                try:
                    self.listofdata[i] = float(self.listofdata[i])
                except:
                    return
        worksheetData.updateGSheetsWithData(self,self.listofdata)


root = Tk()
root.geometry("600x250")
a = GUI(root)
root.mainloop()
a = pd.DataFrame(wks.worksheet("Sheet1").get_all_values())
print(a)
print(a.shape)
