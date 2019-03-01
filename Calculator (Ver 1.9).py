# Known bugs
# Cannot decimail number / number?
# Number  = number?
# Multipole decimal point

# Library
from tkinter import *


# Class
class Calculator(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.displayList = []
        self.displayText = ""
        self.listOfNumbers = []
        self.init_window()

    # Creates a the window and frame for the whole calculator
    def init_window(self):
        self.master.title("Python Calculator")
        self.pack(fill=BOTH, expand=1)

        # Text Box
        displayTextBox = LabelFrame(self, height=70, width=265)
        displayTextBox.place(x=2, y=0)
        self.textToDisplay = Label(displayTextBox, font=("times new roman", "20"), width=17, height=1, anchor="ne")
        self.textToDisplay.place(x=0, y=25)

        # For Clear button flush to the left, leaving space for the main text bar
        clearButton = Button(self, command=self.clearButtonFunction, text="CE")
        clearButton.config(height=4, width=8)
        clearButton.place(x=0, y=75)
        # For subsequent button, will be seperated by a line
        zeroButton = Button(self, command=lambda: self.takeInNumberInput(0), text="0")
        zeroButton.config(height=4, width=8)
        zeroButton.place(x=0, y=361)

        oneButton = Button(self, command=lambda: self.takeInNumberInput(1), text="1")
        oneButton.config(height=4, width=8)
        oneButton.place(x=0, y=289)

        twoButton = Button(self, command=lambda: self.takeInNumberInput(2), text="2")
        twoButton.config(height=4, width=8)
        twoButton.place(x=67, y=289)

        threeButton = Button(self, command=lambda: self.takeInNumberInput(3), text="3")
        threeButton.config(height=4, width=8)
        threeButton.place(x=134, y=289)

        fourButton = Button(self, command=lambda: self.takeInNumberInput(4), text="4")
        fourButton.config(height=4, width=8)
        fourButton.place(x=0, y=218)

        fiveButton = Button(self, command=lambda: self.takeInNumberInput(5), text="5")
        fiveButton.config(height=4, width=8)
        fiveButton.place(x=67, y=218)

        sixButton = Button(self, command=lambda: self.takeInNumberInput(6), text="6")
        sixButton.config(height=4, width=8)
        sixButton.place(x=134, y=218)

        sevenButton = Button(self, command=lambda: self.takeInNumberInput(7), text="7")
        sevenButton.config(height=4, width=8)
        sevenButton.place(x=0, y=147)

        eightButton = Button(self, command=lambda: self.takeInNumberInput(8), text="8")
        eightButton.config(height=4, width=8)
        eightButton.place(x=67, y=147)

        nineButton = Button(self, command=lambda: self.takeInNumberInput(9), text="9")
        nineButton.config(height=4, width=8)
        nineButton.place(x=134, y=147)

        additionButton = Button(self, command=lambda :self.basicOperation("+"), text="+")
        additionButton.config(height=4, width=8)
        additionButton.place(x=201, y=289)

        multiplicationButton = Button(self, command=lambda :self.basicOperation("*"), text="x")
        multiplicationButton.config(height=4, width=8)
        multiplicationButton.place(x=201, y=147)

        subtractionButton = Button(self, command=lambda :self.basicOperation("-"), text="-")
        subtractionButton.config(height=4, width=8)
        subtractionButton.place(x=201, y=218)

        divideButton = Button(self, command=lambda :self.basicOperation("/"), text="/")
        divideButton.config(height=4, width=8)
        divideButton.place(x=201, y=75)

        backspaceButton = Button(self, command=self.backspaceFunctionPress, text="<=")
        backspaceButton.config(height=4, width=8)
        backspaceButton.place(x=134, y=75)

        cButton = Button(self, command=self.cButtonFunctionPress, text="C")
        cButton.config(height=4, width=8)
        cButton.place(x=67, y=75)

        negativeButton = Button(self, command=self.negativeButtonFunctionPress, text="-")
        negativeButton.config(height=4, width=8)
        negativeButton.place(x=67, y=361)

        decimalButton = Button(self, command=self.decimalFunctionPress, text=".")
        decimalButton.config(height=4, width=8)
        decimalButton.place(x=134, y=361)

        equalsButton = Button(self, command=self.equalsFunctionPress, text="=")
        equalsButton.config(height=4, width=8)
        equalsButton.place(x=201, y=361)

    # clears the saved number after an operation
    def clearChache(self):
        self.displayList = []
        self.displayText = ""

    # Clears all cache
    def clearButtonFunction(self):
        self.displayList = []
        self.displayText = ""
        self.listOfNumbers = []
        self.textToDisplay.config(text=self.displayText)

    # Appends the number onto the list
    def takeInNumberInput(self, inputInteger):
        self.displayList.append(str(inputInteger))
        self.getDisplayText()

    # Called when the cache is full and need to get a output number, look at self.basicOperation for use and
    # self.equalsFunctionPress
    def getOutputNumber(self):
        try:
            if self.listOfNumbers[1] == "+":
               return self.listOfNumbers[0] + int(self.displayText)
            elif self.listOfNumbers[1] == "*":
                return self.listOfNumbers[0] * int(self.displayText)
            elif self.listOfNumbers[1] == "-":
                return self.listOfNumbers[0] - int(self.displayText)
            elif self.listOfNumbers[1] == "/":
                return self.listOfNumbers[0] / int(self.displayText)
        except:
            if self.listOfNumbers[1] == "+":
               return self.listOfNumbers[0] + float(self.displayText)
            elif self.listOfNumbers[1] == "*":
                return self.listOfNumbers[0] * float(self.displayText)
            elif self.listOfNumbers[1] == "-":
                return self.listOfNumbers[0] - float(self.displayText)
            elif self.listOfNumbers[1] == "/":
                return self.listOfNumbers[0] / float(self.displayText)

    # The function called when any operator is pressed, i.e. + - / *
    def basicOperation(self, operation):
        try:
            # If there is no cache then store the current number in the cache with operation next
            if len(self.listOfNumbers) == 0:
                self.listOfNumbers.append(int(self.displayText))
                self.listOfNumbers.append(operation)
            # If there is only one number in the cache( i.e. from the equals function), then append the sign to the cache
            elif len(self.listOfNumbers) == 1:
                self.listOfNumbers.append(operation)
            # If there is a stored cache of number and operation(length of list == 2), then perform the operation(in the
            # stored cache) with the current number and cache number. This is done by calling the function
            # self.getOutputNumber. Then reset the list, append the output number to the list with the pressed operation
            else:
                temp = self.getOutputNumber()
                self.listOfNumbers = []
                self.listOfNumbers.append(temp)
                self.listOfNumbers.append(operation)
                self.textToDisplay.config(text=str(temp))
            self.clearChache()
        except:
            pass


    # pop the last number in the list and updates the number shown
    def backspaceFunctionPress(self):
        if len(self.displayList) > 0:
            self.displayList.pop(len(self.displayList) - 1)
            self.getDisplayText()
        else:
            pass

    # Clears the cuurent number shown, displaylist and displaytext, and then updates the text shown
    def cButtonFunctionPress(self):
        self.clearChache()
        self.getDisplayText()

    # Checks if there is number in the list
    # If there is(length of list > 0) then append a negative sign to the front of the list
    # IF not then just append a negative sign to the front
    # Updates the number at the end
    def negativeButtonFunctionPress(self):
        if len(self.displayList) > 0:
            if self.displayList[0] != "-":
                temp = self.displayList
                self.displayList = []
                self.displayList.append("-")
                for i in temp:
                    self.displayList.append(i)
                self.getDisplayText()

            elif self.displayList[0] == "-":
                self.displayList.pop(0)
                self.getDisplayText()
        elif len(self.displayList) == 0:
            self.displayList.append("-")
            self.getDisplayText()

    # checks for length of current number
    # if no number(length is 0) then append 0 and . to the display list
    # if theres is a number, then just append a . to the list
    def decimalFunctionPress(self):
        if len(self.displayList) > 0:
            self.displayList.append(".")
            self.getDisplayText()
        elif len(self.displayList) == 0:
            self.displayList.append("0")
            self.displayList.append(".")
            self.getDisplayText()

    # With cache and a currently displayed number, get output and update the text shown
    def equalsFunctionPress(self):
        try:
            temp = self.getOutputNumber()
            self.textToDisplay.config(text=str(temp))
            self.listOfNumbers = []
            self.listOfNumbers.append(temp)
            self.clearChache()
        except:
            pass

    def getDisplayText(self):
        self.displayText = "".join(self.displayList)
        self.textToDisplay.config(text=self.displayText)


# Main Code
root = Tk()
root.geometry("270x435")

app = Calculator(root)

root.mainloop()



