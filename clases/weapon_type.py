#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum


"""
This Python module contains not only the Enum TipoArma, but also the test of
this Python class.

@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  weapon_type.py
@author :  Antonio Artes Garcia (antonio.artesgarcia@ceu.es)
           Francisco Hernando Gallego (francisco.hernandogallego@ceu.es)
           Ruben Juarez Cadiz (ruben.juarezcadiz@ceu.es)

@version :  0.0.1, 08 November 2021
@information :  The Zen of Python
                  https://www.python.org/dev/peps/pep-0020/
                Style Guide for Python Code
                  https://www.python.org/dev/peps/pep-0008/
                Example NumPy Style Python Docstrings
                  http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
                doctest – Testing through documentation
                  https://pymotw.com/2/doctest/

@copyright :  Copyright 2021 GNU AFFERO GENERAL PUBLIC.
              All rights are reserved. Reproduction in whole or in part is
              prohibited without the written consent of the copyright owner.
"""


# Source packages.



class TipoArma(Enum):
    """Python class to implement an enumeration for the attribute Weapon Type.

    This Python class implements an enumeration for the attribute Weapon Type.

    Syntax
    ------
      obj = TipoArma.Enum

    Parameters
    ----------

    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class TipoArma.

    Attributes
    ----------

    Example
    -------
      >>> from weapon_type import TipoArma
      >>> obj_TipoArma = TipoArma.Boxer
    """

    PUÑETAZO = 2
    PATADA = 4
    CODAZO = 6
    CABEZAZO = 10


def main():
    """Function main of the module.

    The function main of this module is used to test the Class TipoArma.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("=================================================================.")
    print("Test Case 1: Check Class TipoArma - Name.")
    print("=================================================================.")

    if isinstance(TipoArma.PUÑETAZO, TipoArma):
        print("Test PASS. The enum for Puñetazo has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(TipoArma.PATADA, TipoArma):
        print("Test PASS. The enum for Patada has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(TipoArma.CODAZO, TipoArma):
        print("Test PASS. The enum for Codazo has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(TipoArma.CABEZAZO, TipoArma):
        print("Test PASS. The enum for Cabezazo has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================.")
    print("Test Case 2: Check Class TipoArma - Value.")
    print("=================================================================.")

    if TipoArma.PUÑETAZO.value == 2:
        print("Test PASS. The enum for Puñetazo has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if TipoArma.PATADA.value == 4:
        print("Test PASS. The enum for Patada has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if TipoArma.CODAZO.value == 6:
        print("Test PASS. The enum for Codazo has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if TipoArma.CABEZAZO.value == 10:
        print("Test PASS. The enum for Cabezazo has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
