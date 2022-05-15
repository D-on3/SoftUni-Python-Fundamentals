class Circle:
    __pi= 3.14
    def __init__(self,diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        calc = Circle.__pi * self.diameter
        return calc

    def calculate_area(self):
        calc = Circle.__pi * ((self.diameter/2)**2)
        return calc
    def calculate_area_of_sector(self,angle):
        self.angle = angle
        calc = (angle/360)*Circle.__pi * ((self.diameter //2) ** 2)
        return calc

circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
