from lab6 import geometry_utils

operations = {
    "circle_area":lambda: geometry_utils.circle_area(float(input("Enter radius: "))),
    "circle_perimeter":lambda: geometry_utils.circle_perimeter(float(input("Enter radius: "))),
    "rectangle_area":lambda: geometry_utils.rectangle_area(float(input("Enter width: ")), float(input("Enter height: "))),
    "rectangle_perimeter":lambda: geometry_utils.rectangle_perimeter(float(input("Enter width: ")), float(input("Enter height: "))),
    "triangle_area":lambda: geometry_utils.triangle_area(float(input("Enter base: ")), float(input("Enter height: "))),
}

print("Available shapes: circle, rectangle, triangle")
print("Available calculations: _area, _perimeter (e.g., circle_area)")

op = input("Enter the operation you want to perform: ").strip().lower()

if op not in operations:
    print(f"Invalid operation '{op}'. Use format: shape_calculation (e.g., circle_area)")
else:
    try:
        result = operations[op]()
        print(f"Result: {result:.2f}")
    except ValueError:
        print("Input Error: Dimensions must be strictly positive.")
    except Exception:
        print("Input Error: Please enter valid numeric values.")