# timethis.py

import time
from typing import Callable, Any

def timethis(func: Callable) -> Callable:
    """
    Decorator that reports the execution time of the decorated function.

    Args:
        func (Callable): The function to time.

    Returns:
        Callable: A wrapped function that prints execution time after running.
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            end = time.time()
            print(f"{func.__module__}.{func.__name__} : {end - start:.6f} seconds")
    return wrapper

if __name__ == '__main__':
    @timethis
    def countdown(n: int) -> None:
        """Countdown from n to 0."""
        while n > 0:
            n -= 1

    countdown(1_000_000)
