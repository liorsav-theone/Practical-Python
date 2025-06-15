# pcost.py

import porty.report as report
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

    # Read the portfolio
    portfolio = report.read_portfolio(filename)

    # Sum the entire price of all stocks
    return sum([stock.shares * stock.price for stock in portfolio])

def main():

    # Declare the argparser
    parser = argparse.ArgumentParser(description="Calculate the total cost of a portfolio file.")
    parser.add_argument("filename", type=Path, help="Path to the input CSV file")
    args = parser.parse_args()

    # Calculate the cost
    cost = portfolio_cost(args.filename)
    print("Total cost:", cost)

# If you know you Know ;)
if __name__ == '__main__':
    main()
