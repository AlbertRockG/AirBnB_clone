#!/usr/bin/python3
"""
Defines the FileStorage class
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    Represents a class FileStorage that serializes
    instances to a JSON file and deserializes JSON
    file to instances.

    Attributes:
        __file_path (str): path to the JSON file.
        __objects (dict): empty but will store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = dict()

    def __init__(self):
        """
        Initialize method for FileStorage class
        """
        pass

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id

        Args:
            obj (Python object): The object to set
        """
        dictionary = obj.to_dict()
        key = '{}.{}'.format(dictionary['__class__'], str(obj.id))
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        dictionary = dict()
        for k, v in FileStorage.__objects.items():
            dictionary[k] = v.to_dict()
        with open(
            FileStorage.__file_path, 'w', encoding='utf-8'
            ) as file:
            json.dump(dictionary, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects 
        (only if the JSON file (__file_path) exits);
        otherwise, do nothing. 
        If the file doesn't, no exception should be raised.
        """
        try:
            with open(
                FileStorage.__file_path, 'r', encoding='utf-8'
                ) as file:
                json_load = json.load(file)
            for k, v in json_load.items():
                FileStorage.__objects[k] = BaseModel(**v)
            except FileNotFoundError:
                pass
