import os

FILENAME = 'notebook.csv'

def file_write(filedata, filename=FILENAME):
    is_exit = False
    while not is_exit:
        try:
            with open(filename, 'w') as file:
                for file_str in filedata:
                    file.write(file_str + "\n")
                print("Данные сохранены успешно")
                is_exit = True
        except IOError as e:
            print(f"Ошибка при записи в файл: {e}")
            print("Попробовать еще раз? д - повтор, н - выход:", end=" ")
            read_line = ""
            while read_line.lower().strip() != 'д' and read_line.lower().strip() != 'н':
                read_line = input()
            if read_line.lower().strip() == 'н':
                break

def file_read(filename=FILENAME):
    is_exit = False
    while not is_exit:
        try:
            with open(filename, 'r') as file:
                filedata = file.readlines()
                filedata = [line.rstrip() for line in filedata]
                print("Загружен файл заметок")
                is_exit = True
                return filedata
        except IOError as e:
            print(f"Ошибка при чтении файла: {e}")
            print("Попробовать еще раз? д - повтор, н - продолжить с пустым блокнотом:", end=" ")
            read_line = ""
            while read_line.lower().strip() != 'д' and read_line.lower().strip() != 'н':
                read_line = input()
            if read_line.lower().strip() == 'н':
                return []