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
        self.ui.reset_button.clicked.connect(self.reset_system)

        # electrical interaction between particles:
        self.ui.add_particle_button.clicked.connect(self.add_particle)
        self.ui.remove_particle_button.clicked.connect(self.remove_particle)
        self.ui.clear_particle_list_button.clicked.connect(self.clear_list)
        self.ui.red_slider.setValue(99)
        self.ui.green_slider.setValue(99)
        self.ui.blue_slider.setValue(99)

        # electro-magnetic effect of fields on a particle:
        self.ui.add_fields_button.clicked.connect(self.add_field)
        self.ui.red_field_slider.setValue(99)
        self.ui.green_field_slider.setValue(99)
        self.ui.blue_field_slider.setValue(99)

        # global variables:
        self.paused = True
        self.frame_rate = 24
        self.is_still_running = True

        # start simulation:
        x_axis = arrow(pos=vector(-10, -10, -10), axis=vector(20, 0, 0), shaftwidth=0.2, color=color.red)
        y_axis = arrow(pos=vector(-10, -10, -10), axis=vector(0, 20, 0), shaftwidth=0.2, color=color.blue)
        z_axis = arrow(pos=vector(-10, -10, -10), axis=vector(0, 0, 20), shaftwidth=0.2, color=color.green)

        self.eibp_system_start = None
        self.eibp_system = EibpSystem([])

        self.emeofoap_system_start = None
        self.emeofoap_system = EmeofoapSystem([])

        self.main_sim_loop()

    def main_sim_loop(self):
        curret_tab = self.ui.tabWidget.currentIndex()
        rate(self.frame_rate)
        if curret_tab == 0:  # tab number 0 is eibp
            self.emeofoap_system.make_invisible()
            self.eibp_system.make_visible()
            if not self.paused:
                self.eibp_system.update()
        else:  # the other tab is emeofoap
            self.eibp_system.make_invisible()
            self.emeofoap_system.make_visible()
            if not self.paused:
                self.emeofoap_system.update()

        if self.is_still_running:
            qtc.QTimer.singleShot(25, self.main_sim_loop)

    # for simulation controls:
    def reset_system(self):
        self.paused = True

        self.ui.add_particle_button.setEnabled(True)
        self.ui.remove_particle_button.setEnabled(True)
        self.ui.clear_particle_list_button.setEnabled(True)

        if self.eibp_system_start:
            self.eibp_system.make_invisible()
            while len(self.eibp_system.particles) > 0:
                self.eibp_system.remove_particle(0)
            self.eibp_system = self.eibp_system_start
            self.eibp_system_start = None
            self.eibp_system.make_visible()

    def run(self):
        self.paused = False

        self.ui.add_particle_button.setEnabled(False)
        self.ui.remove_particle_button.setEnabled(False)
        self.ui.clear_particle_list_button.setEnabled(False)

        if not self.eibp_system_start:
            self.eibp_system_start = EibpSystem()
            for particle in self.eibp_system.particles:
                self.eibp_system_start.particles.append(sphere(pos=particle.pos,
                                                               color=particle.color,
                                                               radius=0.1,
                                                               mass=particle.mass,
                                                               acceleration=particle.acceleration,
                                                               charge=particle.charge,
                                                               velocity=particle.velocity,
                                                               make_trail=particle.make_trail))

            self.eibp_system_start.make_invisible()

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
            x_pos = default_value_0(self.ui.x_eibp_position_line_edit.text())
            y_pos = default_value_0(self.ui.y_eibp_position_line_edit.text())
            z_pos = default_value_0(self.ui.z_eibp_position_line_edit.text())

            x_vel = default_value_0(self.ui.x_eibp_velocity_line_edit.text())
            y_vel = default_value_0(self.ui.y_eibp_velocity_line_edit.text())
            z_vel = default_value_0(self.ui.z_eibp_velocity_line_edit.text())

            x_acc = default_value_0(self.ui.x_eibp_acceleration_line_edit.text())
            y_acc = default_value_0(self.ui.y_eibp_acceleration_line_edit.text())
            z_acc = default_value_0(self.ui.z_eibp_acceleration_line_edit.text())

            charge = default_value_0(self.ui.charge_eibp_line_edit.text())
            mass = default_value_1(self.ui.mass_eibp_line_edit.text())
        except TypeError:
            qtw.QMessageBox.critical(None, 'Fail', "arguments for creating particles must be numbers.")
            return

        position = vector(x_pos, y_pos, z_pos)
        velocity = vector(x_vel, y_vel, z_vel)
        acceleration = vector(x_acc, y_acc, z_acc)

        particle_color = vector(self.ui.red_slider.value()/99,
                                self.ui.green_slider.value()/99,
                                self.ui.blue_slider.value()/99)

        does_have_trail = self.ui.trail_check_box.isChecked()

        new_particle = sphere(pos=position,
                              color=particle_color,
                              radius=0.1,
                              mass=mass,
                              acceleration=acceleration,
                              charge=charge,
                              velocity=velocity,
                              make_trail=does_have_trail)

        self.eibp_system.particles.append(new_particle)

        particle_name = self.ui.name_input_line.text()
        if particle_name:
            self.ui.particle_list.addItem(self.ui.name_input_line.text())
        else:
            particle_index = self.ui.particle_list.count()
            self.ui.particle_list.addItem(f"particle {particle_index}")

    def remove_particle(self):
        try:
            self.ui.particle_list.selectedItems()[0]
        except IndexError:
            qtw.QMessageBox.critical(None, 'Fail', "you have to select a particle if you want to remove one.")
            return

        are_you_sure_message = qtw.QMessageBox()
        are_you_sure_message.setText("Are you sure?")
        are_you_sure_message.setStandardButtons(qtw.QMessageBox.Yes | qtw.QMessageBox.Cancel)
        are_you_sure_message = are_you_sure_message.exec()

        if are_you_sure_message == qtw.QMessageBox.Yes:
            index_on_list = self.ui.particle_list.currentRow()
            self.eibp_system.remove_particle(index_on_list)
            self.ui.particle_list.takeItem(index_on_list)

    def clear_list(self):
        while self.ui.particle_list.count() > 0:
            self.eibp_system.remove_particle(0)
            self.ui.particle_list.takeItem(0)

    # for electro-magnetic effect of fields on a particle:
    def add_field(self):
        try:
            x_pos = default_value_0(self.ui.middle_point_x.text())
            y_pos = default_value_0(self.ui.middle_point_y.text())
            z_pos = default_value_0(self.ui.middle_point_z.text())

            x_size = default_value_1(self.ui.size_x.text())
            y_size = default_value_1(self.ui.size_y.text())
            z_size = default_value_1(self.ui.size_z.text())

            x_field_vector = default_value_1(self.ui.field_vector_x.text())
            y_field_vector = default_value_1(self.ui.field_vector_y.text())
            z_field_vector = default_value_1(self.ui.field_vector_z.text())

        except TypeError:
            qtw.QMessageBox.critical(None, 'Fail', "arguments for creating particles must be numbers.")
            return

        position = vector(x_pos, y_pos, z_pos)
        size = vector(x_size, y_size, z_size)
        field_vector = vector(x_field_vector, y_field_vector, z_field_vector)

        field_color = vector(self.ui.red_field_slider.value()/99,
                             self.ui.blue_field_slider.value()/99,
                             self.ui.green_field_slider.value()/99)

        if self.ui.magnetic_field_radio.isChecked():
            field_type = "magnetic"
        else:
            field_type = "electric"

        new_field = box(pos=position, color=field_color, size=size, field_vector=field_vector, opacity=.2, field_type=field_type)
        attach_arrow(new_field, "field_vector", scale=.5, shaftwidth=.05, opacity=.1, color=color.white-field_color)

        self.emeofoap_system.fields.append(new_field)

        particle_name = self.ui.name_input_line.text()
        if particle_name:
            self.ui.particle_list.addItem(self.ui.name_input_line.text())
        else:
            particle_index = self.ui.particle_list.count()
            self.ui.particle_list.addItem(f"particle {particle_index}")

    # event handling:
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
