#!/usr/bin/python3

""" Module for the command interpreter for the console """

from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
import cmd

classes = {"BaseModel": BaseModel, "User": User,
           "State": State, "City": City, "Amenity": Amenity,
           "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """ Class HBNB to read commands in the console """

    prompt = '(hbnb) '

    def emptyline(self):
        """ Manage no args """
        pass

    def do_quit(self, arg):
        """ Exit the programm """
        return True

    def do_EOF(self, arg):
        """ Handle EOF signal """
        print()
        return True

    def do_create(self, line):
        """ Create a new instance of a class """
        if not line:
            print("** class name missing **")
            return None
        try:
            new = eval(line + "()")
            new.save()
            print(new.id)
        except:
            print("** class doesn't exist**")

    def do_show(self, line):
        """ Prints the string representation of an
            instance based on the class name and id"""
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                to_show = "{}.{}".format(args[0], args[1])
                if to_show not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[to_show])

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                to_delete = "{}.{}".format(args[0], args[1])
                if to_delete not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[to_delete]
                    storage.save()

    def do_all(self, line):
        """ Printed the  name of class, if exist or not"""
        if line:
            args = line.split()
            if args[0] not in classes:
                print("** class doesn't exist **")
            else:
                to_print = [str(obj) for key, obj in storage.all().items()
                            if type(obj).__name__ == args[0]]
                print(to_print)
        else:
            to_print = [str(obj) for key, obj in storage.all().items()]
            print(to_print)

    def do_update(self, line):
        """ Update <class name> <id> <attribute name> <attribute value> """
        args = line.split()

        if not line:
            print("** class name missing **")
        else:
            if args[0] not in classes:
                print("** class doesn't exist **")
                return
            elif len(args) < 2:
                print("** instance id missing **")
                return
            add_agrs = "{}.{}".format(args[0], args[1])
            if add_agrs not in storage.all():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            elif len(args) >= 4:
                replace_com = args[3].replace('"', '')
                if args[2] == "created_add" or args[2] == "updated_at" \
                        or args[2] == "id":
                    pass
                else:
                    setattr(storage.all()[add_agrs], args[2], replace_com)
                    storage.all()[add_agrs].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
