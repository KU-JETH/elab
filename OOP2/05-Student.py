class Course:
    def __init__(self, title, course_id, credit):
      self.title = title
      self.course_id = course_id
      self.credit = credit

class Student:
  def __init__(self, id, firstname, lastname):
    self.id = id
    self.firstname = firstname.capitalize()
    self.lastname = lastname.capitalize()
    self.course = []
    self.num_course = 0
    self.total_credit = 0
    self.advisor = None
    self.major = None
  
  def add_course(self, course):
    if self.total_credit + course.credit > 25 or course.course_id in self.course:
      return False
    
    self.course.append(course.course_id)
    self.num_course += 1
    self.total_credit += course.credit
    
    return True
  
  def drop_course(self, course):
    if course.course_id not in self.course:
      return False
    
    i = self.course.index(course.course_id)
    self.course.pop(i)
    self.num_course -= 1
    self.total_credit -= course.credit
    
    return True
  
  def set_advisor(self, advisor):
    self.advisor = advisor
        
  def set_major(self, major):
    self.major = major
  
  def __str__(self):
    courses = " ".join(self.course)
    return f"Student ID: {self.id}\nName: {self.firstname} {self.lastname}\nMajor: {self.major}\nAdvisor: {self.advisor}\nCourses: {courses}"