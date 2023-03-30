#!/usr/bin/env python
# -*- coding: utf-8 -*-

from clases.weapon_type import TipoArma

"""
This Python module contains not only the class Pokemon, but also the test of
this Python class.

@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  pokemon.py
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


class Pokemon():
    """Python class to implement a basic version of a Pokemon of the game.

    This Python class implements the basic version of a Pokemon of the game.

    Syntax
    ------
      obj = Pokemon(pokemon_id, nombre_pokemon, tipo_arma, puntos_salud, indice_ataque, indice_defensa)

    Parameters
    ----------
      [in] pokemon_id ID of the Pokemon : int
      [in] nombre_pokemon Name of the Pokemon : str
      [in] tipo_arma Type of weapon that carries out the Pokemon : Enum in TipoArma
      [in] puntos_salud Points of health that the Pokemon has : int in range(1, 101)
      [in] indice_ataque Attack rating of the Pokemon : int in range(1, 11)
      [in] indice_defensa Defense rating of the Pokemon: int in range(1, 11)

    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class Pokemon.

    Attributes
    ----------
    todos los atributos serán privados, pero accesibles mediante getters
    el único atributo modificable será el estado de salud del pokemon

    Example
    -------
      >>> from pokemon import Pokemon
      >>> from tipo_arma import TipoArma
      >>> obj_Pokemon = Pokemon(1, "Bulbasaur", TipoArma.PUÑETAZO, 100, 7, 10)
    """

    def __init__(self, pokemon_id, nombre_pokemon, tipo_arma, puntos_salud, indice_ataque, indice_defensa):
        # hacemos los atributos privados, usaremos getters para poder acceder a ellos
        self.__num_id = pokemon_id
        self.__nombre = nombre_pokemon
        self.__arma = tipo_arma
        self.__salud = puntos_salud
        self.__ataque = indice_ataque
        self.__defensa = indice_defensa

        # verificamos que los parámetros de entrada son del tipo correcto y son válidos
        if not isinstance(self.__num_id, int):
            raise TypeError("The parameter id must be an integer.")
        # try:
        #   self.num_id = int(pokemon_id)   es un entero
        #   self.num_id not in lista_ids    no está en la lista de ids
        # except:
        #   raise TypeError("The parameter id must be a valid integer.")

        if not isinstance(self.__nombre, str):
            raise TypeError("The parameter nombre_pokemon must be a string.")
        if not isinstance(self.__arma, TipoArma):
            raise TypeError("The parameter tipo_arma must be a TipoArma.")
        if not isinstance(self.__salud, int) and self.__salud not in range(1, 101):
            raise TypeError("The parameter puntos_salud must be an integer between 1 and 100.")
        if not isinstance(self.__ataque, int) and self.__ataque not in range(1, 11):
            raise TypeError("The parameter indice_ataque must be an integer between 1 and 10.")
        if not isinstance(self.__defensa, int) and self.__defensa not in range(1, 11):
            raise TypeError("The parameter indice_defensa must be an integer between 1 and 10.")
        

    def __del__(self): # eliminar la instancia de Pokemon de la lista global
        pass

    def __str__(self): # método que devuelve una cadena con la información del objeto
        return "Pokemon ID " + str(self.__num_id) + " with name " + self.__nombre + " has as weapon " + self.__arma.name + " and health " + str(self.__salud)

    # GETTERS y SETTERS
    def get_num_id(self): 
        return self.__num_id
    def get_nombre(self):
        return self.__nombre
    def get_arma(self):
        return self.__arma
    def get_salud(self):
        return self.__salud
    def get_ataque(self):
        return self.__ataque
    def get_defensa(self):
        return self.__defensa
    # el único atributo modificable es el estado de salud del pokemon
    def set_salud(self, new_health_points):
        self.__salud = new_health_points
    

    def is_alive(self): # devuelve True si el pokemon sique vivo, esto es, tiene puntos de salud > 0
        '''Método para saber si el Pokemon está vivo o no'''
        if self.__salud > 0:
            return True
        else:
            return False

    def fight_defense(self, damage_points):
        '''Método que implementa la defensa del Pokémon de un golpe de otro Pokémon'''
        if self.__defensa < damage_points: # si la defensa es menor que los puntos de daño, la salud se ve afectada
            daño = damage_points - self.get_defensa() # calculamos el daño que recibirá el pokemon en base a sus puntos de defensa
            self.set_salud( self.get_salud() - daño ) # actualizamos la salud del pokemon
            return True
        else:
            return False
    
    def fight_attack(self, enemy):
        '''Método que implementa el ataque del Pokémon usando un golpe sobre otro Pokémon.
            Basado en el fight_defense del pokemon enemigo'''
        # confirmamos que el enemigo es un objeto de la clase Pokemon
        if not isinstance(enemy, Pokemon):
            raise TypeError("The parameter enemy must be a Pokemon.")
        else: # ya sabemos que el enemigo es un pokemon
            if self.__ataque > enemy.get_defensa(): # si nuestro ataque es mayor que su defensa, hacemos daño al enemigo
                enemy.fight_defense(self.__ataque) # el enemigo se defiende de nuestro ataque
                return True
            else:
                return False
            

def main():
    """Function main of the module.

    The function main of this module is used to test the Class that is described
    in this module.

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
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = Pokemon(1, "Ivysaur", TipoArma.CABEZAZO, 100, 8, 9)

    if pokemon_1.get_nombre() == "Ivysaur":
        print("Test PASS. The parameter nombre_pokemon has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_arma().name == "CABEZAZO":
        print("Test PASS. The parameter tipo_arma has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_salud() == 100:
        print("Test PASS. The parameter puntos_salud has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_ataque() == 8:
        print("Test PASS. The parameter indice_ataque has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defensa() == 9:
        print("Test PASS. The parameter indice_defensa has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = Pokemon(2, "Charmander", TipoArma.CABEZAZO, 100, 7, 10)

    if str(pokemon_2) == "Pokemon ID 2 with name Charmander has as weapon CABEZAZO and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = Pokemon(3, "Wartortle", TipoArma.PATADA, 97, 8, 9)

    if pokemon_3.is_alive():
        pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if not pokemon_3.is_alive():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = Pokemon(4, "Squirtle", TipoArma.CODAZO, 93, 9, 6)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_salud() == 29:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = Pokemon(5, "Venusaur", TipoArma.PUÑETAZO, 99, 10, 7)
    pokemon_6 = Pokemon(6, "Charmeleon", TipoArma.PUÑETAZO, 99, 9, 8)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_salud() == 97:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_salud() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
