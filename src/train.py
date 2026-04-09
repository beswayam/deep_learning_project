# src/train.py
# Training loop for protein GO annotation models.
# Functions to implement:
#   - train_epoch(model, loader, optimizer, criterion) -> avg_loss
#   - evaluate(model, loader, criterion) -> (avg_loss, predictions, targets)
#   - run_training(model, train_loader, val_loader, config) -> history dict
