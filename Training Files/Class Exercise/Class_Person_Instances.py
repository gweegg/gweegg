# Creating an instance of the Person Class (Class_Person.py)
import Class_Employee_Inheritance

person1Name = "Josh"
person1Age = 26
person1EmpId = "E0001"

person1 = Class_Employee_Inheritance.Employee(person1Name, person1Age,person1EmpId)
print(person1.greet())
print(person1.disp_empId())