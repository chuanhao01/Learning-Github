# importing libaries and code
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
import pandas as pd
from tkinter import *
from Class_Code.GUI_Framework_Code import UseageGUIFramework
import matplotlib.pyplot as plt


class worksheetData:
    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credemtials = ServiceAccountCredentials.from_json_keyfile_name('Python Spreadsheet Project-ce3d5816fe9e.json',scope)
        gc = gspread.authorize(credemtials)
        self.wks = gc.open("Test Data for github test")
        self.worksheet = self.wks.worksheet("Sheet1")
        # used in formating pandas index and columns into GSheets index and cloumn
        self.rowChooser = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        # Used to get in method for amount spent per month
        self.Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # get data from google sheets, save in self.data as pandas dataframe
    def getDatafromGsheets(self):
        self.data = pd.DataFrame(self.wks.worksheet("Sheet1").get_all_values())
        return self.data

    # get dataframe with record, save to self.dataRecord, and return the dataframe
    def getDatafromGsheetsInRecord(self):
        self.dataRecord = pd.DataFrame(self.wks.worksheet("Sheet1").get_all_records())
        return self.dataRecord

    # method to call and pass a (year) dataframe as a arg, sort by month then date,
    # return list of of sorted data with january at the start
    # check for any other method calling this one as we are only considering 1 year(2019) for now
    def getSortedDataInRecordList(self, data):
        uniqueValues = data.loc[:, "Month"].unique()
        lisToReturn = []
        for i in uniqueValues:
            lisToReturn.append(data.loc[data["Month"]==int(i), :].sort_values(by=["Month", "Date of expenditure"]))
        return lisToReturn

    # method to get dataframes sorted by categories, return as a list of dataframes of each category
    def getSortedDataByCategoryList(self, data):
        uniqueValues = data.loc[:, "Category"].unique()
        lisToReturn = []
        for i in uniqueValues:
            lisToReturn.append(data.loc[data.loc[:, "Category"] == i, :])
        # print(lisToReturn)
        return lisToReturn

    # method to plot total money spent by category, for button
    def getPlotForTotalMoneySpentByCategory(self):
        lisOfCategoryData = self.getSortedDataByCategoryList(self.getDatafromGsheetsInRecord())
        for i in lisOfCategoryData:
            # plots a bar for each category
            temp = plt.bar([str(i.loc[:, "Category"].unique()[0])], i.loc[:, "Amount"].sum())
            for rect in temp:
                plt.text(rect.get_x() + rect.get_width() / 2.0, rect.get_height(), "$%d" % int(rect.get_height()), ha='center', va='bottom')
        plt.xlabel("Categories")
        plt.ylabel("Total Money Spent")
        plt.show()

    # method to call to get string of sorted dataframe(by month then date), returning string
    def getSortedDataInRecordString(self):
        lisOfData = self.getSortedDataInRecordList(self.getDatafromGsheetsInRecord())
        rtrString = ""
        for i in lisOfData:
            rtrString = rtrString + str(i)
            rtrString = rtrString + "\n"
        return rtrString

    # get dataframe with record, return string
    def getDataInRecordString(self):
        rtrString = str(self.getDatafromGsheetsInRecord())
        return rtrString

    # get total spent and return as a series, series is set to self.amountSpentSeries
    def getAmountSpentSeries(self):
        self.getDatafromGsheetsInRecord()
        self.amountSpentSeries = self.dataRecord.loc[:, "Amount"]
        return self.amountSpentSeries

    # get total amount spent and return as string
    def getTotalAmountSpent(self):
        self.getAmountSpentSeries()
        self.totalAmountspent = self.amountSpentSeries.sum()
        return str(self.totalAmountspent)

    # get spent by month.
    def getMoneySpentByMonth(self):
        self.getDatafromGsheetsInRecord()
        dataFrameForAmountSpentBYMonth = pd.DataFrame(index=self.Months,columns=["Total Amount"])
        # use booleanindexing to get data only from the months
        for i in range(1,13):
            # gets the sum of amount spent in i month
            amountSpentPerMonth = 0
            amountSpentPerMonth = self.dataRecord.loc[self.dataRecord.loc[:, "Month"] == i, "Amount"].sum()
            # Places the sum to the index of the month in the dataframe
            dataFrameForAmountSpentBYMonth.loc[self.Months[i-1],"Total Amount"] = amountSpentPerMonth
        # Returns the dataframe as a string
        return str(dataFrameForAmountSpentBYMonth)


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
        # Assigning the buttons to the methods
        self.updateButton.config(command= lambda :self.getDataFromEntry())
        self.getDataButton.config(command= lambda :self.getDataToShow("Get Data"))
        self.totalSpentButton.config(command=lambda :self.getDataToShow("Total Spent"))
        self.totalSpentByMonthButton.config(command=lambda :self.getDataToShow("Total Spent\nBy Month"))
        self.getSortedDataButton.config(command=lambda :self.getDataToShow("Get Sorted Data"))
        self.getTotalMoneySpentByCategoryButton.config(command=lambda :worksheetData.getPlotForTotalMoneySpentByCategory(self))
        # Assigning list for combobox
        self.categoryList = ["Food", "Shopping", "Transport", "Home", "Savings", "Healthcare", "Education", "Groceries", "Work", "Others"]
        self.categoryComboBox.config(values=self.categoryList)

    # Method to get data in the Entry of the GUI, and place the data in a list, then calling another method to check
    def getDataFromEntry(self):
        self.listofdata = []
        self.listofdata.append(self.dateEntry.get())
        self.listofdata.append(self.monthEntry.get())
        self.listofdata.append(self.yearEntry.get())
        self.listofdata.append(self.amountEntry.get())
        self.listofdata.append(self.categoryComboBox.get())
        # To check with console if the data is being sent through
        # print(self.listofdata)
        self.checkData()

    # Method to check if the data var type is correct, pushing the data onto the GSheets, also handles catching exceptions
    def checkData(self):
        # To catch the exception where not all the entry fields are filled in
        if len(self.listofdata) < 5:
            self.getDataToShow("missingParameters")
            return
        # based on the data position in the list, change the string value in the list to its correct type
        for i in range(5):
            if i < 3:
                try:
                    self.listofdata[i] = int(self.listofdata[i])
                except:
                    # To catch the exception if the Date, Month and year are not numbers
                    self.getDataToShow("error type 1")
                    return
            elif 2<i<4:
                try:
                    self.listofdata[i] = float(self.listofdata[i])
                except:
                    # To catch the exception where the amount is not a number
                    self.getDataToShow("error type 2")
                    return
        # Pushing data if its correct onto GSheets
        worksheetData.updateGSheetsWithData(self,self.listofdata)


    # method called when get data button is pushed
    # method is also used to catch exceptions in updating data
    def getDataToShow(self, indexOfBox):
        self.dataText.config(state=NORMAL)
        self.dataText.delete(0.0, END)
        dataToShow = ""
        if indexOfBox == "Get Data":
            dataToShow = worksheetData.getDataInRecordString(self)
        elif indexOfBox == "Total Spent":
            dataToShow = "Total Amount Spent\n" + worksheetData.getTotalAmountSpent(self)
        elif indexOfBox == "Total Spent\nBy Month":
            dataToShow = worksheetData.getMoneySpentByMonth(self)
        elif indexOfBox == "Get Sorted Data":
            dataToShow = worksheetData.getSortedDataInRecordString(self)
        elif indexOfBox == "missingParameters":
            dataToShow = "Some values from the entry boxes are missing!"
        elif indexOfBox == "error type 1":
            dataToShow = "The values in the data, month, year are not all numbers"
        elif indexOfBox == "error type 2":
            dataToShow = "The value for amount spent is not a number"
        self.dataText.insert(0.0, dataToShow)
        self.dataText.config(state=DISABLED)



root = Tk()
root.geometry("603x550")
GUI(root)
root.mainloop()

