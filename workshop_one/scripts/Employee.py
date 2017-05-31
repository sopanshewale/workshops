class Employee (object):
    def __init__(self, name, salary):
        self._name   = name
        self._salary = salary
   
    def get_salary(self):
        return self._salary
 
    def set_salary(self, salary):
         self._salary = salary
  
    
