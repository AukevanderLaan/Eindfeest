# performing function
def measure():
    """Imports library to use plotfunctions. Imports model to execute measurements. Gets the wanted results and plots them."""
    # import matplotlib to be able to get plots
    import matplotlib.pyplot as plt

    from diode_experiment import DiodeExperiment

    # defining diode to use DiodeExperiment()
    diode = DiodeExperiment()
    list_voltages, list_currents, list_error_voltages, list_error_currents = diode.scan(
        0, 1023, 2
    )

    # function to plot voltages and currents with their errors

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


def main():
    """Just a function to perform a measurements. Performs the function measure when called upon."""
    measure()


if __name__ == "__main__":
    main()
