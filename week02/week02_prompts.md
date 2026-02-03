# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

**My Prompt:**

You are a senior Python developer. I have a function `sum_of_evens(numbers)`
that is supposed to sum all even numbers in a list, but it adds odd numbers instead.
Please identify the bug and provide a corrected version in Python code.

**AI's Corrected Code:**
```python
def sum_of_evens(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

## Problem 2: Refactoring

**My Prompt:**

You are a senior Python developer. Please refactor the following function to be
more Pythonic and readable while keeping the same behavior.

**AI's Refactored Code:**
```python
def get_names_of_adults(users):
    return [user['name'] for user in users if user['age'] >= 18]

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters
    ----------
    length : float
        Length of the rectangle. Must be positive.
    width : float
        Width of the rectangle. Must be positive.

    Returns
    -------
    float
        The area of the rectangle.

    Raises
    ------
    ValueError
        If length or width is not positive.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
