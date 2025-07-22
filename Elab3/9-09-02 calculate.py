class MyMath():
    
    def is_even(self, num):
        return num % 2 == 0
    
    def fac(self, num):
        x = 1
        for i in range(1, num+1):
            x *= i
        
        return x
    
    def is_prime(self, num):
        for i in range(2, 102):
            if i != num and num % i == 0:
                return False
        return True
    
    def divide_by(self, num, k):
        return num % k == 0
    
    def ten_to_bi(self, num):
        return bin(num)[2:]
    
    def ten_to_oct(self, num):
        return oct(num)[2:]
    
    def ten_to_sixteen(self, num):
        x = hex(num)[2:]
        x = "".join([e.upper() if e.isalpha() else e for e in x])
        return x
    
    def int_to_roman(self, num):
        roman_map = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }
        
        x = ""
        for sys, val in roman_map.items():
            if num // val:
                count = num // val
                x += sys * count
                num = num % val
        return x            
    
    def cal_pi():
        x = 3
        for i in range(2, 102,2):
            if i % 4 == 0:
                x -= (4 / (i * (i+1) * (i+2) ) )
            else:
                x += (4 / (i * (i+1) * (i+2) ) )
        
        return x
    
    pi = cal_pi()