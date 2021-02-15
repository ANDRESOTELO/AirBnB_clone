#!/usr/bin/python3
"""
Program that contains the entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Commnad interpreter class definition
    """
    prompt = "(hbnb)"

    def do_quit(self, command):
        """Command to EXIT program
        """
        return True

    def do_EOF(self, command):
        """Command to end program
        """
        return True

    def emptyline(self):
        """Do not execute anything with an empty line + ENTER """
        return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
