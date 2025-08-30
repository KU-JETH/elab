class Radio():
  def __init__(self):
    self.mode = "FM"
    self.frequency = 87.5
  
  def get_mode(self):
    return self.mode
  
  def get_frequency(self):
    return self.frequency
  
  def set_mode(self, mode):
    self.mode = mode
    
    if mode == "FM":
      self.frequency = 87.5
    else:
      self.frequency = 150
  
  def set_frequency(self, frequency):
    if self.mode == "AM":
      if 280 >= frequency >= 150:
        self.frequency = frequency
    else:
      if 108 >= frequency >= 87.5:
        self.frequency = frequency
  
  def adjust_frequency(self, frequency):
    if self.mode == "FM":
      if 108 >= self.frequency + frequency >= 87.5:
        self.frequency += frequency
        return True
      return False
    else:
      if 280 >= self.frequency + frequency >= 150:
        self.frequency += frequency
        return True
      return False
    
  def __str__(self):
    output = f"{self.mode} Radio: {self.frequency:.1f} "
    if self.mode == "FM":
      output += "MHz"
    else:
      output += "kHz"
    
    return output