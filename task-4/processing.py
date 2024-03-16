from colorama import Fore

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return f"{Fore.GREEN}Contact added.{Fore.RESET}"
    except ValueError:
        return f"{Fore.RED}Oops! Not enough arguments in command. Try again...{Fore.RESET}"
    
def get_all_contacts(contacts):    
    if(contacts.keys()):
        contacts_list = []
        for contact in contacts:
            contacts_list.append(f"{Fore.GREEN}{contact}: {contacts[contact]}{Fore.RESET}")

        return '\n'.join(contacts_list)
    else:
        return f"{Fore.RED}Oops! There is no contacts.{Fore.RESET}"
    
def get_contact(args, contacts):    
    try:
        name, *_ = args        
        return f"{Fore.GREEN}Phone number for {name} is {contacts[name]}{Fore.RESET}"
    except ValueError:
        return f"{Fore.RED}Oops! Not enough arguments in command. Try again...{Fore.RESET}"
    
def change_contact(args, contacts):   
    try:
        name, phone = args
        contacts[name] = phone
        return f"{Fore.GREEN}Contact changed.{Fore.RESET}"
    except ValueError:
        return f"{Fore.RED}Oops! Not enough arguments in command. Try again...{Fore.RESET}" 
