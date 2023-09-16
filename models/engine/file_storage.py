#!/usr/bin/python3
# A class FileStorage that serializes instances to a JSON file
# And deserializes JSON file to instances
import json


class FileStorage:
    def __init__(self, models):
        self.__file_path = "file.json"
        self.__objects = {}
        self.models = models

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    cls = models[class_name]
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
