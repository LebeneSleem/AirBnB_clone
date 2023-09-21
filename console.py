#!/usr/bin/python3
"""
HBNBCommand class definition
Entry point of the command interpreter
"""
import cmd
import json
import re
from models.base_model import BaseModel
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter on EOF (Ctrl+D)"""
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel or any other class, save it,
        and print the id."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        model_classes = {
            "BaseModel": BaseModel,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
            "User": User
        }

        if class_name not in model_classes:
            print("** class doesn't exist **")
            return

        try:
            new_instance = model_classes[class_name]()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        model_classes = {
            "BaseModel": BaseModel,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
            "User": User
        }

        if class_name not in model_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_dict = storage.all()
        key = class_name + "." + args[1]
        if key in obj_dict:
            print(obj_dict[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        model_classes = {
            "BaseModel": BaseModel,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
            "User": User
        }

        if class_name not in model_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_dict = storage.all()
        key = class_name + "." + args[1]
        if key in obj_dict:
            del obj_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print string representations of all instances."""
        if not arg:
            print([str(obj) for obj in storage.all().values()])
            return

        args = arg.split()
        class_name = args[0]

        model_classes = {
            "BaseModel": BaseModel,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
            "User": User
        }

        if class_name not in model_classes:
            print("** class doesn't exist **")
            return

        print([str(obj) for obj in storage.all().values()
              if isinstance(obj, model_classes[class_name])])

    def do_update(self, arg):
        """Update an instance's attributes."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        model_classes = {
            "BaseModel": BaseModel,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
            "User": User
        }

        if class_name not in model_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_dict = storage.all()
        key = class_name + "." + args[1]
        if key not in obj_dict:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = obj_dict[key]
        attr_name = args[2]
        attr_value = args[3]

        try:
            attr_value = eval(attr_value)
        except (NameError, SyntaxError):
            pass

        setattr(obj, attr_name, attr_value)
        obj.save()

    def do_class_show(self, arg):
        """Print the string representation of an instance based on class and ID."""
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **")
            return

        class_name = args[0]
        model_classes = {
            "BaseModel": BaseModel,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
            "User": User
        }

        if class_name not in model_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 3:
            print("** instance id missing **")
            return

        obj_id = args[2]
        obj_key = class_name + "." + obj_id

        obj_dict = storage.all()
        if obj_key in obj_dict:
            print(obj_dict[obj_key])
        else:
            print("** no instance found **")

    def do_class_destroy(self, arg):
        """Delete an instance based on class and ID."""
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **")
            return

        class_name = args[0]
        model_classes = {
            "BaseModel": BaseModel,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
            "User": User
        }

        if class_name not in model_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 3:
            print("** instance id missing **")
            return

        obj_id = args[2]
        obj_key = class_name + "." + obj_id

        obj_dict = storage.all()
        if obj_key in obj_dict:
            del obj_dict[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_class_update(self, arg):
        """Update an instance's attributes based on class, ID, attribute name, and value."""
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **")
            return

        class_name = args[0]
        model_classes = {
            "BaseModel": BaseModel,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
            "User": User
        }

        if class_name not in model_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 3:
            print("** instance id missing **")
            return

        obj_id = args[2]
        obj_key = class_name + "." + obj_id

        obj_dict = storage.all()
        if obj_key not in obj_dict:
            print("** no instance found **")
            return

        if len(args) < 4:
            print("** attribute name missing **")
            return

        if len(args) < 5:
            print("** value missing **")
            return

        obj = obj_dict[obj_key]
        attr_name = args[3]
        attr_value = args[4]

        try:
            attr_value = eval(attr_value)
        except (NameError, SyntaxError):
            pass

        setattr(obj, attr_name, attr_value)
        obj.save()

    def do_class_update_dict(self, arg):
        """Update an instance's attributes based on class, ID, and a dictionary representation."""
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **")
            return

        class_name = args[0]
        model_classes = {
            "BaseModel": BaseModel,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
            "User": User
        }

        if class_name not in model_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 3:
            print("** instance id missing **")
            return

        obj_id = args[2]
        obj_key = class_name + "." + obj_id

        obj_dict = storage.all()
        if obj_key not in obj_dict:
            print("** no instance found **")
            return

        if len(args) < 4:
            print("** dictionary missing **")
            return

        # Convert the provided dictionary representation to a dictionary object
        try:
            dict_representation = eval("{" + " ".join(args[4:]) + "}")
        except (NameError, SyntaxError, TypeError):
            print("** invalid dictionary representation **")
            return

        obj = obj_dict[obj_key]

        # Update the instance's attributes using the dictionary
        for key, value in dict_representation.items():
            setattr(obj, key, value)

        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
