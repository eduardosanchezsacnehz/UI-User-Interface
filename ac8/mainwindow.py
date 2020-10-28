from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindows import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        ui = Ui_MainWindow()
        ui.setupUi(self)

        ui.agrega_final_pushButton.clicked.connect(self.click_agregar)

    @Slot()
    def click_agregar(self):
        print('click')