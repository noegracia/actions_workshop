"""
main.py

This module contains a function to increment a number and prints the result when run directly.
"""

def increment(num):
    """Increments the given number by 1."""
    return num + 1

if __name__ == "__main__":
    INITIAL_NUMBER = 0
    INCREMENTED_NUMBER = increment(INITIAL_NUMBER)
    print(f"The incremented number is: {INCREMENTED_NUMBER}")
