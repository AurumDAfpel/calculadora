import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("Presione ENTER para continuar...")
    clear_console()

