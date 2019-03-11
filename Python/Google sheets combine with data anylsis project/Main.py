# importing libaries and code
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
import pandas as pd
from tkinter import *
from Class_Code.GUI_Framework_Code import UseageGUIFramework

# Shifted to class in worksheetData
# To get google to authenticate the api

# scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# credemtials = ServiceAccountCredentials.from_json_keyfile_name('Python Spreadsheet Project-5fc4b718993a.json', scope)
# gc = gspread.authorize(credemtials) #gc is now your google account, with the access to ur google sheets

# wks is now our worksheet object, note the first var passed has to be a string of the name of the spreadsheet
# on google sheets, also the method .sheetx is to specify which sheet, number.

# wks = gc.open('Test Data for github test')

# Commenting out code

# Class for worksheet interacting with G.sheets
class worksheetData:
    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credemtials = ServiceAccountCredentials.from_json_keyfile_name('Python Spreadsheet Project-5fc4b718993a.json',scope)
        gc = gspread.authorize(credemtials)
        self.wks = gc.open("Test Data for github test")
        self.worksheet = self.wks.worksheet("Sheet1")
        self.rowChooser = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


    # get data from google sheets, save in self.data as pandas dataframe
    def getDatafromGsheets(self):
        self.data = pd.DataFrame(self.wks.worksheet("Sheet1").get_all_values())
        return self.data

    # get dataframe with record
    def getDataInRecord(self):
        rtrString = pd.DataFrame(self.wks.worksheet("Sheet1").get_all_records())
        rtrString = str(rtrString)
        return rtrString
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
        # print(self.getDatafromGsheets())
        listOfNextRandC = []
        listOfNextRandC = self.getGFormatNextRowandColumn()
        # the slice string to get GObject for next Row
        stringOfNextRandC = listOfNextRandC[0] + ":" + listOfNextRandC[1]
        self.nextRowGObject = self.worksheet.range(stringOfNextRandC)
        for i in range(len(self.nextRowGObject)):
            self.nextRowGObject[i].value = updateData[i]
        self.worksheet.update_cells(self.nextRowGObject)



# Class for GUI, with framework imported from another file
class GUI(UseageGUIFramework, worksheetData):
    def __init__(self, master=None):
        # To call on the classes such that we can access the class_attributes
        UseageGUIFramework.__init__(self, master)
        worksheetData.__init__(self)
        # Assigning the update button to a method call
        self.updateButton.config(command= lambda :self.getDataFromEntry())
        # Assigning the get data button to a method call
        self.getDataButton.config(command= lambda :self.getDataToShow())

    # Method to get data in the Entry of the GUI, and place the data in a list, then calling another method to check
    def getDataFromEntry(self):
        self.listofdata = []
        self.listofdata.append(self.dateEntry.get())
        self.listofdata.append(self.monthEntry.get())
        self.listofdata.append(self.yearEntry.get())
        self.listofdata.append(self.amountEntry.get())
        self.listofdata.append(self.categoryEntry.get())
        # To check with console if the data is being sent through
        # print(self.listofdata)
        self.checkData()

    # Method to check if the data var type is correct, pushing the data onto the GSheets
    def checkData(self):
        # based on the data position in the list, change the string value in the list to its correct type
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

    # method called when get data button is pushed
    def getDataToShow(self):
        self.dataText.config(state=NORMAL)
        self.dataText.delete(0.0, END)
        dataToShow = worksheetData.getDataInRecord(self)
        self.dataText.insert(0.0, dataToShow)
        self.dataText.config(state=DISABLED)



root = Tk()
root.geometry("601x550")
GUI(root)
root.mainloop()

