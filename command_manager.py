import menu
import command_dictionary as cd
import command_interpreter as ci

def run_menu():
    print("Welcome to Farmerama Clicker!\n Choose from one of the following options:")
    index = menu.get_menu_choice(cd.tree)
    if index[0] == 1:
        ci.CommandInterpreter([(cd.command_dictionary.get(index[1]), *index[2:])]).run()
    print(f"You selected option {index}:")