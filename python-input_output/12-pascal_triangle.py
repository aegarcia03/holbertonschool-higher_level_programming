#!/usr/bin/python3
"""Defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """Returns a list of lists of integers
    Args:
        n: The number of rows"""
    #Edge case: 
    if n <= 0:
        return []
    # Initialize Pascal's triangle with the first row
    triangle = [[1]]
    # Generate the rows from 1 to n - 1
    for i in range(1, n):
        # Start each row with 1
        row = [1]
        # Get the value of previos row 
        prev_row = triangle[i - 1]
        # Append innerr elements (sum of two elements above)
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        # End each row with 1 
        row.append(1)
        # Append the new row to the triangle 
        triangle.append(row)

    return triangle
