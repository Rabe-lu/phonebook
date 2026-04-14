import json


class FileReader:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def open_file(self):
        with open(self.file_name, 'r') as file:
            content = json.load(file)
            return content
