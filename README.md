# AirBnB clone - The Console
![img](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210629%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210629T151902Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b15af14a41572bc0adabade4ddca0879f7be1632ff6a88c77737f84b07d0d818)

## Description

_This is the first step towards building a full web application: the AirBnB clone.
This first step is very important because it will be the base to build other following projects: HTML/CSS templating, database storage, API, front-end integration_

## Usage

_This Programm works both, interactive and non-interactive mode. In interactive mode, similar to a Unix Shell but limited to some uses, it prints a promp and wait for the user to input something_

_In non-interactive mode you will need to run with a command input piped into its execution so that the command is run quickly._

## Interactive mode Example

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help help
List available commands with "help" or detailed help with "help cmd".
(hbnb) create BaseModel
78576d4b-7866-4ff7-85ef-e814e4a7b623
(hbnb) quit
$
```

## Non-interactive mode example

```
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
$ echo " create City" | ./console.py 
(hbnb) 6f753454-9bd2-461b-9a51-00aa48f0670d
(hbnb)
$ echo "destroy" | ./console.py 
(hbnb) ** class name missing **
(hbnb)
$
```

## Commands
the commands recognized by the console are the following:

|Command | Description |
|--|--|
| **EOF and quit** | Both of them exits from the program. Usage: typing "quit" or pressing Ctrl + D. |
| **help** | List available commands. Usage: typing "help" or "help <command\>". |
| **all** | Prints all string representation of all instances. Usage: typing "all" or "all <class name\>". |
| **create** | Creates a new instance of the class we want. usage: "create <class name\>". |
| **destroy** | Deletes an instance based on the class name and id. Usage: "destroy <class name\> <id\>". |
| **show** | Prints the string representation of an instance based on the class name and id. Usage: "show <class name\> <id\>"
| **update** |  Updates an instance based on the class name and id by adding or updating attribute. Usage: 'update <class name\> <id\> <attribute name\> "attribute value"'

## Models and Engine

_In these packages we will find two different type of files, in models we will find classes that will be used in a future to save information and keep it safe. The engine folder contains the file that serialize and deserilize all of the data in the JSON format and save it into a file .json._

### Authors

*Angui Clavijo Gutierrez* | [@angie-clavijo-desarrollo](https://github.com/angie-clavijo-desarrollo)
*Jean Pierre Ballen* | [@jeanpierreba](https://github.com/jeanpierreba)
