# Improvements to make in the future
# 1. Use functions and a list to create the frameworks of the blanks
# 2. Use functions to make the framework of everthing more efficient

from tkinter import *
# Class declaration
class UseageGUIFramework(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Cool")
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
        self.amountLabel = Label(self.amountLabelframe, text="Amount")
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
        self.dateEntry = Entry(self.dateEntryFrame)
        self.dateEntry.place(x=0,y=0)
        # Month Entry
        self.monthEntryFrame = Frame(self, width=100, height=40)
        self.monthEntryFrame.grid(row=1, column=2)
        self.monthEntry = Entry(self.monthEntryFrame)
        self.monthEntry.place(x=0, y=0)
        # Year Entry
        self.yearEntryFrame = Frame(self, width=100, height=40)
        self.yearEntryFrame.grid(row=1, column=3)
        self.yearEntry = Entry(self.yearEntryFrame)
        self.yearEntry.place(x=0, y=0)
        # Amount
        self.amountEntryFrame = Frame(self, width=100, height=40)
        self.amountEntryFrame.grid(row=1, column=4)
        self.amountEntry = Entry(self.amountEntryFrame)
        self.amountEntry.place(x=0, y=0)
        # Category Entry
        self.categoryEntryFrame = Frame(self, width=100, height=40)
        self.categoryEntryFrame.grid(row=1, column=5)
        self.categoryEntry = Entry(self.categoryEntryFrame)
        self.categoryEntry.place(x=0, y=0)
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
        self.getDataButton = Button(self.getDataFrame, text="Get Data")
        self.getDataButton.place(anchor="nw")









# Main code
# root = Tk()
# root.geometry("600x450")
# UseageGUIFramework(root)
# root.mainloop()