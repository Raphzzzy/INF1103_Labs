from math import isfinite


def get_positive_float(prompt: str) -> float:
    """Repeat until the user provides a finite, strictly positive number."""
    while True:
        try:
            value = float(input(prompt))
            if not isfinite(value) or value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, e.g. 12.50")
