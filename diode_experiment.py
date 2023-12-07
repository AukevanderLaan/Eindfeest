# importing class ArduinoVISADevice to use it in script
# importing numpy to perform some calculations
import numpy as np
from pythondaq.arduino_device import ArduinoVISADevice, list_devices


# defining new class to perform the calculations
class DiodeExperiment:
    def __init__(self, port):
        """Function that is executed when the class is summoned. Sets up empty lists for a number of voltages, currents and the deviation of those voltages and currents."""
        # instant of class ArduinoVISADevice
        self.device = ArduinoVISADevice(port=port)

        # lists in self to save the wanted information
        self.list_voltages = []
        self.list_currents = []
        self.list_std_voltages = []
        self.list_std_currents = []

    def information(self):
        """Get the identity of the device you are using.

        Returns:
            string: identity of the device
        """
        identity = self.device.get_identification()
        return identity

    # function of performing the measurements
    def scan(self, start_value, stop_value, N):
        """Lets the LED burn using start and stop values. Returns the lists of the voltages and currents over the LED.
        Also returns the errors of the voltages and currents over the LED.

        Args:
            start_value (Integer): Sets start-value of the range of the for-loop.
            stop_value (Integer): Sets stop-value of the range of the for-loop. Maximum intensity of Led at ADC = n * 1024.
            N (Integer): Number of times the measurement is repeated. Set larger for more accuracy. Warning: takes more time to run when this value becomes larges.

        Returns:
            Lists: Returns lists of calculated voltages, currents, errors of voltages and errors of currents.
        """
        for ADC in range(start_value, stop_value + 1):
            # for each point, the temporary lists need to be empty at the start
            temporary_list_voltage = []
            temporary_list_current = []
            # performing N times per point to get a mean value and an error
            for i in range(0, N):
                self.device.set_output_value(ADC)
                spanning_c1 = self.device.get_input_voltage(1)
                spanning_c2 = self.device.get_input_voltage(2)

                spanning_led = spanning_c1 - spanning_c2
                current_led = spanning_c2 / 220

                temporary_list_voltage.append(spanning_led)
                temporary_list_current.append(current_led)

            # adding calculated values to the right lists
            self.list_voltages.append(np.mean(temporary_list_voltage))
            self.list_std_voltages.append(np.std(temporary_list_voltage) / np.sqrt(N))
            self.list_currents.append(np.mean(temporary_list_current))
            self.list_std_currents.append(np.std(temporary_list_current) / np.sqrt(N))
        self.device.set_output_value(0)
        return (
            self.list_voltages,
            self.list_currents,
            self.list_std_voltages,
            self.list_std_currents,
        )

    def close(self):
        self.device.close()
