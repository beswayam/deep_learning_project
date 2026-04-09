# Deep Learning Bioinformatics Project - AIN31306

Predicting protein GO (Gene Ontology) annotations from amino acid sequence using deep learning — specifically a 1D CNN baseline and a Transformer-based model (ESM-2 fine-tuning).

---

## Folder Structure

| Folder / File | Purpose |
|---|---|
| `notebooks/` | Jupyter notebooks (run in order 01 → 05) |
| `src/` | Reusable Python source code |
| `results/figures/` | Saved plots and visualisations |
| `results/predictions/` | Model prediction outputs (`.csv`) |
| `report/` | Report drafts and figures for submission |
| `requirements.txt` | Python dependencies |

---

## Notebook Order

| # | Notebook | Description |
|---|---|---|
| 01 | `01_data_exploration.ipynb` | Load & explore the protein dataset |
| 02 | `02_cnn_baseline.ipynb` | Train and evaluate the CNN baseline |
| 03 | `03_hyperparameter_experiments.ipynb` | Systematic hyperparameter search |
| 04 | `04_real_data.ipynb` | Apply best model to full dataset |
| 05 | `05_transformer.ipynb` | Fine-tune ESM-2 Transformer model |

---

## How to Run

### Local

```bash
# 1. Clone the repo
git clone https://github.com/beswayam/deep_learning_project.git
cd deep_learning_project

# 2. Create a virtual environment and install dependencies
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Launch Jupyter
jupyter notebook
```

Then open notebooks in order starting from `01_data_exploration.ipynb`.

### Google Colab

| Notebook | Colab Link |
|---|---|
| 01 Data Exploration | *(add link)* |
| 02 CNN Baseline | *(add link)* |
| 03 Hyperparameter Experiments | *(add link)* |
| 04 Real Data | *(add link)* |
| 05 Transformer | *(add link)* |

---

## Dependencies

- [PyTorch](https://pytorch.org/) — deep learning framework
- [Transformers (HuggingFace)](https://huggingface.co/docs/transformers) — ESM-2 protein language model
- [scikit-learn](https://scikit-learn.org/) — metrics and preprocessing
- [Biopython](https://biopython.org/) — sequence parsing
- [pandas](https://pandas.pydata.org/) — data manipulation
- [matplotlib](https://matplotlib.org/) / [seaborn](https://seaborn.pydata.org/) — visualisation

---

## Results Summary

*(To be filled in after experiments)*

| Model | F1 (macro) | Accuracy | Notes |
|---|---|---|---|
| CNN Baseline | - | - | - |
| Transformer (ESM-2) | - | - | - |
