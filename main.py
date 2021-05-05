# for gui:
from gui import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

# for simulator:
from physim import *


class MainWindow(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        # creating the window:
        super(MainWindow, self).__init__(*args, **kwargs)

        # set up the ui:
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # start simulation:
        self.e1 = Electron(vector(-1, 0, 0), vector(0, 0, 0))
        self.p1 = Proton(vector(0, sin(pi / 3), 0))
        self.e2 = Electron(vector(1, 0, 0), vector(3, 0, 0))
        self.sys = System([self.e1, self.p1, self.e2])
        self.main_sim_loop()

    def main_sim_loop(self):
        # rate(24)
        # rate(60)
        for p in self.sys.particles:
            print(p.sphere.pos)
        self.sys.update()
        qtc.QTimer.singleShot(25, self.main_sim_loop)


if __name__ == "__main__":
    app = qtw.QApplication([])
    widget = MainWindow()
    widget.show()
    app.exec_()
