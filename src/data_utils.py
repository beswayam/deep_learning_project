# src/data_utils.py
# Utilities for loading and preprocessing protein sequence data.
# Functions to implement:
#   - read_fasta(filepath) -> dict {protein_id: sequence}
#   - load_labels(filepath) -> pd.DataFrame
#   - encode_sequence(seq, vocab) -> List[int]
#   - build_dataset(fasta_path, labels_path) -> (X, y)
