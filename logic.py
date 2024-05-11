import math

def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle given its radius.
    
    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return math.pi * radius ** 2

def calculate_square_area(side: float) -> float:
    """Calculate the area of a square given one side.
    
    Args:
        side (float): The length of one side of the square.

    Returns:
        float: The area of the square.
    """
    return side * side

def calculate_rectangle_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle given its length and width.
    
    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width

def calculate_triangle_area(base: float, height: float) -> float:
    """Calculate the area of a triangle given its base and height.
    
    Args:
        base (float): The base of the triangle.
        height (float): The height of the triangle.

    Returns:
        float: The area of the triangle.
    """
    return 0.5 * base * height
