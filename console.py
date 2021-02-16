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
        """Prints all string representation instances
if you type "all" without arguments print all instances
if you type "all" + class name, print all instances of the class
        """
        args = line.split()
        data = storage.all()
        list_instances = []

        if len(line) < 1:
            for key, value in data.items():
                list_instances.append(str(value))
            print(list_instances)

        elif args[0] in class_name:
            for key, value in data.items():
                key_split = key.split(".")
                if key_split[0] == args[0]:
                    list_instances.append(str(value))
            print(list_instances)
        else:
            print("** class doesn't exist **")
            
    def do_update(self, line):
        """Update an instance based on the class name and id by adding
or updating attribute
        """
        args = line.split()
        data = storage.all()

        if len(line) < 1:
            print("** class name missing **")
        elif args[0] in class_name:
            if len(args) == 2:
                key = args[0] + "." + args[1]
                if key in data:
                    print("** attribute name missing **")
                else:
                    print("** no instance found **")
            elif len(args) == 3:
                key = args[0] + "." + args[1]
                if key in data:
                    print("** value missing **")
                else:
                    print("** no instance found **")
            elif len(args) == 4:
                key = args[0] + "." + args[1]
                if key in data:
                    for key, value in data.items():
                        a = value.to_dict()
                        a[args[2]] = args[3]
                        storage.save()
                else:
                    print("** instance id missing **")
        else:
            print("** class doesn't exist **")
            

if __name__ == "__main__":
    """
    To execute program like a main
    """
    HBNBCommand().cmdloop()
