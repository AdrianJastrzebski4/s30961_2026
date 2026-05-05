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

def validate_positive_int(prompt: str, min_val: int = 1, max_val: int = 100_000) -> int:
    """pobieram poprawną liczbę całkowitą"""
    while True:
        text = input(prompt)

        if text.isdigit():
            value = int(text)

            if min_val <= value <= max_val:
                return value

        print(f"Błąd: wartość musi być liczbą całkowitą z zakresu [{min_val}, {max_val}].")


def get_sequence_id() -> str:
    """pobiera ID sekwencji bez białych znaków"""
    while True:
        seq_id = input("Podaj ID sekwencji: ")

        if seq_id != "" and not any(char.isspace() for char in seq_id):
            return seq_id

        print("Błąd: ID nie może być puste ani zawierać białych znaków.")


def find_motif(sequence: str, motif: str) -> list:
    """wyszukuje motyw w sekwencji"""
    positions = []
    motif = motif.upper()

    for i in range(len(sequence) - len(motif) + 1):
        if sequence[i:i + len(motif)] == motif:
            positions.append(i + 1)

    return positions

