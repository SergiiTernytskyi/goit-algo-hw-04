def total_salary(path):
    try:
        with open(path, mode='r', encoding='UTF-8') as fh:
            lines = [el.strip() for el in fh.readlines()]

            total = 0
            for line in lines:
                _, salary = line.split(',')                
                total += float(salary)
            
            average = total / len(lines)
            return([total, average])    
    except FileNotFoundError:
        print(f"Oops! File, You trying to reach seems does not exist. Try again...")
    except OSError:
        print(f"Oops! Error occurred trying to open {path}")