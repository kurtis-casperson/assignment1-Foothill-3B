
import math 


class Circle:
  

    def __init__(self, x=0, y=0, radius=1):
       x = x
       y = y
       radius = radius
    
    def get_x(self):
       return self.x
    
    def get_y(self):
       return self.y
    
    def get_radius(self):
       return self.radius
    
    def set_x(self, x):
       self.x = x
    
    def set_y(self, y):
       self.y = y

    def set_radius(self, radius):
       self.radius = radius

    def getArea(self, radius):
       area = math.pi * (radius ** 2)
       return area
    
    def getPerimeter(self, radius):
       perimeter = 2 * math.pi * (radius)
       return perimeter
    
    def containPoint(self, x, y):
       distance = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
        # Check if the distance is less than or equal to the radius
       return distance <= self.radius

    def containCircle(self, circle):
       distance_centers = math.sqrt((circle.get_x() - self.x) ** 2 + (circle.get_y() - self.y) ** 2)
        # Check if this circle can completely enclose the other circle
       return distance_centers + circle.getRadius() <= self._radius
    
    def overlaps(circle):
       return

def run():
  print("===== Question 1 =====")
 
  circle = Circle(2,2,2)
  area = circle.getArea(3)
  print(area)

run()