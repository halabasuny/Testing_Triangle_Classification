"""
Triangle classification module.

This module provides functionality to classify triangles based on their side lengths.
"""
from __future__ import annotations
from typing import Union
import math

Number = Union[int, float]

def _is_number(x) -> bool:
    """
    Check if a value is a valid number (int or float, excluding bool).

    Args:
        x: The value to check.

    Returns:
        True if x is an int or float (but not a bool), False otherwise.
    """
    # bool is a subclass of int; treat True/False as invalid side lengths
    return isinstance(x, (int, float)) and not isinstance(x, bool)

def classify_triangle(a: Number, b: Number, c: Number) -> str:
    """
    Classify a triangle based on its side lengths.

    Classifies triangles as NotATriangle (invalid), Equilateral, Isosceles, Scalene,
    and optionally appends "Right" if it's a right triangle.

    Args:
        a: First side length.
        b: Second side length.
        c: Third side length.

    Returns:
        A string describing the triangle type: "NotATriangle", "Equilateral",
        "Isosceles", "Scalene", "Equilateral Right", "Isosceles Right",
        or "Scalene Right".
    """
    # Validate inputs
    if not (_is_number(a) and _is_number(b) and _is_number(c)):
        return "NotATriangle"
    if a <= 0 or b <= 0 or c <= 0:
        return "NotATriangle"

    # Triangle inequality (use sorted for simplicity)
    x, y, z = sorted([float(a), float(b), float(c)])
    if x + y <= z:
        return "NotATriangle"

    # Side-based classification
    if math.isclose(x, y) and math.isclose(y, z):
        tri_type = "Equilateral"
    elif math.isclose(x, y) or math.isclose(y, z) or math.isclose(x, z):
        tri_type = "Isosceles"
    else:
        tri_type = "Scalene"

    tol = 1e-9
    is_right = abs((x * x + y * y) - (z * z)) <= tol * max(1.0, z * z)

    if is_right:
        # Equilateral cannot be right; but if floats are weird, still append for consistency
        return f"{tri_type} Right"
    return tri_type
