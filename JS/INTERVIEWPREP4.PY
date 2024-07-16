class Employee:
    def __init__(self, emp_id: int, name: str, age: int, department: str, salary: float):
        pass

class EmployeeManagementSystem:
    def __init__(self):
        pass
    
    def add_employee(self, emp_id: int, name: str, age: int, department: str, salary: float) -> None:
        pass
    
    def remove_employee(self, emp_id: int) -> bool:
        pass
    
    def update_employee(self, emp_id: int, name: str = None, age: int = None, department: str = None, salary: float = None) -> bool:
        pass
    
    def list_employees(self, department: str = None) -> List[Employee]:
        pass
    
    def get_average_salary(self, department: str) -> float:
        pass
