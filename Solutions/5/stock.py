# stock.py

class Stock:
    """
    Represents a stock holding with a name, number of shares, and price per share.
    """

    __slots__ = ('name', '_shares', 'price')

    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name   = name
        self.shares = shares
        self.price  = price

    def __repr__(self) -> str:
        return f"Stock({self.name!r}, {self.shares!r}, {self.price!r})"

    @property
    def shares(self) -> int:
        """Get the number of shares."""
        return self._shares

    @shares.setter
    def shares(self, value: int) -> None:
        """Set the number of shares with type validation."""
        if not isinstance(value, int):
            raise TypeError("Shares must be an integer.")
        self._shares = value

    @property
    def cost(self) -> float:
        """
        Compute the total cost of the holding.

        Returns:
            float: Total cost calculated as shares * price.
        """
        return self.shares * self.price

    def sell(self, nshares: int) -> int:
        """
        Sell a number of shares and return the updated number.

        Args:
            nshares (int): The number of shares to sell.

        Returns:
            int: The new number of shares after selling.
        """
        self.shares -= nshares
        return self.shares
