# Необходимо написать проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку(add), сохранять её, читать список
# заметок(list), редактировать заметку (edit), удалять заметку (delete).

import Commands
from Notebook import Notebook

def main_menu():
    while True:
        read_line = input(f"Введите команду ({', '.join(Commands.commands.keys())}) или 'exit' для выхода: ")
        read_line = read_line.lower().strip()
        if read_line == 'exit':
            break
        else:
            if read_line not in Commands.commands:
                print('Неизвестная команда')
            else:
                Commands.commands[read_line]()


Notebook.get_from_file()     
main_menu()