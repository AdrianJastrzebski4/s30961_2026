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


def calculate_stats(sequence: str) -> dict:
    """zwracam słownik ze statystykami"""
    length = len(sequence)

    a = sequence.count("A") / length * 100
    c = sequence.count("C") / length * 100
    g = sequence.count("G") / length * 100
    t = sequence.count("T") / length * 100
    gc = (sequence.count("G") + sequence.count("C")) / length * 100

    return {
        "A": a,
        "C": c,
        "G": g,
        "T": t,
        "gc_ratio_A": gc
    }


def insert_name(sequence: str, name: str) -> str:
    """wstawiam imię w losową pozycję"""
    position = random.randint(0, len(sequence))
    return sequence[:position] + name.lower() + sequence[position:]


def format_fasta(seq_id: str, description: str, sequence: str, line_width: int = 80) -> str:
    """zwracam sformatowany rekord fasta"""
    header = ">" + seq_id

    if description != "":
        header += " " + description

    result = header + "\n"

    for i in range(0, len(sequence), line_width):
        result += sequence[i:i + line_width] + "\n"

    return result

