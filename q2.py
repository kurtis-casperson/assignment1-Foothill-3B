# Foothill College									
# CS 03B - Object Oriented Programming Methodologies in Python
# Question 2             
# Prepared by Viet Trinh 							
# Email: trinhviet@fhda.edu


import math

class Triangle:
    def __init__(self, side1=1.0, side2=1.0, side3=1.0):
        """Constructor to create a triangle with specified sides or default values."""
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
   
    def get_side1(self):
        return self.side1

    def get_side2(self):
        return self.side2

    def get_side3(self):
        return self.side3

    
    def getArea(self):
        semi_perimeter = self.getPerimeter() / 2 
        area = math.sqrt(semi_perimeter * (semi_perimeter - self.side1) * (semi_perimeter - self.side2) * (semi_perimeter - self.side3))
        return area

    
    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3

    def toString(self):
        return f"Triangle: side1={self.side1}, side2={self.side2}, side3={self.side3}, Area={self.getArea():.2f}, Perimeter={self.getPerimeter():.2f}"

def run():
    print("===== Question 2 =====")
    default_triangle = Triangle()
    print(f"Default Triangle: side1={default_triangle.side1}, side2={default_triangle.side2}, side3={default_triangle.side3}")


    specified_triangle = Triangle(3.0, 4.0, 5.0)
    print(f"Specified Triangle: side1={specified_triangle.side1}, side2={specified_triangle.side2}, side3={specified_triangle.side3}")

    print(default_triangle.toString())

run()