import os
import pickle as pkl


class FileWriter:

    def __init__(self, path):
        if self._check_path(path):
            self._path = path
            print(path)
            self.file_is_exists = os.path.exists(self._path)
        else:
            raise Exception('Указанного файла нет')

    def __enter__(self):
        if self.file_is_exists:
            option = 'a'
        else:
            option = 'w'
            self.file_is_exists = True
        self.file = open(self.path, option)
        return self.file


    def __exit__(self, *args):
        self.file.close()
        self.file=None
	
    
    @property
    def path(self):
        return self._path


    @path.setter
    def path(self, other_path):
        if self._check_path(other_path):
            self._path = other_path
            self.file_is_exists = os.path.exists(self._path)
        else:
            raise Exception('Указанная директория не существует')



    def _check_path(self, path):
        return os.path.isdir('/'.join(path.split('/')[:-1]))

    def print_file(self):
        if self.file_is_exists:
            with open(self.path) as f:
                print(f.read())

    def write(self, some_string):
        with open(self._path, 'a' if self.file_is_exists else 'w') as f:
            f.write(some_string + '\n')
            self.file_is_exists = True

    def save_yourself(self, file_name):
        with open(file_name, 'wb') as f:
            pkl.dump(self, f, 2)

    @classmethod
    def load_file_writer(cls, pickle_file):
        with open(pickle_file, 'rb') as f:
            obj=pkl.load(f)
        return obj
