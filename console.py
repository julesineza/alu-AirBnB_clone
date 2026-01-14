#!/usr/bin/python3
"""
command interpreter console.py using cmd module python
"""

import cmd 
class HBNBCommand(cmd.Cmd):
    """
     A program that contains the entry point of the command interpreter

    Args :
        cmd.Cmd     
    """
    prompt = '(hbnb)'

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_EOF(self,arg):
        """
        Quit command to exit the program
        """
        return True

    def do_quit(self,arg):
        """
        Quit command to exit the program
        """
        return True
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()        
