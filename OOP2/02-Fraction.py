# โค้ดนี้ไม่ค่อยดีเท่าไหร่นะ เเก้ผมได้

class Fraction:
  def __init__(self, numerator, denominator):
    self.numerator = numerator
    self.denominator = denominator
    self.valuate()
  
  def evaluate(self):
    return self.numerator / self.denominator
  
  def add(self, n):
    numerator = self.numerator + self.denominator * n
    return Fraction(numerator, self.denominator)
  
  def __add__(self, other):
    numerator = self.numerator * other.denominator + other.numerator * self.denominator
    denominator = self.denominator * other.denominator
    
    return Fraction(numerator, denominator)
  
  def multiply(self, n):
    numerator = self.numerator * n
    return Fraction(numerator, self.denominator)
  
  def __mul__(self, other):
    return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
  
  def __str__(self):
    if self.numerator == 0:
      return f"0 / 1"
    return f"{self.numerator} / {self.denominator}"
  
  # ทำให้เป็นเศษส่วนอย่างต่ำ โดยที่ไม่ใช้ gcd
  def valuate(self):
    for i in range(2, 11):
      while self.numerator % i == 0 and self.denominator % i == 0:
        self.numerator = int(self.numerator / i)
        self.denominator = int(self.denominator / i)