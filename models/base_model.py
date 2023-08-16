#!/usr/bin/python3
"""
Defines the BaseModel class
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Represents the BaseModel class
    with all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialisation method of BaseModel class.

        Attributes:
            args (list): imputted list of arguments.
            kwargs (dict): inputted arguments as a dict.
            id (str): unique identifier assigned with uuid to each instance.
            created_at (time): datetime - assigns the current datetime.
            updated_at (time): datetime - assgns with the current datetime.
                modified at each update.
        """
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    self.__dict__[k] = datetime.strptime(
                        v, "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif k == 'id':
                    self.id = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Prints [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """
        Updates the public instance attribute update_at
        with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
