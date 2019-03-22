from Main import worksheetData as WK
import matplotlib.pyplot as plt

class Data(WK):
    def __init__(self):
        WK.__init__(self)
        self.getDatafromGsheetsInRecord()


    def __str__(self):
        return str(self.dataRecord)

    def getBar(self):
        tempData = self.dataRecord.loc[:, "Amount":"Category"]
        totalOfSpent = tempData.loc[self.dataRecord["Category"] == "Food", "Amount"].sum()
        totalOfSpent1 = tempData.loc[self.dataRecord["Category"] == "Groceries", "Amount"].sum()
        a = [totalOfSpent, totalOfSpent1]
        return a

a = Data()
print(a)
b = a.getBar()
plt.bar(["Food"], b[0])
plt.bar(["Groceries"], b[1])
plt.show()
