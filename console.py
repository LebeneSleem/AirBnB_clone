#!/usr/bin/python3
"""
HBNBCommandd class definition
Entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


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
        """Create a new instance of BaseModel, save it,
        and print the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
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
        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_dict = storage.all()
        key = args[0] + "." + args[1]
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
        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_dict = storage.all()
        key = args[0] + "." + args[1]
        if key in obj_dict:
            del obj_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print string representations of all instances."""
        obj_dict = storage.all()
        if not arg:
            obj_list = list(obj_dict.values())
        else:
            args = arg.split()
            if args[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
                return
            obj_list = [v for k, v in obj_dict.items()
                        if k.startswith(args[0] + ".")]
        print([str(obj) for obj in obj_list])

    def do_update(self, arg):
        """Update an instance's attributes."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_dict = storage.all()
        key = args[0] + "." + args[1]
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
