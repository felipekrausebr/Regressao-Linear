"""Regressão múltipla pela equação normal do enunciado."""
import numpy as np


def regmultipla(X, y):
    """Recebe X (m, n+1), já com coluna de uns, e y (m,) ou (m,1).

    Retorna [beta0, beta1, ...]. Resolve (X.T @ X) beta = X.T @ y,
    equivalente a inv(X.T @ X) @ X.T @ y, sem calcular a inversa.
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    if y.ndim == 2 and y.shape[1] == 1:
        y = y[:, 0]
    if X.ndim != 2 or y.ndim != 1 or X.shape[0] != y.size:
        raise ValueError('X deve ser uma matriz e y deve ter um valor por linha.')
    if not np.isfinite(X).all() or not np.isfinite(y).all():
        raise ValueError('Os dados devem ser finitos.')
    if X.shape[1] == 0 or not np.allclose(X[:, 0], 1):
        raise ValueError('A primeira coluna de X deve conter uns (intercepto).')
    if np.linalg.matrix_rank(X) < X.shape[1]:
        raise ValueError('X possui colunas linearmente dependentes.')
    return np.linalg.solve(X.T @ X, X.T @ y)
