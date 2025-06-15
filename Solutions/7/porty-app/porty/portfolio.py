# portfolio.py

from porty.stock import Stock
from typing import List, Any
from pydantic import BaseModel, Field
import porty.fileparse as fileparse

class Portfolio(BaseModel):
    """
    Represents a portfolio containing a collection of stock holdings.

    Attributes:
        stocks (List[Stock]): A list of Stock objects held within the portfolio.
    """

    stocks: List[Stock] = Field(description="A list of stock holdings")

    @property
    def total_cost(self) -> float:
        """
        Calculates the total cost of all stocks within the portfolio.

        Returns:
            float: The sum of the costs of each stock.
        """
        return sum(s.cost for s in self.stocks)

    @classmethod
    def from_csv(cls, lines: Any) -> "Portfolio":
        """
        Creates a Portfolio instance by parsing stock data from CSV lines.

        Args:
            lines (Any): A file-like object or iterable containing CSV formatted data.

        Returns:
            Portfolio: An instance of Portfolio populated with Stock objects.
        """
        stocks = fileparse.parse_csv(lines)
        return cls(stocks=stocks)
