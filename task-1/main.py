from pathlib import Path
from processing import total_salary

file_path = Path('task-1/salaries.txt')


try:
    total, average = total_salary(file_path)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
except TypeError:
    print(f"Oops! Someyhing went wrong. Try again...")
