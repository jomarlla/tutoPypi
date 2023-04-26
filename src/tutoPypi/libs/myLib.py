"""
#Documentación de módulo myLib

Poner aquí la descripción del módulo

"""

#Esto es para decir que un parámetro puede ser de varios tipos, o any
from typing import Union, Any

#definición de la función
def mediaList(l:list[Union[float, str]])->float:
    """
    Documentación de la función ptoMedio.

    Devuelve la media de los números en la lista.

    Examples:
        >>> from libs import myLib
        >>> myLib.medialist([1,2,3])

    Args:
        l: La lista con los números a promediar. Pueden ser números o cadenas.
    
    Returns:
        La media de los números en la lista.
    """
    m:float=0
    for e in l:
        m=m+float(e)
    return m/len(l)
