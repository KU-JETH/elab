class ClassRoom:
  def __init__(self):
    self.grade = 0
    self.homeRoomTeacher = ""
    self.studentList = []
    self.numStudents = 0
    
  def get_student_no(self, n: int):
    return self.studentList[n - 1]

  def add_student(self, student_name: str):
    if len(self.studentList) >= 10:
      return False
    
    self.studentList.append(student_name)
    self.numStudents += 1
    return True

  def remove_student(self, student_name):
    if student_name not in self.studentList:
      return False

    student_idx = self.studentList.index(student_name)
    self.studentList.pop(student_idx)
    self.numStudents -= 1
    return True
  
  def change_student(self, n, new_name):
    if n <= 0 or n > len(self.studentList):
      return False
    
    self.studentList[n-1] = new_name
    return True
  
  def remove_student_no(self, n):
    if n <= 0 or n > len(self.studentList):
      return False
  
    self.studentList.pop(n - 1)
    self.numStudents -= 1
    return True
  
  def __str__(self):
    students = ', '.join(self.studentList)
    return f"Grade: {self.grade}\nHomeroom Teacher: {self.homeRoomTeacher}\nStudents: {students}"
  
  # Setter & Getter
  def set_grade(self, grade):
    self.grade = grade
  
  def get_grade(self):
    return self.grade
  
  def set_homeroom_teacher(self, name):
    self.homeRoomTeacher = name
  
  def get_homeroom_teacher(self):
    return self.homeRoomTeacher

  def set_student_list(self, ls):
    self.studentList = ls
  
  def get_student_list(self):
    return self.studentList
  
  def set_num_student(self, n):
    self.numStudents = n
  
  def get_num_student(self):
    return self.numStudents