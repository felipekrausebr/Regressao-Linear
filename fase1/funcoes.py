"""Funções da fase 1. regressao retorna beta1, beta0, nessa ordem."""
import numpy as np

# Funções Matemáticas
def correlacao(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(np.multiply(x, y))
    sum_x2 = np.sum(np.power(x, 2))
    sum_y2 = np.sum(np.power(y, 2))

    numerator = (n * sum_xy) - (sum_x * sum_y)
    denominator = np.sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))

    if denominator == 0:
        return np.nan  # correlação indefinida sem variação
    else:
        return numerator / denominator

def regressao(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(np.multiply(x, y))
    sum_x2 = np.sum(np.power(x, 2))

    if n * sum_x2 - sum_x ** 2 == 0:
        raise ValueError('x deve apresentar variação para ajustar uma reta.')
    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    intercept = (sum_y - slope * sum_x) / n

    return slope, intercept
