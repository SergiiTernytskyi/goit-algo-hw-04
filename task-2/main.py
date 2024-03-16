from pathlib import Path
from processing import get_cats_info

file_path = Path('task-2/cats_list.txt')

cats = get_cats_info(file_path)
print(get_cats_info(file_path))

