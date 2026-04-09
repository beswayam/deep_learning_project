# Project Context for AI Assistance

## Project Overview

This is a deep learning bioinformatics project for the course **AIN31306** at Wageningen University.
The goal is to predict **Gene Ontology (GO) functional annotations** for proteins from their
amino acid sequences, using:

1. A **1D CNN baseline** trained from scratch
2. A **Transformer model** (fine-tuned ESM-2 protein language model from Meta/HuggingFace)

## Repository Layout

```
notebooks/          - Jupyter notebooks (run 01 → 05 in order)
src/
  data_utils.py     - Data loading, FASTA parsing, encoding sequences
  model.py          - CNN and Transformer model definitions
  train.py          - Training loop, early stopping, checkpointing
  metrics.py        - F1, accuracy, per-class metrics, confusion matrix
results/
  figures/          - All saved plots (loss curves, confusion matrices, etc.)
  predictions/      - CSV files with model predictions
report/             - Report drafts and submission figures
```

## Key Design Decisions

- Protein sequences are encoded as integer indices (amino acid vocabulary) or one-hot
- GO annotation prediction is treated as **multi-label classification**
- CNN uses 1D convolutions over sequence positions
- Transformer uses ESM-2 (`esm2_t6_8M_UR50D` or larger) with a classification head
- All experiment metrics are logged to `results/experiment_log.csv` (one row per run)

## Coding Conventions

- All source code lives in `src/`; notebooks import from `sys.path.append('../src')`
- Plots are saved to `results/figures/` via `plt.savefig()`
- Use `torch.manual_seed(42)` for reproducibility
- Prefer functions over classes for simple utilities
- Type hints are encouraged in `src/` files

## Dataset

- Swiss-Prot / UniProt subset with GO term labels
- Sequences stored as FASTA; labels as CSV with `protein_id` and GO columns
- Raw data is **not committed** to git (too large); download instructions in notebook 01
