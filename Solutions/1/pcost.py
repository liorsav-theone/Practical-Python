# pcost.py

import csv
import argparse
from pathlib import Path

def portfolio_cost(filename: Path) -> float:
    """
    Compute the total cost (shares * price) of a portfolio CSV file.

    Args:
        filename (Path): Path to the CSV file containing portfolio data.

    Returns:
        float: The total calculated cost.
    """
    total_cost = 0.0

    # Open the file
    with filename.open("rt") as f:

        # Read the csv file
        rows = csv.reader(f)

        # Get the row headers
        headers = next(rows)

        # Iterate over all rows
        for row in rows:
            try:

                # Calculate the total cost
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price

            # This catches errors in int() and float() conversions above
            except ValueError:
                print('Bad row:', row)

    return total_cost

# Declare the argparser
parser = argparse.ArgumentParser(description="Calculate the total cost of a portfolio file.")
parser.add_argument("filename", type=Path, help="Path to the input CSV file")
args = parser.parse_args()

# Calculate the cost
cost = portfolio_cost(args.filename)
print("Total cost:", cost)
