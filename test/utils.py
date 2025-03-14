import torch

dtypes = [torch.half, torch.bfloat16, torch.float, torch.double,
          torch.int, torch.long]
grad_dtypes = [torch.half, torch.float, torch.double]

devices = [torch.device('cpu')]
if torch.cuda.is_available():
    devices += [torch.device(f'cuda:{torch.cuda.current_device()}')]


def tensor(x, dtype, device):
    return None if x is None else torch.tensor(x, dtype=dtype, device=device)
