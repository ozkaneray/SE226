import math


def circle_area(radius):
    if radius <= 0:
        raise ValueError(f"Radius must be a positive number. Got: {radius}")
    return math.pi * radius ** 2


def circle_perimeter(radius):
    if radius <= 0:
        raise ValueError(f"Radius must be a positive number. Got: {radius}")
    return 2 * math.pi * radius


def rectangle_area(width, height):
    if width <= 0 or height <= 0:
        raise ValueError(
            f"Width and height must be positive numbers. Got: width={width}, height={height}"
        )
    return width * height


def rectangle_perimeter(width, height):
    if width <= 0 or height <= 0:
        raise ValueError(
            f"Width and height must be positive numbers. Got: width={width}, height={height}"
        )
    return 2 * (width + height)


def triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError(
            f"Base and height must be positive numbers. Got: base={base}, height={height}"
        )
    return 0.5 * base * height