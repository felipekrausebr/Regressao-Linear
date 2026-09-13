"""Fase 1: correlação e regressão linear simples."""
from pathlib import Path
import argparse
import numpy as np
import matplotlib.pyplot as plt
from funcoes import correlacao, regressao

# Dados fornecidos

x1 = [10,8,13,9,11,14,6,4,12,7,5]
y1 = [8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68]

x2 = [10,8,13,9,11,14,6,4,12,7,5]
y2 = [9.14,8.14,8.47,8.77,9.26,8.10,6.13,3.10,9.13,7.26,4.74]

x3 = [8,8,8,8,8,8,8,8,8,8,19]
y3 = [6.58,5.76,7.71,8.84,8.47,7.04,5.25,5.56,7.91,6.89,12.50]

x4 = [10.0,8.0,13.0,9.0,11.0,14.0,6.0,4.0,12.0,7.0,5.0]
y4 = [7.46,6.77,12.74,7.11,7.81,8.84,6.08,5.39,8.15,6.42,5.73]

x5 = [10.0,8.0,9.0,11.0,14.0,6.0,4.0,12.0,7.0,5.0]
y5 = [7.46,6.77,7.11,7.81,8.84,6.08,5.39,8.15,6.42,5.73]


def main(mostrar=True):
    # Organizando os dados em uma lista para iterar com um laço 'for'
    datasets = [
        (x1, y1, 'blue', 'Conjunto 1'),
        (x2, y2, 'orange', 'Conjunto 2'),
        (x3, y3, 'green', 'Conjunto 3'),
        (x4, y4, 'red', 'Conjunto 4'),
        (x5, y5, 'purple', 'Conjunto 5 (teste removendo Outlier do Conjunto 4)')
    ]

    # Cinco gráficos em uma grade de 3 linhas e 2 colunas
    fig, axs = plt.subplots(3, 2, figsize=(14, 10))

    # Transformando os eixos em uma lista para facilitar o laço
    axs = axs.flatten()

    for i, (x, y, color, label) in enumerate(datasets):
        x_arr = np.array(x)
        y_arr = np.array(y)

        # 1. Calculando a correlação
        r = correlacao(x_arr, y_arr)

        # 2. Calculando a regressão (slope = B1, intercept = B0)
        b1, b0 = regressao(x_arr, y_arr)

        # 3. Calculando os pontos da reta de regressão (y = B0 + B1*x)
        y_previsto = b0 + b1 * x_arr

        # 4. Plotando o Gráfico de Dispersão (os pontos)
        axs[i].scatter(x_arr, y_arr, color=color, label=label)

        # 5. Plotando a Reta de Regressão (a linha)
        # Ordenamos o 'x' apenas para a linha ser desenhada de forma contínua da esquerda para a direita
        x_sorted = np.sort(x_arr)
        y_previsto_sorted = b0 + b1 * x_sorted
        axs[i].plot(x_sorted, y_previsto_sorted, color='black', linestyle='--')

        # 6. Adicionando os títulos com os resultados (arredondados para 4 casas decimais)
        title_str = f"{label}\nCorrelação: {r:.4f} | B0: {b0:.4f} | B1: {b1:.4f}"
        axs[i].set_title(title_str)
        axs[i].set_xlabel('x')
        axs[i].set_ylabel('y')
        axs[i].grid(alpha=0.2)
        print(f'{label}: r={r:.6f}, beta0={b0:.6f}, beta1={b1:.6f}')

    # Ajustando o espaçamento para os gráficos não grudarem uns nos outros
    axs[-1].set_visible(False)
    plt.tight_layout()
    saida = Path(__file__).resolve().parent / 'resultados'
    saida.mkdir(exist_ok=True)
    fig.savefig(saida / 'regressoes.png', dpi=150)
    if mostrar:
        plt.show()
    else:
        plt.close(fig)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sem-janela', action='store_true')
    args = parser.parse_args()
    main(mostrar=not args.sem_janela)
