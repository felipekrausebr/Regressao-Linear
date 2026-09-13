"""Fase 2: execute python rmdemo.py; use --sem-janela para apenas salvar."""
from pathlib import Path
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator
from mpl_toolkits.mplot3d import Axes3D  # suporte aos eixos 3D
from sklearn.linear_model import LinearRegression
from regmultipla import regmultipla


def correlacao(x, y):
    """Correlação de Pearson pela fórmula da fase 1."""
    dx = np.asarray(x, dtype=float) - np.mean(x)
    dy = np.asarray(y, dtype=float) - np.mean(y)
    denominador = np.sqrt(np.sum(dx**2) * np.sum(dy**2))
    if denominador == 0:
        return np.nan  # correlação indefinida, não correlação zero
    return np.sum(dx * dy) / denominador


def regressao(x, y):
    """Retorna beta0 e beta1 da regressão simples."""
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    dx, dy = x - x.mean(), y - y.mean()
    b1 = np.sum(dx * dy) / np.sum(dx**2)
    return y.mean() - b1 * x.mean(), b1


def main(arquivo=None, mostrar=True):
    pasta = Path(__file__).resolve().parent
    arquivo = Path(arquivo) if arquivo else pasta / 'data.csv'
    saida = pasta / 'resultados'
    saida.mkdir(exist_ok=True)

    # a) CSV sem cabeçalho: preservar também a primeira observação.
    dados = pd.read_csv(arquivo, header=None)
    if dados.shape[1] != 3:
        raise ValueError('O CSV deve conter tamanho, quartos e preço, nessa ordem.')
    dados.columns = ['tamanho', 'quartos', 'preco']
    if not np.isfinite(dados.to_numpy(dtype=float)).all():
        raise ValueError('Há dados ausentes ou não finitos.')

    # b) Análise descritiva e respostas usando os registros observados.
    resumo = dados.describe()
    menores = dados.loc[dados.tamanho == dados.tamanho.min()]
    caras = dados.loc[dados.preco == dados.preco.max()]

    # c) Cada linha representa uma casa. A coluna de uns estima beta0.
    atributos = dados[['tamanho', 'quartos']].to_numpy(dtype=float)
    X = np.column_stack([np.ones(len(dados)), atributos])
    y = dados.preco.to_numpy(dtype=float)

    # d) Dois ajustes SIMPLES, cada um com uma variável explicativa.
    rs = [correlacao(atributos[:, j], y) for j in range(2)]
    fig, eixos = plt.subplots(1, 2, figsize=(12, 5), layout='constrained')
    preco_tick = FuncFormatter(lambda valor, pos: f'{valor / 1000:.0f}')
    for j, (ax, nome) in enumerate(zip(eixos, ['Tamanho da casa', 'Número de quartos'])):
        x = atributos[:, j]
        b0, b1 = regressao(x, y)
        grade = np.linspace(x.min(), x.max(), 100)
        ax.scatter(x, y, color='#245c91', alpha=.8, label='Casas observadas')
        ax.plot(grade, b0 + b1 * grade, color='#bc4c25', label='Regressão simples')
        ax.set(xlabel=nome, ylabel='Preço (mil unidades monetárias)',
               title=f'{nome} e preço\nr = {rs[j]:.4f}\nβ₀ = {b0:.2f}; β₁ = {b1:.2f}')
        ax.yaxis.set_major_formatter(preco_tick)
        ax.grid(alpha=.2)
        ax.legend()
        if j == 1:
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    fig.savefig(saida / 'regressoes_simples.png', dpi=160)

    # e–g) Em três dimensões, a regressão múltipla é um plano.
    beta = regmultipla(X, y)
    fig3d = plt.figure(figsize=(11, 8))
    ax = fig3d.add_subplot(111, projection='3d')
    ax.scatter(atributos[:, 0], atributos[:, 1], y, color='#173e68',
               s=35, depthshade=False, label='Casas observadas')
    tamanho, quartos = np.meshgrid(
        np.linspace(atributos[:, 0].min(), atributos[:, 0].max(), 30),
        np.linspace(atributos[:, 1].min(), atributos[:, 1].max(), 20))
    plano = beta[0] + beta[1] * tamanho + beta[2] * quartos
    ax.plot_surface(tamanho, quartos, plano, color='#e8a14d', alpha=.35)
    ax.set(xlabel='Tamanho da casa', ylabel='Número de quartos',
           zlabel='Preço (mil unidades monetárias)')
    ax.zaxis.set_major_formatter(preco_tick)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_title('Regressão linear múltipla\n'
                 f'Preço = {beta[0]:.2f} + {beta[1]:.2f} × tamanho {beta[2]:+.2f} × quartos\n'
                 f'r(tamanho, preço) = {rs[0]:.4f}; r(quartos, preço) = {rs[1]:.4f}', pad=22)
    ax.view_init(elev=22, azim=-55)
    ax.legend(loc='upper left')
    fig3d.subplots_adjust(left=.02, right=.9, bottom=.08, top=.85)
    fig3d.savefig(saida / 'regressao_multipla_3d.png', dpi=160)

    # h) Alterar somente o número de quartos, mantendo tamanho = 1650.
    quantidade = np.arange(1, 6)
    cenarios_X = np.column_stack([np.ones(5), np.full(5, 1650), quantidade])
    cenarios = pd.DataFrame({'tamanho': 1650, 'quartos': quantidade,
                             'preco_previsto': cenarios_X @ beta})
    previsao = np.array([1, 1650, 3]) @ beta

    # i) sklearn adiciona o intercepto: fornecer somente os dois atributos.
    modelo = LinearRegression().fit(atributos, y)
    beta_sklearn = np.r_[modelo.intercept_, modelo.coef_]
    comparacao = pd.DataFrame({'equacao_normal': beta, 'sklearn': beta_sklearn},
                              index=['beta0', 'beta1_tamanho', 'beta2_quartos'])
    comparacao['diferenca_absoluta'] = np.abs(beta - beta_sklearn)
    np.testing.assert_allclose(beta, beta_sklearn, rtol=1e-8, atol=1e-6)
    np.testing.assert_allclose(X @ beta, modelo.predict(atributos), rtol=1e-8, atol=1e-6)

    texto = '\n'.join([
        '# Fase 2 — Resultados e interpretação',
        f'\nFonte: data.csv fornecido na atividade. {len(dados)} casas, sem exclusões.',
        'O enunciado não informa a unidade de tamanho nem a moeda; foram mantidas as unidades originais.',
        '\n## b) Estatística descritiva\n',
        '```\n' + resumo.to_string() + '\n```',
        f'Preço médio: {dados.preco.mean():.2f}.',
        'Casa(s) de menor tamanho:\n```\n' + menores.to_string(index=False) + '\n```',
        'Casa(s) mais cara(s):\n```\n' + caras.to_string(index=False) + '\n```',
        '\n## c) Matrizes',
        f'X tem dimensão {X.shape}: colunas [1, tamanho, quartos]. y tem {len(y)} preços.',
        '\n## d–g) Correlações e regressão',
        f'r(tamanho, preço) = {rs[0]:.6f}; r(quartos, preço) = {rs[1]:.6f}.',
        f'Preço previsto = {beta[0]:.6f} + {beta[1]:.6f} × tamanho {beta[2]:+.6f} × quartos.',
        'O plano é contínuo para visualização; o número de quartos observado é inteiro.',
        'As correlações exibidas são bivariadas, não correlações parciais.',
        '\n## h) Previsão e alteração de quartos',
        f'Para tamanho 1650 e 3 quartos: {previsao:.6f}. Com o CSV, o arredondamento inteiro é {previsao:.0f}.',
        'Na conferência dos anexos, os preços das linhas 8, 11, 13 e 19 do CSV diferem dos do MAT em até 2 unidades. '
        'O MAT gera 293081.464335, que arredonda para 293081, valor do enunciado. '
        'Esta implementação usa o CSV, uma das opções permitidas, sem alterar os valores.',
        '```\n' + cenarios.to_string(index=False) + '\n```',
        f'Mantendo o tamanho fixo, cada quarto adicional altera a previsão em {beta[2]:.2f}.',
        'O coeficiente negativo de quartos descreve uma associação condicional nesta amostra. '
        'A correlação simples positiva também incorpora a associação entre tamanho e quartos. '
        'No ajuste múltiplo, o efeito do tamanho é considerado separadamente. '
        'Isso não demonstra que adicionar um quarto cause queda no preço. '
        'Mais quartos em uma mesma área podem representar ambientes menores, mas os dados não comprovam essa explicação.',
        'Os cenários são uma análise do modelo; nem toda combinação precisa existir na amostra.',
        '\n## i) Comparação com scikit-learn',
        '```\n' + comparacao.to_string() + '\n```',
        f'Previsão sklearn (1650, 3): {modelo.predict([[1650, 3]])[0]:.6f}.',
        'Coeficientes e previsões conferidos com assert_allclose. As pequenas diferenças são numéricas.',
        'O ajuste usa toda a base, como solicitado. A comparação valida a implementação, não a capacidade de prever casas fora da amostra.',
    ])
    (saida / 'respostas.md').write_text(texto, encoding='utf-8')
    print(texto)
    if mostrar:
        plt.show()  # janela com rotação do gráfico 3D pelo mouse
    else:
        plt.close('all')
    return dados, beta, comparacao, cenarios


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dados', help='Caminho de outro CSV no mesmo formato')
    parser.add_argument('--sem-janela', action='store_true')
    args = parser.parse_args()
    main(args.dados, mostrar=not args.sem_janela)
