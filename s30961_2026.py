#Numer albumu: s30961
#Data: 2026
#Opis: Generator losowych sekwencji DNA w formacie FASTA.

import random


def generate_sequence(length: int) -> str:
    """zwracam losowa sekwencję DNA o długości"""
    sequence = ""

    for _ in range(length):
        sequence += random.choice("ACGT")

    return sequence




