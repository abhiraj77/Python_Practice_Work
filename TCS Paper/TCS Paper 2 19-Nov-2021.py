class Employee:
    def __init__(self, emp_name,designation,salary,OTContribution):
        self.emp_name = emp_name
        self.designation = designation
        self.salary = salary
        self.OTContribution = OTContribution # OTContribution = {month:overtime}
        self.OTStatus = False

class Organization:
    def __init__(self, employee_list):
        self.employee_list = employee_list

    def OTEligible(self,OTThreshold):
        for employee in self.employee_list:
            if sum(employee.OTContribution.values()) > OTThreshold:
                employee.OTStatus = True
                print(f"{employee.emp_name} {employee.OTStatus}")
            else:
                print(f"{employee.emp_name} {employee.OTStatus}")
    
    def TotalBonusAmt(self, rate):
        for employee in self.employee_list:
            total = 0
            if employee.OTStatus == True:
                total += rate * sum(employee.OTContribution.values())
        return total

n = int(input())
employee_list = []
for i in range(n):
    emp_name = input()
    designation = input()
    salary = int(input())
    n2 = int(input())
    OTContribution = {}
    for k in range(n2):
        month = input()
        time = int(input())
        OTContribution[month] = time
    employee_list.append(Employee(emp_name, designation, salary, OTContribution))

OTThreshold = int(input())
rate = int(input())
org = Organization(employee_list)
org.OTEligible(OTThreshold)
total = org.TotalBonusAmt(rate)
print(total)