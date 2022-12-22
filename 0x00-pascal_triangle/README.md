# Pascal's Triangle

This repository contains a function pascal_triangle(n) that returns a list of lists of integers representing the Pascal's triangle of n.

## Requirements

    Python 3.x

## Getting Started

    Clone or download this repository to your local machine.
    Open a terminal or command prompt and navigate to the directory containing the function file.
    Import the function using from pascal_triangle import pascal_triangle.
    Call the function with a positive integer n as an argument to generate the Pascal's triangle of n.

## Function Signature

def pascal_triangle(n: int) -> List[List[int]]:

## Example

>>> from pascal_triangle import pascal_triangle
>>> pascal_triangle(5)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

## Notes

    The function returns an empty list if n is less than or equal to 0.
    You can assume n will always be an integer.