def get_cats_info(path):
    try:
        with open(path, mode='r', encoding='UTF-8') as fh:
            lines = [el.strip() for el in fh.readlines()]

            cats_list = []
            
            for line in lines:
                cat_id, cat_name, cat_age = line.split(',')
                
                cats_list.append({'id': cat_id, "name": cat_name, 'age': cat_age})

            return cats_list 
        
    except FileNotFoundError:
        print(f"Oops! File, You trying to reach seems does not exist. Try again...")
    except OSError:
        print(f"Oops! Error occurred trying to open {path}")