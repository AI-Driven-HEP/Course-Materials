import torch

from .models import Model  
from .play import play_game

def train():
    # 1. Initialize model, loss, optimizer
    model = Model()


    # 2. Replace with real training
    for epoch in range(10):   # example: 10 epochs
        pass             


    # 3. ✅ After training is complete, save the model weights
    torch.save(model.state_dict(), "student_model.pth")
    print("Model saved as student_model.pth")
