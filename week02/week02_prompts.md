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
```

**What I Learned:**

The bug was on the condition line - it checked `if num % 2 == 1:` (odd numbers) instead of `if num % 2 == 0:` (even numbers). The AI quickly identified this logical error and provided the corrected version.

---

## Problem 2: Refactoring

**My Prompt:**

You are a senior Python developer. Please refactor the following function to be
more Pythonic and readable while keeping the same behavior. The original code uses
a manual index-based loop which is not idiomatic Python.

Original code:
```python
def get_names_of_adults(users):
    results = []
    for i in range(len(users)):
        if users[i]['age'] >= 18:
            results.append(users[i]['name'])
    return results
```

Please provide a refactored version using Pythonic patterns like list comprehension.

**AI's Refactored Code:**

```python
def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    return [user['name'] for user in users if user['age'] >= 18]
```

**What I Learned:**

List comprehensions are the Pythonic way to transform lists - they're more concise and readable than manual index-based loops with append(). The refactored version is 1 line instead of 4 and directly iterates over users instead of using range(len()).

---

## Problem 3: Documenting

**My Prompt:**

You are a senior Python developer. This function calculates the area of a rectangle
and raises a ValueError for invalid inputs. Please write a professional NumPy-style
docstring for it that documents all parameters, return values, and exceptions.

Code:
```python
def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```

**AI's Documented Code:**

```python
def calculate_area(length, width):
    """Calculate the area of a rectangle.

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

    Examples
    --------
    >>> calculate_area(5, 4)
    20
    >>> calculate_area(0, 5)
    Traceback (most recent call last):
        ...
    ValueError: Length and width must be positive numbers.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```

**What I Learned:**

The NumPy docstring style is very structured - it includes Parameters, Returns, Raises sections, and even Examples showing both normal use and error cases. This is much more complete than basic comments and helps both users and AI tools understand exactly what the function does.
