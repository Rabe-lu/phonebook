import json


class FileWriter:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def save_file(self, content):
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(content, file, indent=4, ensure_ascii=False)
            