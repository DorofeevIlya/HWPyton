from Notebook import Notebook, set_time, is_valid_date, DATEFORMAT


class Controller: 

    @staticmethod
    def add():
        while True:
            head = input('Введите заголовок заметки: ')
            body = input('Введите текст заметки: ')
            new_note = Notebook(head, body)
            print(f"{new_note.mod_time} создана заметка id: {new_note.id}")
            Notebook.notes.append(new_note)
            read_line = ""
            print("Добавить еще одну заметку? (д/н):", end=" ")
            while read_line.lower().strip() != 'д' and read_line.lower().strip() != 'н':
                read_line = input()
            if read_line.lower().strip() == 'н':
                break
        Notebook.put_to_file()         

    @staticmethod
    def edit():
        readline = ""
        print("Введите id заметки:", end=" ")
        while not readline.isdigit():
            readline = input()
        index_by_id = Notebook.find_id(int(readline))
        if index_by_id == None:
            print(f"Заметка с id{readline} не найдена. Для просмотра заметок воспользуйтесь командой list")
        else:
            find_note = Notebook.notes[index_by_id]
            print("Заголовок заметки: "+find_note.head)
            head = input('Введите новый заголовок заметки: ')
            print("Текст заметки: " + find_note.body)
            body = input('Введите новый текст заметки: ')
            Notebook.notes[index_by_id].head = head
            Notebook.notes[index_by_id].body = body
            Notebook.notes[index_by_id].mod_time = set_time()
            print("Заметка отредактирована")
            Notebook.put_to_file()          

    @staticmethod
    def delete():
        readline = ""
        print("Введите id заметки:", end=" ")
        while not readline.isdigit():
            readline = input()
        index_by_id = Notebook.find_id(int(readline))
        if index_by_id == None:
            print(f"Заметка с id{readline} не найдена. Для просмотра заметок воспользуйтесь командой list")
        else:
            print(Notebook.notes[index_by_id].short_list())
            print("Удалить заметку? (д/н):", end=" ")
            read_line = ""
            while read_line.lower().strip() != 'д' and read_line.lower().strip() != 'н':
                read_line = input()
            if read_line.lower().strip() == 'д':
                del(Notebook.notes[index_by_id])
                print("Заметка удалена")
                Notebook.put_to_file()        

    @staticmethod
    def listing():
        start_date, end_date = "", ""
        is_exit = False
        print(f"Введите начальную дату для поиска заметки в формате {set_time(DATEFORMAT)} (не обязательно):", end=" ")
        while not is_exit:
            readline = input()
            if is_valid_date(readline) or readline.strip() == "":
                start_date = readline
                is_exit = True
        is_exit = False
        print(f"Введите конечную дату для поиска заметки в формате {set_time(DATEFORMAT)} (не обязательно):", end=" ")
        while not is_exit:
            readline = input()
            if is_valid_date(readline) or readline.strip() == "":
                end_date = readline
                is_exit = True
        find_data = Notebook.find_by_date(start_date, end_date)
        if len(find_data)==0:
            print("Заметки не найдены")
        else:
            list(map(lambda note: print(note.short_list()), find_data))


    @staticmethod
    def view():
        readline = ""
        print("Введите id заметки:", end=" ")
        while not readline.isdigit():
            readline = input()
        index_by_id = Notebook.find_id(int(readline))
        if index_by_id == None:
            print(f"Заметка с id{readline} не найдена. Для просмотра заметок воспользуйтесь командой list")
        else:
            print(Notebook.notes[index_by_id])



commands = {'add': Controller.add, 'edit': Controller.edit, 'delete': Controller.delete, 'list': Controller.listing,
            'view': Controller.view}