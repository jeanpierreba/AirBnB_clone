#!/usr/bin/python3

""" Module for the command interpreter for the console """

import cmd
"""from models.base_model import BaseModel"""


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
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
