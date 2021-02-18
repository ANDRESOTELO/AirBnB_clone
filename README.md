![enter image description here](https://lh3.googleusercontent.com/LdLAW3MY82GvPbUlR-o8jnablOLV0luZZqjxiYkz5eRx3ZMQkNYb8gram4QYhuFKgRsJ2ZfgvCUZvpK2I1fu1Z9p5ZD3RYBN5bAp3H-tCGsqXW0ZRq4puXTkIe1RX2yQbn6OPMWZP9bNgOIQr3ubZPX94UFLKbs9XXxvPftL0FNAyKGAuTC58T56axOlQphhM1etD13zEgJLBswt8CCADeUpr79VelvrHuP30p1--iisaIC8RSXBs9lJza8v2QGEDlv97E7riKkMg5iTWF3yO_JOEBSeD-Jx_XBF51MoN_TuCaoXBOKiNPasnNcaTu_GK0PAkHDvxRdJRrkTNYAnrd0sGHiMtsUylBncfecTvXvVZ7j5uuaQxOYA_T_N8wMpn6ZxEuRfbdT4y-wZy9C36-fcGT4oTatbNwIF_ihw6DsbKVsxBscymb-9MfscR2VJZxuXAGWlTgoBJvp1uTPBV_drTIHS8u1q0PuP-k3j10feWXjGfQgkkWIyl5dy34p_wvOww80w7DEt6UKV6qbUjkj1XHv1NX6OlXKoqT02xRp_uHBQXqCjUb1_c7628ciDffewZRKGCrVXJP8cfBczVs4qXTwUziPd7K7UmSEL7Nr5VKgnEdFuMTeJWPrvoa7FDOCF0uopGsx5yPQoIT2MoZBFjr3KzWOKpHeZxHmKgCO7TMMcjafzgN2dCjbQFA=w1105-h422-no?authuser=0)
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