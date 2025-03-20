import argparse

def read_fasta(file_path):
    """Reads a FASTA file and returns a list of sequence lengths."""
    with open(file_path, 'r') as file:
        lengths = []
        seq = ''
        for line in file:
            line = line.strip()
            if line.startswith('>'):  # Header line
                if seq:
                    lengths.append(len(seq))
                seq = ''
            else:
                seq += line
        if seq:  # for the last sequence in the file
            lengths.append(len(seq))
    return lengths


def calculate_n50(lengths):
    total_length = sum(lengths)
    sorted_lengths = sorted(lengths)
    cumulative_length = 0
    for length in sorted_lengths:
        cumulative_length += length
        if cumulative_length >= total_length / 2:
            return length
    return None

def calculate_l50(lengths):
    total_length = sum(lengths)
    sorted_lengths = sorted(lengths)
    cumulative_length = 0
    for length in sorted_lengths:
        cumulative_length += length
        if cumulative_length >= total_length / 2:
            return len(sorted_lengths) - sorted_lengths.index(length)
    return None

def calculate_n90(lengths):
    total_length = sum(lengths)
    sorted_lengths = sorted(lengths)
    cumulative_length = 0
    for length in sorted_lengths:
        cumulative_length += length
        if cumulative_length >= total_length * 0.9:
            return length
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("fasta_file")
    args = parser.parse_args()

    lengths = read_fasta(args.fasta_file)
    n50 = calculate_n50(lengths)
    l50 = calculate_l50(lengths)
    n90 = calculate_n90(lengths)
    print(f"N50: {n50}")
    print(f"L50: {l50}")
    print(f"N90: {n90}")


if __name__ == "__main__":
    main()