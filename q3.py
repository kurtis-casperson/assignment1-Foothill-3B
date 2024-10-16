# Foothill College									
# CS 03B - Object Oriented Programming Methodologies in Python
# Question 3           
# Prepared by Viet Trinh 							
# Email: trinhviet@fhda.edu


class Employee:
    def __init__(self, name, employee_number):
        """Constructor to initialize the employee's name and number."""
        self.name = name
        self.employee_number = employee_number

    # Accessor methods
    def get_name(self):
        return self.name

    def get_employee_number(self):
        return self.employee_number

    def __str__(self):
        return f"Employee Name: {self.name}, Employee Number: {self.employee_number}"


employee1 = Employee("Clint Eastwood", 12345)
print(employee1)


employee2 = Employee("Tom Brady", 67890)
print(employee2)



class ProductionWorker(Employee):
    def __init__(self,name, employee_number, pay_rate, shift_number=0 ):
        super().__init__(name, employee_number)
        self.pay_rate = pay_rate
        self.shift_number = shift_number
        self.day_shift = 1
        self.night_shift = 2

    def set_pay_rate(self, pay_rate):
        if pay_rate >= 0: 
            self.pay_rate = pay_rate
        else:
            raise ValueError("Pay rate must be a non-negative value.")


    def get_pay_rate(self):
        return self.pay_rate
    
    


def run():
  print("===== Question 3 =====")

  name = input("Enter employee's name: ")
  employee_number = int(input("Enter employee number: "))

  shift_number = int(input("Enter shift number (1 for Day, 2 for Night): "))
  pay_rate = float(input("Enter hourly pay rate: $"))

    # Create ProductionWorker object
  employee_production = ProductionWorker(name, employee_number, shift_number, pay_rate)

  print(employee_production)



run()
  