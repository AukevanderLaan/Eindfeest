import pyvisa


# defining class to communicate with the arduino
class ArduinoVISADevice:
    """Class for communication with the Arduino device. Contains various method, all having other functions."""

    def __init__(self, port):
        """Sets up communication with the Arduino device.

        Args:
            port (string): Name of the port.
        """
        rm = pyvisa.ResourceManager("@py")
        self.device = rm.open_resource(
            port, read_termination="\r\n", write_termination="\n"
        )
        self.previous_value = 0

    # getting identification of device
    def get_identification(self):
        """Summons the names of the working ports and returns them.

        Returns:
            string: Names of working ports.
        """
        identification = self.device.query("*IDN?")
        return identification

    # output to LED
    def set_output_value(self, value):
        """Turns on the LED with the given ADC values. Maximum intensity at ADC = 1024. Does not work outside the range 0-1023.

        Args:
            value (Integer): represents the strength of the burning of the LED.
        """
        if value < 1024 and value >= 0:
            self.device.query(f"OUT:CH0 {value}")
            self.previous_value = value

    # getting previously used value
    def get_output_value(self):
        """Returns previously ADC value given to the LED.

        Returns:
            Integer: last value of ADC given to the LED
        """
        return self.previous_value

    # measuring channel getting ADC-value
    def get_input_value(self, channel):
        """Measures the ADC-value of the chosen channel. Returns this value.

        Args:
            channel (string): Channel of which you want to measure the voltage.

        Returns:
            Integer: ADC-value over the chosen channel
        """
        input_value = self.device.query(f"MEAS:CH{channel}?")
        return input_value

    # measuring channel getting voltage-value
    def get_input_voltage(self, channel):
        """Gets ADC-value form the Arduino. Calculates the the voltage directly out of the measured ADC-value.

        Args:
            channel (integer): channel over which you want to measure the voltage.

        Returns:
            float: calculated value for the voltage over the channel
        """
        input_voltage = float(self.device.query(f"MEAS:CH{channel}?")) * 3.3 / 1024
        return input_voltage

    def close(self):
        self.device.close()


# defining function to get all working ports
def list_devices():
    """Returns a list of all ports working.

    Returns:
        list: list of ports
    """
    rm = pyvisa.ResourceManager("@py")
    return rm.list_resources()
