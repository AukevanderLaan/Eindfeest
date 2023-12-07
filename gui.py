import csv
import sys

import numpy as np
import pyqtgraph as pg
import pyvisa
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from pythondaq.diode_experiment import DiodeExperiment
from pythondaq.ui_simple_app import Ui_MainWindow

# sets colours of the background and the data in the plot.
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")


class UserInterface(QtWidgets.QMainWindow):
    """Class to connect buttons to functions. Sets starting values ans ranges to doublespinboxes and spinboxes.

    Args:
        QtWidgets (class): is needed to use buttons and plotwidget etc.
    """

    def __init__(self):
        """Sets up starting values, ranges and stepsizes for buttons. Also calls all usable ports and fills the combobox with them."""
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # connects buttons to their functions
        self.ui.scan_button.clicked.connect(self.scanner)
        self.ui.save_button.clicked.connect(self.saver)

        # setting values for all boxes
        self.ui.doubleSpinBox_start.setValue(0)
        self.ui.doubleSpinBox_stop.setValue(3.3)
        self.ui.spinBox_repititions.setValue(1)

        # setting ranges for all boxes
        self.ui.doubleSpinBox_start.setRange(0, 3.3)
        self.ui.doubleSpinBox_stop.setRange(0, 3.3)
        self.ui.spinBox_repititions.setRange(0, 999)

        # setting stepsize for all boxes
        self.ui.doubleSpinBox_start.setSingleStep(0.01)
        self.ui.doubleSpinBox_stop.setSingleStep(0.01)
        self.ui.spinBox_repititions.setSingleStep(1)

        # fills up the combobox
        rm = pyvisa.ResourceManager("@py")
        self.ui_list_ports = rm.list_resources()
        for i in range(0, len(self.ui_list_ports)):
            self.ui.select_box.addItem(self.ui_list_ports[i])

        self.show()

    @Slot()
    def scanner(self):
        """When the scan button is clicked, the scan starts, getting start and stop values and number of repetitions. The needed port has to be selected to get a plot.
        The plot will be made and is repetable. The communication will be closed after the scan to be opened when the scan button is press again.
        """
        self.ui.graphicsView.clear()
        # calls for class DiodeExperiment
        self.port = self.ui_list_ports[self.ui.select_box.currentIndex()]
        self.diode = DiodeExperiment(port=self.port)
        start = int(self.ui.doubleSpinBox_start.value() / 3.3 * 1024)
        stop = int(self.ui.doubleSpinBox_stop.value() / 3.3 * 1024)
        N = self.ui.spinBox_repititions.value()

        # condition that start value is
        if start < stop:
            (
                self.ui_list_voltages,
                self.ui_list_currents,
                self.ui_list_error_voltages,
                self.ui_list_error_currents,
            ) = self.diode.scan(start, stop, N)

            self.ui.graphicsView.plot(
                self.ui_list_voltages,
                self.ui_list_currents,
                symbol="o",
                symbolSize=7,
                pen=None,
            )
            self.ui.graphicsView.setLabel("left", "Current(A)")
            self.ui.graphicsView.setLabel("bottom", "Voltage(V)")
            error_bars = pg.ErrorBarItem(
                x=np.array(self.ui_list_voltages),
                y=np.array(self.ui_list_currents),
                width=2 * np.array(self.ui_list_error_voltages),
                height=2 * np.array(self.ui_list_error_currents),
            )
            self.ui.graphicsView.addItem(error_bars)
        else:
            print("Start-value has to be smaller than Stop-value")

        self.diode.close()

    @Slot()
    def saver(self):
        """Saves the measured voltage and current values as a csv-file. When the save button is pressed, the user can choose where it wants to save the file."""
        name, _ = QtWidgets.QFileDialog.getSaveFileName(filter="CSV files (*.csv)")
        with open(f"{name}", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["U", "I", "error U", "error I"])
            for a, b, c, d in zip(
                self.ui_list_voltages,
                self.ui_list_currents,
                self.ui_list_error_voltages,
                self.ui_list_error_currents,
            ):
                writer.writerow([a, b, c, d])


def main():
    """Main function to start the inteface and show it."""
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
