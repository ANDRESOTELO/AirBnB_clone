# AirBnB_clone
(image here)
#  Description

This repository contains our own simple version of the `shell`, that is a command interpreter to read, write, execute files or programs, using command in a terminal, for more context read [linux command](https://linuxcommand.org/lc3_lts0010.php)

##  Example

Iteractive mode:
 - Execute the `simple_shell` file, then you will be inside the minishell

       $ ./simple_shell
       ¥ minishell ¶:
       ¥ minishell ¶: ls
        built-in.c header.h ctrl_c.c minishell.c splits_string.c
        exec.c sfree.c string_directory.c 
       ¥ minishell ¶: /bin/ls
        built-in.c header.h ctrl_c.c minishell.c splits_string.c
        exec.c sfree.c string_directory.c 

Non/interactive
 - Write `echo` and between doble quotes `" "` put the command to execute and after the pipeline `|` execute the `simple_shell` file

    `$ echo "ls" | ./simple_shell` 
   ` ¥ minishell ¶:`
`built-in.c header.h ctrl_c.c minishell.c splits_string.c
exec.c sfree.c string_directory.c`

# Flowchart
(image here)

# Files

 - **README** : It contains all the information about the project and
   all its content. 
 - **header.h** : It is the header file you can find all the libraries that we use to create this program, also all the prototypes of the functions that we create to navigate and run the `shell`
 - **shell.c** : This is the main program to start the infinity loop of the simple_shell, it contains the SIGNAL to campture the `ctrl + c`, it evaluate if the entry command is a built-in, a program or just a non existent value.
 - **strfunctions.c** : Contains the function to create copies of a string, copare it or divided by tokens.
 - **advstr.c** : Have functions to divide an entry string or the PATH depends of the entry argument.
 - **executable.c** : In this file you can find the executable fucntions from the shell like fork process, print the enviroment or concatenate the PATH.
 -  **extra.c** : There are the final functions like convert a integers into a string, handle error in the prompt and a function to free memory from a double pointer string.
 - **man_1_simple_shell.1.gz** : This is the manual that contains the synopsis, description, return, and more  specifiers of the simple_shell that we create.


##  To compile

    $ gcc -Wall -Werror -Wextra -pedantic header.h *.c -o minishell

## More info for execute

    valgrind --leak-check=full --show-leak-kinds=all ./minishell

##  Requirements

 - Ubuntu 16.04.7 LTS
 - Functions and files will be compiled with gcc 4.8.4
   with flags 
   
 - All the files must have [Betty](https://github.com/holbertonschool/Betty/wiki) style


## Author
 
 - **Juan Carlos Hernandez** : [@luigi_jong](https://twitter.com/luigi_jong)

##  info

 - Date (DD/MM/YYYY)
 - Holberton school Colombia 
 - Cohort #13 BOG0920
