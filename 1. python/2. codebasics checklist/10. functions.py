def calculate_area_triangle(base, height):
    area = 1/2 * (base*height)
    return area

def calculate_area(base, height, shape="triangle"):
    match shape:
        case "triangle":
            area = 1/2 * (base*height)
        case "rectangle":
            area = base * height
    return area

print(calculate_area(2,3, "rectangle"))
print(calculate_area_triangle(2,3))
print(calculate_area(2,3,"triangle"))
print(calculate_area(2,3))

def print_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end='')
        print()

print(print_pattern(3))