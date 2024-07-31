import pandas as pd
from datetime import datetime
data = {
    'Employee ID': [101, 102, 103, 104, 105],
    'Department': ['HR', 'Finance', 'IT', 'HR', 'Finance'],
    'Salary': [60000, 80000, 90000, 75000, 85000],
    'Joining Date': ['2015-01-15', '2017-08-23', '2016-06-30', '2018-04-11', '2015-11-03']
}

employee_data = pd.DataFrame(data)
employee_data['Joining Date'] = pd.to_datetime(employee_data['Joining Date'])
print(employee_data)
highest_salaries = employee_data.groupby('Department')['Salary'].max()
lowest_salaries = employee_data.groupby('Department')['Salary'].min()

print("\nHighest salaries in each department:")
print(highest_salaries)

print("\nLowest salaries in each department:")
print(lowest_salaries)
current_date = pd.to_datetime('today')
employee_data['Tenure'] = (current_date - employee_data['Joining Date']).dt.days / 365.25
average_tenure = employee_data['Tenure'].mean()

print("\nAverage tenure of employees in the company:", average_tenure)
specific_date = pd.to_datetime('2017-01-01')
employees_before_date = employee_data[employee_data['Joining Date'] < specific_date]

print("\nEmployees who joined before January 1, 2017:")
print(employees_before_date)
