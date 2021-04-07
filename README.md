![enter image description here](https://i.imgur.com/SIHaun2.png)
# AirBnB Description

This repository contains our own simple version of `arbnb`, this is an application to search for records, filter them or create new users, here you will find an executable console in which you can execute different commands and save your information in a `json` file to later update a data base.

##  Example

Iteractive mode:
 - Execute the `console.py` file this way `./console.py` then you will be inside the consol command interpreter.

       AirBnB_clone$ ./console.py
       (hbnb)help
       
       Documented commands (type help <topic>):
       ========================================
       EOF  all  create  destroy  help  quit  show  update
       
       (hbnb)create BaseModel
       79b0ea7a-cbb2-469c-b70a-607d21df4c66
       (hbnb)all
       (hbnb)
       ["[BaseModel] (79b0ea7a-cbb2-469c-b70a-607d21df4c66) 
       {'created_at': datetime.datetime(2021, 2, 17, 21, 23, 11), 
       'id': '79b0ea7a-cbb2-469c-b70a-607d21df4c66',
       'updated_at': datetime.datetime(2021, 2, 17, 21, 23, 11)
        }"]
       (hbnb)destroy BaseModel 79b0ea7a-cbb2-469c-b70a-607d21df4c66 
       (hbnb)all
       []
       (hbnb)show BaseModel 79b0ea7a-cbb2-469c-b70a-607d21df4c66
       ** no instance found **
       (hbnb)

Non/interactive
 - Write `echo` and between doble quotes `" "` put the command to execute and after the pipeline `|` execute the `console` file

```
AirBnB_clone$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
AirBnB_clone$
```
## Commands for interactive mode
***help***: Display  all available commands in the console.
***help***<'command'>: Show what the command does.
***create***  *<'Class_name'>* : Create a new instance of the class.
***show*** *<'Class_name'> <'id'>* : Display the specified instance. 
***all***: Display all the instances there are created.
***all*** *<'Class_name'>* : Display only matches instances.
***update*** *<'Class_name'><'id'><'attribute'><'value'>*: Modify the especified instance with the attribute as a key and the value.
***destroy*** *<'Class_name'><'id'>*: Delete the especified instance.
***quit***: Close the command interpreter.
***ctrl + d***: Signal to close the console. 
 
# Files

 - **README** 
 - **console.py** 
 - **models/** 
	 - **base_model.py**
	 - **user.py**
	 - **state.py** 
	 - **city.py** 
	 - **amenity.py** 
	 -  **place.py** 
	 - **review.py** 

- **test/** 
	- **test_models/** 
		- **test_base_model.py**
		 - **test_user.py**
		 - **test_state.py** 
		 - **test_city.py** 
		 - **test_amenity.py** 
		 -  **test_place.py** 
		 - **test_review.py** 

	- **test_engine/** :
		- **test_file_storage.py** : 

## Flowchart
![enter image description here](https://media.discordapp.net/attachments/756643698447613992/811984924407234570/Flowchart.png?width=491&height=473)

## Execute tests

    AirBnB_clone$ python3 -m unittest discover tests
    ...................................
    --------------------------------------------------
    Ran 35 tests in 0.078s
    
    OK
    AirBnB_clone$

##  Requirements

 - *Ubuntu 16.04.7 LTS*
 - *Python 3.5.2*
 - All the files must have *[pep8](https://github.com/treyhunner/pep8)* style

## Authors
 
 - **Juan Carlos Hernández** : Twitter - [@luigi_jong](https://twitter.com/luigi_jong)
 - **Andres Sotelo Duran** :  Twitter - [@looperdesignco](https://twitter.com/looperdesignco)

##  info

 - Date 17/02/2021)
 - Holberton school Colombia 
 - Cohort #13 BOG0920