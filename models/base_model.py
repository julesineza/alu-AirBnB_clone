#!/usr/bin/python3
import uuid
from datetime import datetime
class BaseModel:
    """
    defines all common attributes/methods for other classes
    """
    def __init__(self):
        """
        class initilization
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """provide a user friendly output when class is queried"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """
        perfoms dave operation by updataing self.updated_at to the current time 
        """
        self.updated_at=datetime.now()

    def to_dict(self):
        """
        converts the class into a dictonary (value,pair) so it can be usefule for saving in json or sending to api which use json format """
        dictonary = self.__dict__
        new_dict= dictonary.copy()
        new_dict["__class__"] = self.__class__.__name__

        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
print("-----------------------------------------------------\n")
my_model.save()
print(my_model)
print("-----------------------------------------------------\n")

my_model_json = my_model.to_dict()
print(my_model_json)
print("-----------------------------------------------------\n")
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))    
    