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

        # electrical interaction between particles - gui:
        self.ui.add_particle_button.clicked.connect(self.add_particle)

        # global variables:
        self.paused = True
        self.frame_rate = 24
        self.is_still_running = True

        # start simulation:
        temp_shape = sphere(opacity=0)
        del temp_shape

        self.system = System([])
        self.main_sim_loop()

    def main_sim_loop(self):
        rate(self.frame_rate)
        if not self.paused:
            self.system.update()
        if self.is_still_running:
            qtc.QTimer.singleShot(25, self.main_sim_loop)
        else:
            pass

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
        try:
            x_pos = default_value(self.ui.x_eibp_position_line_edit.text())
            y_pos = default_value(self.ui.y_eibp_position_line_edit.text())
            z_pos = default_value(self.ui.z_eibp_position_line_edit.text())

            x_vel = default_value(self.ui.x_eibp_velocity_line_edit.text())
            y_vel = default_value(self.ui.y_eibp_velocity_line_edit.text())
            z_vel = default_value(self.ui.z_eibp_velocity_line_edit.text())

            x_acc = default_value(self.ui.x_eibp_acceleration_line_edit.text())
            y_acc = default_value(self.ui.y_eibp_acceleration_line_edit.text())
            z_acc = default_value(self.ui.z_eibp_acceleration_line_edit.text())

            charge = default_value(self.ui.charge_eibp_line_edit.text())
            mass = default_value_mass(self.ui.mass_eibp_line_edit.text())
        except TypeError:
            qtw.QMessageBox.critical(None, 'Fail', "arguments for creating particles must be numbers.")
            return

        position = vector(x_pos, y_pos, z_pos)
        velocity = vector(x_vel, y_vel, z_vel)
        acceleration = vector(x_acc, y_acc, z_acc)

        new_particle = Particle(position, velocity, acceleration, charge, mass, color.white)
        self.system.particles.append(new_particle)

        index = self.ui.particle_list.count()
        self.ui.particle_list.addItem(f"particle {index}")

    def closeEvent(self, event):
        close = qtw.QMessageBox()
        close.setText("You sure?")
        close.setStandardButtons(qtw.QMessageBox.Yes | qtw.QMessageBox.Cancel)
        close = close.exec()

        if close == qtw.QMessageBox.Yes:
            event.accept()
            self.is_still_running = False
        else:
            event.ignore()

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
