import menu

def run_menu():
    print("Welcome to Farmerama Clicker!\n Choose from one of the following options:")
    options = ['1: Run predefined commands',
               '2: Create new predefined commands',
               '3: Run quick command']
    index = menu.get_menu_choice(options)
    print(f"You selected option {index + 1}: {options[index]}")
    suboptions = ['1: ',
               '2: ',
               '3: ']
    index2 = menu.get_menu_choice(suboptions)