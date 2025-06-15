# report.py

import argparse
import fileparse
import tableformat
from stock import Stock
from pathlib import Path
from collections import namedtuple
from typing import List, Dict, Any

# Define a namedtuple to represent a stock record
TableRow = namedtuple('TableRow', ['name', 'shares', 'price', 'change'])

def read_portfolio(filename: Path) -> List[Stock]:
    """
    Read a stock portfolio CSV file into a list of Stock.

    Args:
        filename (Path): Path to the CSV file with portfolio data.
    
    Returns:
        Dict[str, Any]: A list of Stock objects with the keys name, shares, and price.
    """
    
    # Read the csv file
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines)

    # Create a stock for each entry in the svc file
    return [Stock(**d) for d in portdicts]

def read_prices(filename: Path) -> Dict[str, float]:
    """
    Read a CSV file of price data into a dictionary mapping names to prices.

    Args:
        filename (Path): Path to the CSV file with price data.

    Returns:
        Dict[str, float]: A dictionary of stock names to their current prices.
    """

    # Read the csv file to a dict
    with filename.open() as lines:
        return dict(fileparse.parse_csv(lines, types=[str,float], has_headers=False))

def make_report(portfolio :List[Stock], prices: Dict[str, float]) -> List[TableRow]:
    '''
    Create a report comparing the portfolio's original prices to current prices.

    Args:
        portfolio (List[Stock]): List of Stock from the portfolio.
        prices (Dict[str, float]): Dictionary mapping stock names to current prices.

    Returns:
        List[TableRow]: A list of report rows summarizing the changes in value.
    '''
    report = []

    # Create the report for each stock in the portfolio
    for stock in portfolio:
        price = prices.get(stock.name, 0.0)
        report.append(TableRow(name=stock.name, shares=stock.shares, price=price, change=price - stock.price))

    # Return the report
    return report 

def print_report(report_data: List[TableRow]) -> None:
    """
    Print a formatted table from a list of TableRow namedtuples.

    Args:
        report_data (List[TableRow]): The data to be printed in table format.
    """

    # Output the header
    print(' '.join([f'{header:>10s}' for header in TableRow._fields]))
    print(f'{"---------- "*len(TableRow._fields)}')
    
    # Print the rows
    for row in report_data:
        print(f'{row.name:>10s} {row.shares:>10d} {row.price:>10.2f} {row.change:>10.2f}')

def print_report(report_data: List[TableRow], formatter: tableformat.TableFormatter) -> None:
    """
    Print a formatted table from a list of TableRow namedtuples.

    Args:
        report_data (List[TableRow]): The data to be printed in table format.
        formatter (TableFormatter): The formatter used to format the table.
    """    

    # Format the headers
    formatter.headings(['Name','Shares','Price','Change'])

    # Format the rows
    for name, shares, price, change in report_data:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def portfolio_report(portfolio_file: Path, price_file: Path, fmt: str) -> None:
    """
    Generate and print a stock performance report from portfolio and price files.

    Args:
        portfolio_file (Path): Path to the CSV file containing portfolio data.
        price_file (Path): Path to the CSV file containing current stock prices.
        fmt (str): The table format.
    """

    # Read data files 
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(price_file)

    # Create the report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main():

    # Declare the argparser
    parser = argparse.ArgumentParser(description="Create a report from a portfolio file and a price file.")
    parser.add_argument("portfolio", type=Path, help="Path to the input portfolio file")
    parser.add_argument("prices",    type=Path, help="Path to the input prices file")
    parser.add_argument("fmt",       type=str, help="The table format", default='txt')
    args = parser.parse_args()

    # Create the report
    portfolio_report(args.portfolio, args.prices, args.fmt)
    
# If you know you know ;)
if __name__ == '__main__':
    main()
