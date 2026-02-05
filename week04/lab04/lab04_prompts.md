# Lab 04: Data Structures – AI Interaction Log

---

## Problem 1: Finding common items

**My Prompt:**

You are a senior Python developer. I have two very large lists of product IDs
from different suppliers. I need to find which product IDs appear in both lists.
Order does not matter, but performance is important.
What Python data structure should I use and why?

**AI Recommendation & Reasoning:**

The AI recommended using a **set**. Sets allow fast membership testing and
support efficient intersection operations. Converting both lists to sets and
finding their intersection is much faster than looping through lists.

---

## Problem 2: User profile lookup

**My Prompt:**

I have a list of user profiles where each user has a unique username, age,
and email. I frequently need to look up a user by username, and performance
is critical. What Python data structure should I use?

**AI Recommendation & Reasoning:**

The AI recommended using a **dictionary** with usernames as keys. Dictionaries
provide O(1) average-time lookups, which is much faster than searching a list.

---

## Problem 3: Listing even numbers in order

**My Prompt:**

I have a list of integers representing sensor readings. I need to return only
the even numbers while preserving the original order. What data structure
or approach should I use?

**AI Recommendation & Reasoning:**

The AI recommended using a **list** with a list comprehension. Lists preserve
order, and list comprehensions provide a clean and readable solution.
