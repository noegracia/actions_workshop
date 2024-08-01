"""
main.py

This module contains a simple function to increment a number and prints the result when run directly.
"""

def increment(num):
    """Increments the given number by 1."""
    return num + 1

if __name__ == "__main__":
    initial_number = 0
    incremented_number = increment(initial_number)
    print(f"The incremented number is: {incremented_number}")
