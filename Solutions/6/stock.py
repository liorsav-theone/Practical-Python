# stock.py
# stock.py
from pydantic import BaseModel, Field

class Stock(BaseModel):
    """
    Represents a stock holding with a name, number of shares, and price per share.
    """
    name:   str   = Field(description="Stock symbol")
    shares: int   = Field(description="Number of shares")
    price:  float = Field(description="Price per share")

    # Enforce that every assignment is valid
    class Config:
        validate_assignment = True

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
