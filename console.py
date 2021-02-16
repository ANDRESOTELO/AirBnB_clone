#!/usr/bin/python3
"""
Program that contains the entry point of the command interpreter
"""

import sys
import models
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Commnad interpreter class definition
    """
    intro = "Welcome to Airbnb console! Type ? or help to list commands"
    prompt = "(hbnb)"

    def do_quit(self, line):
        """Exit the program writing 'quit'
        """
        return True

    def do_EOF(self, line):
        """Exit the program with Ctrl + D
        """
        return True

    def emptyline(self):
        """Empty line is entered in response to the prompt
        """
        return

    def do_create(self, line):
        """Create a new instance of BaseModel. If instance was created,
the id of the instance will be printed
        """
        if len(line) < 1:
            print("** class name missing **")
        elif line == "BaseModel":
            obj = BaseModel()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """string representation of an instance
        """
        args = line.split()
        data = storage.all()
        # if passing show as argumnen but no more arguments
        if len(line) < 1:
            print("** class name missing **")
        # if passing 2 arguments
        elif len(args) >= 1:
            for key, value in data.items():
                key_split = key.split(".")
                if len(args) == 1:
                    if args[0] == key_split[0]:
                        print("** instance id missing **")
                    else:
                        print("** class doesn't exist **")
                else:
                    if args[0] == key_split[0] and args[1] == key_split[1]:
                        print(value)
                    elif args[0] != key_split[0]:
                        print("** class doesn't exist **")
                    else:
                        print("** no instance found **")

if __name__ == "__main__":
    """
    To execute program like a main
    """
    HBNBCommand().cmdloop()
