#!/usr/bin/python3
import uuid
from datetime import datetime
class BaseModel:
    """
    defines all common attributes/methods for other classes
    """
    def __init__(self,*args,**kwargs):
        """
        class initilization
        """
        if kwargs:
            for key , value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    #we need to convert the datetime back to a datetime from a string
                    setattr(self,key,datetime.fromisoformat(value))
                else:
                    setattr(self,key,value)    
        else:
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
    

