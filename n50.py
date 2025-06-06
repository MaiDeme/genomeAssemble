import argparse
import matplotlib.pyplot as plt

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
    sorted_lengths = sorted(lengths)
    cumulative_length = 0
    sorted_lengths = sorted_lengths[:-3]
    print(sorted_lengths)

    total_length= sum(sorted_lengths)

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

def contigs_more_than_n(lengths, n):
    return len([length for length in lengths if length > n])

def histogram(lengths):
    plt.hist(lengths, bins=100)
    plt.show()
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("fasta_file")
    args = parser.parse_args()

    lengths = read_fasta(args.fasta_file)
    n50 = calculate_n50(lengths)
    l50 = calculate_l50(lengths)
    histogram(lengths)
    print(f"contigs more than 100: {contigs_more_than_n(lengths, 1000000)}")
    print(f"N50: {n50}")
    print(f"L50: {l50}")


if __name__ == "__main__":
    main()