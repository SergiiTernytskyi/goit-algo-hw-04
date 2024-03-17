from pathlib import Path
from processing import get_cats_info

def main():
    file_path = Path('cats_list.txt')
    cats = get_cats_info(file_path)
    print(cats)


if __name__ == "__main__":
    main()