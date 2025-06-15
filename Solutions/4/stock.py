# stock.py

class Stock:
    """
    Represents a stock holding with a name, number of shares, and price per share.
    """

    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name   = name
        self.shares = shares
        self.price  = price

    def __repr__(self) -> str:
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

    def cost(self) -> float:
        """
        Calculate the total cost of the holding.

        Returns:
            float: Total cost computed as shares * price.
        """
        return self.shares * self.price

    def sell(self, num_shares: int) -> None:
        """
        Sell a number of shares from the holding.

        Args:
            num_shares (int): The number of shares to sell.
        """
        self.shares -= num_shares
