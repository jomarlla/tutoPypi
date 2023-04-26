"""
#Documentación del módulo main

Este es el punto de entrada del programa.
Este programa se ejecuta con
    >>> python3 main.py

El programa hace tal, tal y tal
"""

import os, sys
PROJEC_DIR=os.path.dirname(__file__)
sys.path.append(PROJEC_DIR)

from libs import myLib

def creaLista()->list[float]:
    """
    Documentación de a función creaLista.

    Esta función crea una lista para hacer una prueba.


    Examples:
        >>> from main import creaLista
        >>> creaLista()
    
    Returns:
        Una lista.
    """
    return [10.15, 125, 425, 253.25]

def main():
    """
    Documentación de a función main.

    Punto de entrada del programa.


    Examples:
        >>> from tutoPypi import main
        >>> main.main()
    
    Returns:
        la media.
    """
    l=creaLista()
    m=myLib.mediaList(l)
    return m


if __name__=='__main__':
    m=main()
    print (f"La media de la lista es es {m}")