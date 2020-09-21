#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List

def convert_to_absolute() -> float:
    nombre =int(input("Choisie un nombre: "))
    return abs(nombre)


def use_prefixes() -> List[str]:
    result =[]
    prefixes, suffixes = 'JKLMNOPQ', 'ack'
    for i in range(0,len(prefixes)):
        name = prefixes[i] + suffixes
        result.append(name)
    return result


def prime_integer_summation() -> int:
    sum = 0
    for i in range(2,100):
        prime = True
        for divider in range(2, int((i / 2)**1/2)+1):
            if i % divider == 0:
                prime = False

        if prime == True:
            sum += i
            print(i)

    return sum


def factorial(number: int) -> int:
    return 0


def use_continue() -> None:
    pass


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
