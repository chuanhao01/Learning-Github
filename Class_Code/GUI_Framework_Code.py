# Improvements to make in the future
# 1. Use functions and a list to create the frameworks of the blanks
# 2. Use functions to make the framework of everthing more efficient

from tkinter import *
from tkinter import ttk
# Class declaration
class UseageGUIFramework(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("GUI For Personal Finance Tracker")
        self.pack(fill=BOTH, expand=1)
        self.getFrameworkOfWidgets()

    def getFrameworkOfWidgets(self):
        # Date
        self.dateLabelframe = LabelFrame(self, height=40, width=100)
        self.dateLabelframe.grid(row=0, column=1)
        self.dateLabel = Label(self.dateLabelframe, text="Date")
        self.dateLabel.place(anchor="center", x=50, y=18)
        # Month
        self.monthLabelframe = LabelFrame(self, height=40, width=100)
        self.monthLabelframe.grid(row=0, column=2)
        self.monthLabel = Label(self.monthLabelframe, text="Month")
        self.monthLabel.place(anchor="center", x=50, y=18)
        # Year
        self.yearLabelframe = LabelFrame(self, height=40, width=100)
        self.yearLabelframe.grid(row=0, column=3)
        self.yearLabel = Label(self.yearLabelframe, text="Year")
        self.yearLabel.place(anchor="center", x=50, y=18)
        # Amount
        self.amountLabelframe = LabelFrame(self, height=40, width=100)
        self.amountLabelframe.grid(row=0, column=4)
        self.amountLabel = Label(self.amountLabelframe, text="Amount\nSpent")
        self.amountLabel.place(anchor="center", x=50, y=18)
        # Category
        self.categoryLabelframe = LabelFrame(self, height=40, width=100)
        self.categoryLabelframe.grid(row=0, column=5)
        self.categoryLabel = Label(self.categoryLabelframe, text="Category")
        self.categoryLabel.place(anchor="center", x=50, y=18)
        # input
        self.inputsLabelframe = LabelFrame(self, height=40, width=100)
        self.inputsLabelframe.grid(row=1, column=0)
        self.inputsLabel = Label(self.inputsLabelframe, text="Inputs")
        self.inputsLabel.place(anchor="center", x=50, y=18)
        # Date entry
        self.dateEntryFrame = Frame(self, width=100, height=40)
        self.dateEntryFrame.grid(row=1, column=1)
        self.dateEntryFrame.grid_propagate(False)
        self.dateEntryFrame.rowconfigure(0, weight=1)
        self.dateEntryFrame.columnconfigure(0, weight=1)
        self.dateEntry = Entry(self.dateEntryFrame)
        self.dateEntry.grid(row=0, column=0)
        self.dateEntry.grid(sticky="nsew")
        # Month Entry
        self.monthEntryFrame = Frame(self, width=100, height=40)
        self.monthEntryFrame.grid(row=1, column=2)
        self.monthEntryFrame.grid_propagate(False)
        self.monthEntryFrame.rowconfigure(0, weight=1)
        self.monthEntryFrame.columnconfigure(0, weight=1)
        self.monthEntry = Entry(self.monthEntryFrame)
        self.monthEntry.grid(row=0, column=0)
        self.monthEntry.grid(sticky="nsew")
        # Year Entry
        self.yearEntryFrame = Frame(self, width=100, height=40)
        self.yearEntryFrame.grid(row=1, column=3)
        self.yearEntryFrame.grid_propagate(False)
        self.yearEntryFrame.rowconfigure(0, weight=1)
        self.yearEntryFrame.columnconfigure(0, weight=1)
        self.yearEntry = Entry(self.yearEntryFrame)
        self.yearEntry.grid(row=0, column=0)
        self.yearEntry.grid(sticky="nsew")
        # Amount
        self.amountEntryFrame = Frame(self, width=100, height=40)
        self.amountEntryFrame.grid(row=1, column=4)
        self.amountEntryFrame.grid_propagate(False)
        self.amountEntryFrame.rowconfigure(0, weight=1)
        self.amountEntryFrame.columnconfigure(0, weight=1)
        self.amountEntry = Entry(self.amountEntryFrame)
        self.amountEntry.grid(row=0, column=0)
        self.amountEntry.grid(sticky="nsew")
        # Category ComboBox
        self.categoryComboBoxFrame = Frame(self, width=100, height=40)
        self.categoryComboBoxFrame.grid(row=1, column=5)
        self.categoryComboBoxFrame.grid_propagate(False)
        self.categoryComboBoxFrame.rowconfigure(0, weight=1)
        self.categoryComboBoxFrame.columnconfigure(0, weight=1)
        self.categoryComboBox = ttk.Combobox(self.categoryComboBoxFrame)
        self.categoryComboBox.grid(row=0, column=0)
        self.categoryComboBox.grid(sticky="nsew")
        # Update
        self.updateButtonFrame = Frame(self, width=300, height=40)
        self.updateButtonFrame.grid(row=2, column=1, columnspan=3)
        self.updateButton = Button(self.updateButtonFrame, text="Update")
        self.updateButton.config(width=20, height=2)
        self.updateButton.place(anchor="center", x=150, y=20)
        # Label for Data label
        self.datalabelLabelframe = LabelFrame(self, height=40, width=100)
        self.datalabelLabelframe.grid(row=3, column=0)
        self.datalabelLabel = Label(self.datalabelLabelframe, text="Data")
        self.datalabelLabel.place(anchor="center", x=50, y=18)
        # Text to place data in
        self.dataFrame = Frame(self, height=240, width=600)
        self.dataFrame.grid(row=4, column=0, columnspan=6, rowspan=5)
        self.dataText = Text(self.dataFrame)
        self.dataText.place(anchor="nw")
        self.dataText.config(state=DISABLED)
        # Button to call for data
        self.getDataFrame = Frame(self, height=40, width=100)
        self.getDataFrame.grid(row=9, column=0)
        self.getDataFrame.grid_propagate(False)
        self.getDataFrame.rowconfigure(0, weight=1)
        self.getDataFrame.columnconfigure(0, weight=1)
        self.getDataButton = Button(self.getDataFrame, text="Get Data")
        self.getDataButton.grid(row=0, column=0)
        self.getDataButton.grid(sticky="nsew")
        # Button to get total money spent
        self.totalSpentFrame = Frame(self, height=40, width=100)
        self.totalSpentFrame.grid(row=9, column=1)
        self.totalSpentFrame.grid_propagate(False)
        self.totalSpentFrame.rowconfigure(0, weight=1)
        self.totalSpentFrame.columnconfigure(0, weight=1)
        self.totalSpentButton = Button(self.totalSpentFrame, text="Total Spent")
        self.totalSpentButton.grid(row=0, column=0)
        self.totalSpentButton.grid(sticky="nsew")
        # Button to get total spent by month
        self.totalSpentByMonthFrame = Frame(self, height=40, width=100)
        self.totalSpentByMonthFrame.grid(row=9, column=2)
        self.totalSpentByMonthFrame.grid_propagate(False)
        self.totalSpentByMonthFrame.rowconfigure(0, weight=1)
        self.totalSpentByMonthFrame.columnconfigure(0, weight=1)
        self.totalSpentByMonthButton = Button(self.totalSpentByMonthFrame, text="Total Spent\nBy Month")
        self.totalSpentByMonthButton.grid(row=0, column=0)
        self.totalSpentByMonthButton.grid(sticky="nsew")
        # Button to get bar graph for cat










# Main code
# root = Tk()
# root.geometry("600x450")
# UseageGUIFramework(root)
# root.mainloop()