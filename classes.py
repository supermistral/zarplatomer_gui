from PyQt5 import QtCore, QtGui, QtWidgets

class Dialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self, parent = None)
        #Main_Window = QtWidgets.QMainWindow(self)
        self.resize(200, 60)
        self.setFixedSize(self.size())
        self.label_err = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_err.setFont(font)
        self.label_err.setText("Что-то пошло не так...")
        self.label_err.move(20, 5)
        self.button = QtWidgets.QPushButton("OK", self)
        self.button.move(120, 30)
        self.setWindowModality(QtCore.Qt.ApplicationModal)


class Signal(QtCore.QObject):
    mysignal = QtCore.pyqtSignal()


class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)
    def __init__(self, mainwindow, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.mainwindow = mainwindow
        self.running = False
#    finish = Signal()

    def run(self):
        self.running = True
        if self.running:
            self.mainwindow.on_click()
        
    def delete(self): 
        self.mainwindow = None 
        self.terminate()