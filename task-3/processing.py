from pathlib import Path
from colorama import Fore

def show_directory(path):
    try:
        directory = Path(path)
        if(directory.exists()):
            print(f"{Fore.YELLOW}[Directory] {directory}{Fore.RESET}")

        for inner_path in directory.iterdir():
            if(inner_path.is_dir()):
                show_directory(inner_path)
            elif(inner_path.is_file):
                print(f"{Fore.BLUE}[File] {inner_path}{Fore.RESET}")            
    except FileNotFoundError:
         print(f"{Fore.RED} [ERROR] Oops! Path, You trying to reach seems does not exist. Try again...{Fore.RESET}")
