import datetime
import re

from File_utils import file_write, file_read

date_formats = {
    "%Y-%m-%d": r"^\d{4}-\d{2}-\d{2}$",
    "%y-%m-%d": r"^\d{2}-\d{2}-\d{2}$",
    "%d/%m/%Y": r"^\d{2}/\d{2}/\d{4}$",
}
DATEFORMAT = "%Y-%m-%d"
DATETIMEFORMAT = DATEFORMAT + " %H:%M:%S"
date_pattern = date_formats.get(DATEFORMAT)  


def is_valid_date(date_string):
    match = re.match(date_pattern, date_string)
    return bool(match)


def set_time(d_format=DATETIMEFORMAT):
    return datetime.datetime.now().strftime(d_format)


class Notebook:
    notes = []  
    _id_counter = 0  

    def __init__(self, head, body, id=None, mod_time=None):
        self.head = head
        self.body = body
        self.id = int(id) if id is not None else Notebook.get_next_id()         
        self.mod_time = mod_time if mod_time is not None else set_time()

    def __str__(self):
        return f"ID: {self.id}\nЗаголовок: {self.head}\nЗаметка: {self.body}\nИзменено: {self.mod_time}"

    def short_list(self): 
        return f"ID: {self.id} Заголовок: {self.head} Изменено: {self.mod_time}"

    def to_string(self, delimiter=';'):  
        values = [str(value) for value in list(vars(self).values())]
        return delimiter.join(values)

    @classmethod  
    def from_string(cls, string, delimiter=';'):
        values = string.split(delimiter)
        try:
            return cls(*values)
        except:
            return None

    @classmethod           
    def get_from_file(cls):
        filedata = file_read()
        for file_str in filedata:
            new_note = cls.from_string(file_str)
            if new_note is not None:       
                cls.notes.append(new_note)
                cls._id_counter = max(cls._id_counter, new_note.id)   

    @staticmethod      
    def put_to_file():
        note_list = Notebook.notes
        filedata = [note.to_string() for note in note_list]
        file_write(filedata)

    @staticmethod                      
    def find_id(find_id):
        for index, note in enumerate(Notebook.notes):
            if note.id == find_id:
                return index
        return None

    @staticmethod                  
    def find_by_date(start_date, end_date):
        result = Notebook.notes
        if start_date:
            result = [note for note in result if note.mod_time.split(" ")[0] >= start_date]
        if end_date:
            result = [note for note in result if note.mod_time.split(" ")[0] <= end_date]
        return result

    @staticmethod                  
    def get_next_id():
        Notebook._id_counter += 1
        return Notebook._id_counter