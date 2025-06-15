# report.py

import csv
from pathlib import Path
from collections import namedtuple
from typing import List, Dict, Any

# Define a namedtuple to represent a stock record
TableRow = namedtuple('TableRow', ['name', 'shares', 'price', 'change'])

def read_portfolio(filename: Path) -> List[Dict[str, Any]]:
    """
    Read a stock portfolio CSV file into a list of Stock dictionaries.

    Args:
        filename (Path): Path to the CSV file with portfolio data.
    
    Returns:
        Dict[str, Any]: A list of Stock dictionaries with the keys name, shares, and price.
    """
    portfolio = []

    # Open the file
    with filename.open("rt") as f:

        # Read the csv file
        rows = csv.reader(f)

        # Get the headers
        headers = next(rows)

        # Iterate over all rows
        for row in rows:

            # Create a dict for each row
            record = dict(zip(headers, row))
            stock = {
                 'name'   : record['name'],
                 'shares' : int(record['shares']),
                 'price'   : float(record['price'])
            }

            # Append the rows to the portfolio
            portfolio.append(stock)

    # Return the created list
    return portfolio

def read_prices(filename: Path) -> Dict[str, float]:
    """
    Read a CSV file of price data into a dictionary mapping names to prices.

    Args:
        filename (Path): Path to the CSV file with price data.

    Returns:
        Dict[str, float]: A dictionary of stock names to their current prices.
    """
    prices = {}

    # Open the file
    with filename.open("rt") as f:

        # Read the csv file
        rows = csv.reader(f)

        # Iterate over all rows and get their price
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

def make_report(portfolio :List[Dict[str, Any]], prices: Dict[str, float]) -> List[TableRow]:
    '''
    Create a report comparing the portfolio's original prices to current prices.

    Args:
        portfolio (List[Stock]): List of Stock dictionaries from the portfolio.
        prices (Dict[str, float]): Dictionary mapping stock names to current prices.

    Returns:
        List[TableRow]: A list of report rows summarizing the changes in value.
    '''
    report = []

    # Create the report for each stock in the portfolio
    for item in portfolio:
        price = prices.get(item['name'], 0.0)
        report.append(TableRow(name=item['name'], shares=item['shares'], price=price, change=price - item['price']))

    # Return the report
    return report 

# Read data files and create the report data        
portfolio = read_portfolio(Path('Data/portfolio.csv'))
prices = read_prices(Path('Data/prices.csv'))

# Output the header
print(' '.join([f'{header:>10s}' for header in TableRow._fields]))
print(f'{"---------- "*len(TableRow._fields)}')

# Print the rows
for row in make_report(portfolio, prices):
    print(f'{row.name:>10s} {row.shares:>10d} {row.price:>10.2f} {row.change:>10.2f}')
