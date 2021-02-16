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

class_name = {"BaseModel": BaseModel}

class HBNBCommand(cmd.Cmd):
    """
    Commnad interpreter class definition
    """
    #Remember to delet this line before the last commit
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
        args = line.split()

        if len(line) < 1:
            print("** class name missing **")
        elif args[0] in class_name:
            obj = class_name[args[0]]()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id
        """
        args = line.split()
        data = storage.all()
        # if passing only 1 argument
        if len(line) < 1:
            print("** class name missing **")
        elif args[0] in class_name:
            if len(args) == 2:
                key = args[0] + "." + args[1]
                if key in data:
                    print(data[key])
                else:
                    print("** no instance found **")
            elif len(args) == 1:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        args = line.split()
        data = storage.all()
        # if passing only 1 argument
        if len(line) < 1:
            print("** class name missing **")
        elif args[0] in class_name:
            if len(args) == 2:
                key = args[0] + "." + args[1]
                if key in data:
                    del(data[key])
                    storage.save()
                else:
                    print("** no instance found **")
            elif len(args) == 1:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name
        """
        args = line.split()
        data = storage.all()
        new_list = []

        if len(line) < 1:
            for key, value in data.items():
                new_list.append(str(value))
            print(new_list)
        elif args[0] in class_name:
            for key, value in data.items():
                key_split = key.split(".")
                if key_split[0] == args[0]:
                    new_list.append(str(value))
            print(new_list)
        else:
            print("** class doesn't exist **")
            


if __name__ == "__main__":
    """
    To execute program like a main
    """
    HBNBCommand().cmdloop()
