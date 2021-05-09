import numpy as np

def calculate(list):
    if len(list) != 9: raise ValueError('List must contain nine numbers.')
    
    matrix = np.array([list[0:3], list[3:6], list[6:]])

    mean = [
      [matrix[:, 0].sum() / 3, matrix[:, 1].sum() / 3, matrix[:, 2].sum() / 3], 
      [matrix[0].sum() / 3, matrix[1].sum() / 3, matrix[2].sum() / 3], 
      sum(list) / 9
    ]

    variance = [
      [((matrix[:, 0] - mean[0][0]) ** 2).sum() / 3, ((matrix[:, 1] - mean[0][1]) ** 2).sum() / 3, ((matrix[:, 2] - mean[0][2]) ** 2).sum() / 3],
      [((matrix[0] - mean[1][0]) ** 2).sum() / 3, ((matrix[1] - mean[1][1]) ** 2).sum() / 3, ((matrix[2] - mean[1][2]) ** 2).sum() / 3],
      ((np.array(list) - mean[2]) ** 2).sum() / 9
    ]

    sd = [
      [a ** (1/2) for a in variance[0]],
      [a ** (1/2) for a in variance[1]],
      variance[2] ** (1/2)
    ]

    _max = [
      [matrix[:, 0].max(), matrix[:, 1].max(), matrix[:, 2].max()], 
      [matrix[0].max(), matrix[1].max(), matrix[2].max()], 
      max(list)
    ]

    _min = [
      [matrix[:, 0].min(), matrix[:, 1].min(), matrix[:, 2].min()], 
      [matrix[0].min(), matrix[1].min(), matrix[2].min()], 
      min(list)
    ]

    _sum = [
      [matrix[:, 0].sum(), matrix[:, 1].sum(), matrix[:, 2].sum()], 
      [matrix[0].sum(), matrix[1].sum(), matrix[2].sum()], 
      sum(list)
    ]

    return {
      'mean': mean,
      'variance': variance,
      'standard deviation': sd,
      'max': _max,
      'min': _min,
      'sum': _sum
    }