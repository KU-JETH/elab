# ข้อนี้ผมใช้สมการเส้นเเทน
# เเละก็ไม่ได้ใช้ Class Point ที่โจทย์ให้มา ถ้ามีก็บอกให้ผมเเก้ได้นะ

class Line:
  def __init__(self, x1, y1, x2, y2):
    self.start = (x1, y1)
    self.end = (x2, y2)
    
    self.slope = (y2 - y1) / (x2 - x1)
    
    self.c = (y1 + y2) - self.slope * (x1 + x2)
    self.y_intercept = (-self.c / self.slope, 0)
  
  def contains(self, x, y):
    if x in range(self.start[0], self.end[0]) and y in range(self.start[1], self.end[1]):
      return True
      
    return False
  
  def get_distance(self):
    x = self.end[0] - self.start[0]
    y = self.end[1] - self.start[1]
    return (x ** 2 + y ** 2) ** (1/2)
  
  def get_x1(self):
    return self.start[0]
  
  def get_y1(self):
    return self.start[1]
  
  def get_x2(self):
    return self.end[0]
  
  def get_y2(self):
    return self.end[1]
  
  def get_y(self, x):
    y = self.slope * x + self.c
    
    if y in range(self.start[1], self.end[1]):
      return y
    return -999.999