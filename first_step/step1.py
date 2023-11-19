class Circle:
    """
    Circle (Aylana) bor uning radiusi berilgan uning yuzini anoqlovchi class
    """

    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        import math
        area = math.pi * self.radius ** 2
        return area


# inheritance
class Sphere(Circle):
    def calculate_area(self) -> float:
        # Kam ishlatiladigan yechim
        # area = 4 * Circle(self.radius).calculate_area()
        # alternativ taklif etiladigan yechim
        area = 4 * super().calculate_area()
        return area


if __name__ == "__main__":
    circle = Circle(10)
    circle_area = circle.calculate_area()
    print(f'Aylana yuzi: {circle_area:,.2f} ga teng')

    sphere = Sphere(10)
    sphere_area = sphere.calculate_area()
    print(f'Sfera yuzi: {sphere_area:,.2f} ga teng')
