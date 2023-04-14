import csv
class Employee:
    def __init__(self):
        self.Name()
        self.Surname()
        self.Position()
        self.Salary()

    def Name(self, name='Name'):
        self.name = name
        return self.name
    def Surname(self, surname='Surname'):
        self.surname = surname
        return self.surname
    def Position(self, position='Position'):
        self.position = position
        return self.position
    def Salary(self, salary=500):
        self.salary = salary
        self.Write_to_CSV()
        return self.salary
    def SalaryIncrease(self, increase):
        self.salary += increase
        self.Write_to_CSV()
        return self.salary
    def SalaryIncreasePercent(self, percent):
        self.salary *= (1+percent/100)
        self.Write_to_CSV()
        return self.salary
    def SalaryComparison(self,obj_employee):
        return f'Difference between salarys of {self.name} and {obj_employee.name} is {self.salary - obj_employee.salary}'
    def Info(self):
        print(self.name, self.surname, self.position, self.salary)
    def Write_to_CSV(self):
        file = open('salary_increase.csv', 'a')
        file.write(f'{self.name} {self.surname} {self.position} {self.salary} \n')
        file.close()


worker_1 = Employee()
worker_2 = Employee()

worker_1.Name('Tomas')
worker_1.Surname('Pelegrim')
worker_1.Position('Manager')
worker_1.Salary(750)
worker_1.SalaryIncrease(250)
worker_1.SalaryIncreasePercent(17)

print(worker_1.SalaryComparison(worker_2))
worker_1.Info()
