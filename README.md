![AirBnB](https://scontent.fbog2-2.fna.fbcdn.net/v/t1.0-9/151832876_10159252478228035_253539761794129848_o.jpg?_nc_cat=108&ccb=3&_nc_sid=730e14&_nc_eui2=AeEPCNdSL01DbLQIxvpkL-4eo6NOw32cMBujo07DfZwwG7xJiHFqVvB7sAK7733hs9s&_nc_ohc=pY7DkoTU_qgAX9Xtlff&_nc_ht=scontent.fbog2-2.fna&oh=a26132b856bde0285ab3ab6226148d02&oe=60549DB5)
# AirBnB Description

This repository contains our own simple version of the `arbnb`, this is an application to search and filter  interpreter

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

# Files

 - **README** : It contains all the information about the project and
   all its content. 
 - **console.py** : 
 - **models/** :
	 - **base_model.py**: 
	 - **user.py**:  
	 - **state.py** : 
	 - **city.py** : 
	 - **amenity.py** : 
	 -  **place.py** : 
	 - **review.py** : 

- **test/** :
	- **test_models/** :
		- **test_base_model.py**:  
		 - **test_user.py**: 
		 - **test_state.py** : 
		 - **test_city.py** : 
		 - **test_amenity.py** : 
		 -  **test_place.py** :  
		 - **test_review.py** : 

	- **test_engine/** :
		- **test_file_storage.py** : 

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