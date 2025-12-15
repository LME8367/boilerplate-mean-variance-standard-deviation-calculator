import numpy as np

def calculate(numbers):
  if len(numbers) != 9:
    raise ValueError("List must contain nine numbers.")

  lst = np.array(numbers).reshape((3,3))

  calculations = {
    'mean': [lst.mean(axis=0).tolist(), lst.mean(axis=1).tolist(), lst.mean().tolist()],
    'variance': [lst.var(axis=0).tolist(), lst.var(axis=1).tolist(), lst.var().tolist()],
    'standard deviation': [lst.std(axis=0).tolist(), lst.std(axis=1).tolist(), lst.std().tolist()],
    'max': [lst.max(axis=0).tolist(), lst.max(axis=1).tolist(), lst.max().tolist()],
    'min': [lst.min(axis=0).tolist(), lst.min(axis=1).tolist(), lst.min().tolist()],
    'sum': [lst.sum(axis=0).tolist(), lst.sum(axis=1).tolist(), lst.sum().tolist()]
  }


  return calculations

print(calculate([0,1,2,3,4,5,6,7,8]))