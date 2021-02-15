#!/usr/bin/python3
"""
Program that contains the entry point of the command interpreter
"""

import sys
import models
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
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

    def __str__(self):
        """Method to override the __str__ method and return
specific text format
        """
        return "{} {}".format(obj.__class__.__name__, obj.id)


if __name__ == "__main__":
    """
    To execute program like a main
    """
    HBNBCommand().cmdloop()
