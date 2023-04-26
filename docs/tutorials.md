# Tutorial

## Requirements
- Python >=3
- Psycopg2
- PostgreSQl >= 10

## Installation

###Windows

Use [pip](https://pypi.org/project/pip/) to install the packages in the virtual environment:

    pip install tutoPypi

### Linux distributions
In Linux it is good practice always use Python [virtual environments](https://docs.python.org/3/library/venv.html) to install new Python libraries. To use Python virtual environments you must install the `venv` library:

> **_NOTE:_**  Make sure, in the bellow listings, to replace the `X` of `python3.X` for your Python distribution version.
> 

    sudo apt-get install python3.X-venv
   
Navigate to the folder where you want to create the virtual environment, for example the `venvs` folder, and type:

    python3.X -m venv tutopypi

Activate the virtual environment to install the packages:
   
    source tutopypi/bin/activate

Install the psycopg2 dependency:

    (pgOperations)$pip install psycopg2

In Linux distributions may be the installation of `psycopg2` fail. In this cases you must install the following before:

    sudo apt-get install libpq-dev -y 
    sudo apt-get install build-essential -y 
    sudo apt-get install python3.X-dev -y 
    
Now you can proceed with the installation of `psycopg2`.

    (pgOperations)$pip install psycopg2
        Collecting psycopg2
        Building wheels for collected packages: psycopg2
        Building wheel for psycopg2 (setup.py) ... error
        ...
        ...
        Installing collected packages: psycopg2
        Running setup.py install for psycopg2 ... done
        Successfully installed psycopg2-2.9.5

And install `tutoPypi`:

    (tutopypi)$pip install tutoPypi

You are ready to use the library.

## Summary

Este es el resumen
## Ejemplo de uso

Importar la librería

    from tutoPypi import main

Ejecutar el programa

    main.main()

Resultado:
    203.35

