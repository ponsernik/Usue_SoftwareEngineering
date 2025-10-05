from sam4_5_1 import triangle_square


def get_sides():
    side1 = float(input("Размер первой стороны: "))
    side2 = float(input("Размер второй стороны: "))
    side3 = float(input("Размер третьей стороны: "))
    return side1, side2, side3


def start():
    dimensions = get_sides()

    result = triangle_square(dimensions[0], dimensions[1], dimensions[2])

    print(f"Результат: {result:.2f}")


if __name__ == "__main__":
    start()