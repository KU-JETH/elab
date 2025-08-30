class Switch:
  def __init__(self, name, status=False):
    self.name = name
    self.status = status
  
  def turn(self):
    self.status = not self.status
  
  def clone(self):
    return Switch(f"{self.name}.copy", self.status)
  
  def __str__(self):
    status = "on" if self.status else "off"
    return f"switch({self.name}) is {status}"
  
class Light:
  def __init__(self, name, switch):
    self.name = name
    self.switch = switch
  
  def turn(self):
    self.switch.turn()
  
  def get_status(self):
    return self.switch.status
  
  def set_switch(self, new_switch):
    self.switch = new_switch
  
  def clone(self):
    switch = self.switch.clone()
    return Light(f"{self.name}.copy", switch)
  
  def __str__(self):
    return f"light({self.name}) with {self.switch}"