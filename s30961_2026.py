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

def make_complement(sequence: str) -> str:
    """tworze sekwencję komplementarną"""
    result = ""

    for nucleotide in sequence:
        if nucleotide == "A":
            result += "T"
        elif nucleotide == "T":
            result += "A"
        elif nucleotide == "C":
            result += "G"
        elif nucleotide == "G":
            result += "C"

    return result


def make_reverse_complement(sequence: str) -> str:
    """tworze sekwencję odwrotnie komplementarną"""
    complement = make_complement(sequence)
    return complement[::-1]


def transcribe_to_mrna(sequence: str) -> str:
    """tworzy sekwencję mRNA"""
    return sequence.replace("T", "U")


def save_to_file(filename: str, content: str) -> None:
    """zapisuje dane do pliku"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
        file.write("# EOF_1\n")

        def main():
            """główna funkcja programu"""

            length = validate_positive_int("Podaj długość sekwencji: ")
            seq_id = get_sequence_id()
            description = input("Podaj opis sekwencji: ")
            name = input("Podaj imię: ")

            sequence = generate_sequence(length)
            sequence_with_name = insert_name(sequence, name)

            stats = calculate_stats(sequence)

            motif = input("Podaj motyw do wyszukania, np. ATG: ")
            motif_positions = find_motif(sequence, motif)

            complement = make_complement(sequence)
            reverse_complement = make_reverse_complement(sequence)
            mrna = transcribe_to_mrna(sequence)

            fasta_text = ""
            fasta_text += format_fasta(seq_id, description, sequence_with_name)
            fasta_text += format_fasta(seq_id + "_complement", "Sekwencja komplementarna", complement)
            fasta_text += format_fasta(seq_id + "_reverse_complement", "Sekwencja odwrotnie komplementarna",
                                       reverse_complement)
            fasta_text += format_fasta(seq_id + "_mRNA", "Sekwencja mRNA", mrna)

            filename = seq_id + ".fasta"
            save_to_file(filename, fasta_text)

            print(f"Sekwencja zapisana do pliku: {filename}")

            print(f"Statystyki sekwencji (n={length}):")
            print(f"A: {stats['A']:.2f}%")
            print(f"C: {stats['C']:.2f}%")
            print(f"G: {stats['G']:.2f}%")
            print(f"T: {stats['T']:.2f}%")
            print(f"GC-content: {stats['gc_ratio_A']:.2f}%")

            print("Pozycje motywu:")
            if motif_positions:
                print(motif_positions)
            else:
                print("Nie znaleziono motywu.")

        if __name__ == "__main__":
            main()