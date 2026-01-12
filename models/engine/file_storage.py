#!/usr/bin/python3

"""
FileStorage class for serialization/deserialization
"""

import json 
from models.base_model import BaseModel
import os

class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """
    
    #private attributes
    __file_path:"file.json"
    __objects : {}
        
    def all(self):
        """returns all the objects in filestorage and we fetch them from __objects dict
        Returns :
            dict : a dictonary of all objects
        """
        
        return FileStorage.__objects

    def new(self,obj):
        """
        for adding new objects
        Args:
            obj which is the object to be added

        """
        key="{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key]=obj

    def save(self):
        """
        for serializes __objects to the JSON file (path: __file_path)
        """
        new_dict= {}
        # value is the dict
        for key , value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()

        with open(FileStorage.__file_path,"w",encoding='utf-8') as json_file:
            json.dump(new_dict,json_file)

    def reload(self):
         """
        Deserializes the JSON file to __objects
        Only if the JSON file exists, otherwise do nothing
        """
        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                    obj_dict = json.load(f)
                
                from models.base_model import BaseModel
                
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    if class_name == 'BaseModel':
                        FileStorage.__objects[key] = BaseModel(**value)
            except Exception:
                pass
            