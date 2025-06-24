import sys

if len(sys.argv) != 2:
    print("Usage: python contigs.py <fichier_fasta>")
    sys.exit(1)

fasta_file = sys.argv[1]
threshold = 1000000  # 1 Mb

count = 0
seq_len = 0

with open(fasta_file, 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith('>'):
            if seq_len > threshold:
                count += 1
            seq_len = 0  # Reset for next contig
        else:
            seq_len += len(line)
    # Check last contig
    if seq_len > threshold:
        count += 1

print(f"Nombre de contigs > 1 Mb : {count}")
