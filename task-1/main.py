from pathlib import Path
from processing import total_salary

def main():
    file_path = Path('salaries.txt')
    try:
        total, average = total_salary(file_path)
        print(f"Total salary value: {total}, average salary value: {average}")
    except TypeError:
        print(f"Oops! Someyhing went wrong. Try again...")


if __name__ == "__main__":
    main()