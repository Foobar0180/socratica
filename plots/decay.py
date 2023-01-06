"""Radioactive decay program

Program to calculate and plot the radioactive decay of specified
isotopes over a given amount of time.
"""

# Import all the modules that we need to run the program
import math as mth
import numpy as np
import matplotlib.pyplot as plt


def calc_exp(t, half_life):
    """Calculates the exponential part of the decay equation"""
    return np.exp(-mth.log(2) * (t / half_life))


# Used to store the results in a list
results = []

# Define the array of independent variable values for the x-axis
# of the plot, t in seconds
x = np.linspace(0, 10, 20, endpoint=True)

# We should repeat the instructions until the user chooses to
# halt the program

# Set a flag to store whether the programs keeps running
run = True

while run:
    # Prompt the user to input the name of a particular isotope, its
    # half-life in seconds, an initial amount (in grams) and an
    # elapsed time (in seconds)

    # I have chosen not to handle any
    # value errors here, as it was not explicitly mentioned in the
    # program requirements
    isotope = str(input("\nEnter the name of an isotope: "))
    half_life = float(input("\nEnter the half-life of the isotope: "))
    weight = int(input("\nEnter an initial amount (in grams): "))
    elapsed_time = int(input("\nEnter the elapsed time (in seconds): "))

    # Calculate the amount of the isotope remaining after the specified
    # elapsed time
    amount_remaining = weight * calc_exp(elapsed_time, half_life)

    # Store the results
    results.append("\nThe isotope {} will have {} grams remaining after {} seconds".format(
        isotope, amount_remaining, elapsed_time))

    # Calculate the initial mass of the isotope (in grams)
    # necessary to ensure that, after half a minute, 5 grams of it
    # remain
    initial_mass = 5 / calc_exp(30, half_life)

    # Store the results
    results.append("To have 5 grams of isotope {} after 30 seconds, you need an initial amount of {}".format(
        isotope, initial_mass))

    # For the y-axis of the plot we need the amounts remaining
    # after an undefined number of seconds
    y = weight * calc_exp(x, half_life)

    # Plot the amount of the isotope remaining as a function of time,
    # from elapsed time t = 0 seconds until t = 10 seconds
    plt.plot(x, y)

    # Ask the user if the they want to halt the program
    halt = str(input("\nDo you want to add another isotope (y/n): "))
    run = halt == "y"

# When the user wishes to enter no more isotopes, we display the
# decay plots for all of the isotopes that were entered, in a single
# plot, and print out a list of all the isotopes that were added
if results:
    # Show the plot with the results
    plt.title("Amount of radioactive isotope remaining over time")
    plt.show()

    # Print the results of our program
    for result in results:
        print(result)
else:
    print("\nNo isotopes were entered")
