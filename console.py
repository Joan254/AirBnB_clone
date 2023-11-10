#!/usr/bin/python3
"""Defines the HBNB console."""
import cmd
from models.base_model import BaseModel
from models import storage
import re
from shlex import split
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines the HBNB command interpreter.
    Attributes:
        prompt (str): the command prompt.
    """
    prompt = "(hbnb) "
    current_classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line + ENTER"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        arg_list = parse(arg)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.current_classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_list[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        """
        arg_list = parse(arg)
        obj_dict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.current_classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg_list[0], arg_list[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        and saves the change into the JSON file
        """
        arg_list = parse(arg)
        obj_dict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.current_classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            storage.save

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name
        """
        arg_list = parse(arg)
        if (len(arg_list) > 0 and arg_list[0]
                not in HBNBCommand.current_classes):
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if len(arg_list) > 0 and arg_list[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(arg_list) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute and saves the change
        into the JSON file
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        arg_list = parse(arg)
        obj_dict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        if arg_list[0] not in HBNBCommand.current_classes:
            print("** class doesn't exist **")
            return False
        if len(arg_list) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_list) == 3:
            try:
                type(eval(arg_list[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(arg_list) == 4:
            obj = obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            if arg_list[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg_list[2]])
                obj.__dict__[arg_list[2]] = valtype(arg_list[3])
            else:
                obj.__dict__[arg_list[2]] = arg_list[3]
        elif type(eval(arg_list[2])) == dict:
            obj = obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            for k, v in eval(arg_list[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype[v]
                else:
                    obj.__dict__[k] = v
        storage.save()

    def do_count(self, arg):
        """Retrieves the number of instances of a class"""
        arg_list = parse(arg)
        count = 0
        for obj in storage.all().values():
            if arg_list[0] == obj.__class__.__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
