import sys
import os
import csv


from adodbapi.apibase import onIronPython

# Set the QT_API environment variable to use PyQt6
os.environ["QT_API"] = "pyqt6"

from qtpy import QtWidgets, QtCore
from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)



#bmi= [körpergewicht in kg] / ( [Körpergröße in m] ^2 )  -->kg ** 2

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.numOnDisplay= ""
        self.operation= ""
        self.firstOperand = float()
        self.secondOperand = float()
        self.operationResult = float()

        self.setWindowTitle("Rechner")

        self.updateDisplay()

        #Digits
        self.ui.zeroButton.clicked.connect(self.onZeroClicked)
        self.ui.oneButton.clicked.connect(self.onOneClicked)
        self.ui.twoButton.clicked.connect(self.onTwoClicked)
        self.ui.threeButton.clicked.connect(self.onThreeClicked)
        self.ui.fourButton.clicked.connect(self.onFourClicked)
        self.ui.fiveButton.clicked.connect(self.onFiveClicked)
        self.ui.sixButton.clicked.connect(self.onSixClicked)
        self.ui.sevenButton.clicked.connect(self.onSevenClicked)
        self.ui.eightButton.clicked.connect(self.onEightClicked)
        self.ui.nineButton.clicked.connect(self.onNineClicked)
        self.ui.commaButton.clicked.connect(self.onCommaClicked)

        self.ui.delButton.clicked.connect(self.onDelClicked)

        #operators:
        self.ui.multButton.clicked.connect(self.onMultClicked)
        self.ui.divideButton.clicked.connect(self.onDivClicked)
        self.ui.plusButton.clicked.connect(self.onplusClicked)
        self.ui.minusButton.clicked.connect(self.onMinusClicked)
        self.ui.equalsButton.clicked.connect(self.onEqualsClicked)


        #self.ui.newEntryButton.clicked.connect(self.onNewEntry)#button
        #self.ui.saveButton.clicked.connect(self.onSave)
        #self.ui.actionSave.triggered.connect(self.onSave)#Menüpunkt
        #self.ui.studentsTable.cellChanged.connect(self.onCellChanged) #table-Form
        #QtWidgets.QApplication.quit() #Quit application

    def onMultClicked(self):
        self.operation= "mult"
        self.firstOperand= float(self.numOnDisplay)
        self.numOnDisplay= ""
        self.updateDisplay()

    def onDivClicked(self):
        self.operation= "div"
        self.firstOperand= float(self.numOnDisplay)
        self.numOnDisplay= ""
        self.updateDisplay()

    def onplusClicked(self):
        self.operation= "plus"
        self.firstOperand= float(self.numOnDisplay)
        self.numOnDisplay= ""
        self.updateDisplay()

    def onMinusClicked(self):
        self.operation= "minus"
        self.firstOperand= float(self.numOnDisplay)
        self.numOnDisplay= ""
        self.updateDisplay()

    def updateDisplay(self):
        self.ui.display.setText(self.numOnDisplay)

    def onDelClicked(self):
        self.numOnDisplay = self.numOnDisplay[:-1]
        self.updateDisplay()

    def onEqualsClicked(self):
        self.secondOperand = float(self.numOnDisplay)
        self.numOnDisplay = ""

        if self.operation == "mult":
            self.operationResult= self.firstOperand * self.secondOperand
            self.numOnDisplay= str(self.operationResult)
            self.firstOperand = 0
            self.secondOperand = 0
            self.operationResult = 0
        elif self.operation == "div":
            self.operationResult = self.firstOperand / self.secondOperand
            self.numOnDisplay = str(self.operationResult)
            self.firstOperand = 0
            self.secondOperand = 0
            self.operationResult = 0
        elif self.operation == "plus":
            self.operationResult = self.firstOperand + self.secondOperand
            self.numOnDisplay = str(self.operationResult)
            self.firstOperand = 0
            self.secondOperand = 0
            self.operationResult = 0
        elif self.operation == "minus":
            self.operationResult = self.firstOperand - self.secondOperand
            self.numOnDisplay = str(self.operationResult)
            self.firstOperand = 0
            self.secondOperand = 0
            self.operationResult = 0
        self.updateDisplay()







    def onCommaClicked(self):
        self.numOnDisplay += "."
        self.updateDisplay()

    def onOneClicked(self):
        self.numOnDisplay += "1"
        self.updateDisplay()

    def onTwoClicked(self):
        self.numOnDisplay += "2"
        self.updateDisplay()

    def onThreeClicked(self):
        self.numOnDisplay += "3"
        self.updateDisplay()

    def onFourClicked(self):
        self.numOnDisplay += "4"
        self.updateDisplay()

    def onFiveClicked(self):
        self.numOnDisplay += "5"
        self.updateDisplay()

    def onSixClicked(self):
        self.numOnDisplay += "6"
        self.updateDisplay()

    def onSevenClicked(self):
        self.numOnDisplay += "7"
        self.updateDisplay()

    def onEightClicked(self):
        self.numOnDisplay += "8"
        self.updateDisplay()

    def onNineClicked(self):
        self.numOnDisplay += "9"
        self.updateDisplay()

    def onZeroClicked(self):
        self.numOnDisplay += "0"
        self.updateDisplay()







    def onOperatorClicked(self):
        divideClicked= self.ui.divideButton.clicked
        multClicked= self.ui.multButton.clicked
        plusClicked= self.ui.plusButton.clicked
        minClicked= self.ui.minusButton.clicked

        if divideClicked or multClicked or plusClicked or minClicked:
            return True
        else:
            return False




window = MainWindow()


window.show()

sys.exit(app.exec())

# C:\ProgramData\anaconda3\python.exe -m PyInstaller .\main.py  #for exe with all needed pyth files
#C:\ProgramData\anaconda3\python.exe -m PyInstaller --onefile main.py  #for onefile exe

#C:\ProgramData\anaconda3\python.exe -m PyInstaller --onefile -w main.py # for oneFile as windowed app(zb qt) ohne terminal
