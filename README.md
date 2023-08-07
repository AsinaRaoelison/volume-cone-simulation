# Volume Cone Simulation

This is a Python program to estimate the volume of a cone using the Law of Large Numbers through Monte Carlo simulations. It generates random points uniformly distributed in a cube containing the cone and calculates the proportion of points falling inside the cone to estimate the volume.

## Prerequisites

- Python 3.x
- Required Python libraries: `random`, `math`, `argparse`

## How to Use

1. Clone the repository to your local machine.
2. Make sure you have Python 3.x installed.
3. Install the required Python libraries by running:
    pip install -r requirements.txt
4. Prepare an input file (e.g., `cone_parameters.txt`) containing the cone parameters:

    5.0 # Radius of the base of the cone
    10.0 # Height of the cone
    100000 # Number of simulations
5. Run the program with the input file as an argument:

    python volume_cone_simulation.py cone_parameters.txt

Optional arguments:
- `-n` or `--nbsimul`: The number of simulations to perform for volume estimation. (Default is 10000)

The program will estimate the volume of the cone using the Law of Large Numbers and display the results in the terminal.

## Input File Format

The input file should contain three lines:
1. The first line: the radius of the base of the cone.
2. The second line: the height of the cone.
3. The third line: the number of simulations to be performed.

## Sample Output

Volume estimé du cône: 262.73140849918414
Volume théorique du cône: 261.79938779914946

