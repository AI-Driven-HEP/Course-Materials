try:
    import torch.nn as nn
except Exception:
    class nn:  # minimal shim if torch isn't installed yet
        class Module: pass
class Model(nn.Module):
    """
    👉 Students: Replace this with your own model!
    - Input: 9 board cells --> torch.tensor([env.board], dtype=torch.float32)
    - Output: policy (9 moves) --> torch.Size([1, 9]) , value (game outcome) --> torch.Size([1, 1])
    """
    pass
