import Class_Person

class Employee(Class_Person.Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age) # call the constructor of the parent class
        self.emp_id = emp_id # new attribute for the derived class

    def disp_empId(self):
        return f"My Employee ID is {self.emp_id}"