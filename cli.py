import csv

import click
import matplotlib.pyplot as plt
import pyvisa
from pythondaq.arduino_device import ArduinoVISADevice
from pythondaq.diode_experiment import DiodeExperiment


@click.group()
def cmd_group():
    """A group of commands."""
    pass


@cmd_group.command()
def list():
    """Gets a list of all working ports of the Arduino. Returns nothing."""
    rm = pyvisa.ResourceManager("@py")
    print(rm.list_resources())
    return


@cmd_group.command()
@click.option(
    "-b",
    "--startvalue",
    default=0,
    help="First value of the range of voltages you want to set for the LED",
    show_default=True,
)
@click.option(
    "-e",
    "--stopvalue",
    default=3.3,
    help="Last value of the range of voltages you want to set for the LED.",
    show_default=True,
)
@click.option(
    "-r",
    "--repititions",
    default=2,
    help="Number of repititions. Warning: increasing will slow down the measurement.",
    show_default=True,
)
@click.option("-o", "--output", help="Option to get a csv-document of the results.")
@click.option("-p", "--port", help="Name of the port you want to use.")
@click.option(
    "-g",
    "--graph",
    help="Makes a graph of the measured voltages and currents. Type --graph true or -g true to make a plot",
)
@click.option(
    "-n",
    "--no_graph",
    help="Makes no graph of the measured voltages and currents. Type --no_graph anything or -n anything to not make a plot anytime",
)
def scan(startvalue, stopvalue, output, repititions, port, graph, no_graph):
    """Performs the measurments. Put in the minimal and maximal values of the voltages you want the LED to burn at.
    You can also give the number of repitions for the measurement, decreasing the errors with more repititions. There is an option to save your data as a csv file.
    Enter the port you want to use. You will get an error when there is no given port. Function prints the lists of the measured voltages and currents.
    """
    # calculating the ADC values
    start = int(startvalue / 3.3 * 1024)
    stop = int(stopvalue / 3.3 * 1024)

    # gives an error when there is no value for port
    if port == None:
        print("Please submit the port you want to use!")

    # when there is a value for port, the measement is done
    else:
        diode = DiodeExperiment(port)
        (
            list_voltages,
            list_currents,
            list_error_voltages,
            list_error_currents,
        ) = diode.scan(start, stop, repititions)
        print(list_voltages, list_currents)

    # if the option output is used, the user saves the data as a csv-file
    if output != None:
        with open(f"{output}.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["U", "I"])
            for a, b in zip(list_voltages, list_currents):
                writer.writerow([a, b])

    # if the option graph is used, the user gets a graph. if the users uses the option no_graph and types anything next to -n or -no_graph, no graph will be made
    if graph == "true" and no_graph == None:
        plt.errorbar(
            list_voltages,
            list_currents,
            xerr=list_error_voltages,
            yerr=list_error_currents,
            fmt="o",
            markersize="1",
        )
        plt.title("Meting Arduino")
        plt.xlabel("Voltage(V)")
        plt.ylabel("Currents(A)")
        plt.show()
    else:
        print("No graph was made")
    return


@cmd_group.command()
@click.option(
    "-p", "--port", default="ASRL4::INSTR", help="Name of the port you want to use. "
)
def info(port):
    """If no port is given, see default for the name of the port. Prints the identity of the device."""
    diode = DiodeExperiment(port)
    print(
        f"The used port is {port}. The identity of the device is {diode.information()}"
    )
    return


def main():
    cmd_group()


if __name__ == "__main__":
    main()
