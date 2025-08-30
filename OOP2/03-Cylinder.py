import math

class Cylinder:
  def __init__(self, radius, height):
    self.radius = radius
    self.height = height
      
  def get_radius(self):
    return self.radius

  def get_height(self):
    return self.height
  
  def set_radius(self, r):
    self.radius = r

  def set_height(self, h):
    self.height = h

  def get_base_area(self):
    return self.radius ** 2 * math.pi

  def get_volume(self):
    return self.get_base_area() * self.height
      
  def __str__(self):
    return f"Radius: {self.radius:.3f}, Height: {self.height:.3f}"
