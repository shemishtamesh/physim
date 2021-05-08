# for gui:
from gui import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

# for simulator:
from physim import *

# for exception handling:
import sys


class MainWindow(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        # creating the window:
        super(MainWindow, self).__init__(*args, **kwargs)

        # set up the ui:
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # set up simulation controls:
        self.ui.run_button.clicked.connect(self.run)
        self.ui.pause_button.clicked.connect(self.pause)
        self.ui.set_frame_rate_button.clicked.connect(self.set_frame_rate)

        # electrical interaction between particles
        self.ui.add_particle_button.clicked.connect(self.add_particle)

        # global variables:
        self.paused = True
        self.frame_rate = 24

        # start simulation:
        self.e1 = Electron(vector(-1, 0, 0), vector(0, 0, 0))
        self.p1 = Proton(vector(0, sin(pi / 3), 0))
        self.e2 = Electron(vector(1, 0, 0), vector(3, 0, 0))
        self.system = System([self.e1, self.p1, self.e2])
        self.main_sim_loop()

    def main_sim_loop(self):
        rate(self.frame_rate)
        if not self.paused:
            for p in self.system.particles:
                print(p.sphere.pos)
            self.system.update()

        qtc.QTimer.singleShot(25, self.main_sim_loop)

    # for simulation controls:
    def run(self):
        self.paused = False

    def pause(self):
        self.paused = True

    def set_frame_rate(self):
        try:
            new_frame_rate = float(self.ui.frame_rate_line_edit.text())
            if new_frame_rate > 0:
                self.frame_rate = new_frame_rate
            else:
                qtw.QMessageBox.critical(None, 'Fail', "frame rate must be grater than 0.")
        except ValueError:
            qtw.QMessageBox.critical(None, 'Fail', "frame rate must be a number.")

    # for electrical interaction between particles:
    def add_particle(self):
        index = self.ui.particle_list.count()
        self.ui.particle_list.addItem(f"particle {index}")


if __name__ == "__main__":
    # for handling exceptions:
    sys._excepthook = sys.excepthook

    def exception_hook(exctype, value, traceback):
        print(traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)

    sys.excepthook = exception_hook


    app = qtw.QApplication([])
    widget = MainWindow()
    widget.show()
    app.exec_()
