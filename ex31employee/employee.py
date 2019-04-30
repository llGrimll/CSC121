class Employee:
    '''
    Takes first and last name and creates an email.
    '''
    def __init__(self, first, last, dept):  # constructor method
        self.first = first
        self.last = last
        self.dept = dept
        self.email = first[0] + last + "@warren.edu"

    def fullname(self):
        return f"{self.first}, {self.last}"


class Adjunct(Employee):
    def __init__(self, first, last, dept, rank):
        super().__init__(first, last, dept)
        self.rank = rank
        self.email = first + str(".") + last + "@warren.edu"


ADJ_DEPT = "Academics"
ADJ_SR = "Senior Adjunct"
ADJ_JR = "Adjunct"

emp1 = Employee("Steve", "Smith", "Faculty")
emp2 = Employee("Adrian", "Anderson", "Academics")
emp3 = Adjunct("Brad", "Myers", ADJ_DEPT, ADJ_SR)
emp4 = Adjunct("Seth", "Aaronstein", ADJ_DEPT, ADJ_JR)

print(emp1.email.lower())
print(emp2.email.lower())
print(emp1.fullname())
