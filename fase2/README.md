# Regressão Linear Múltipla — Fase 2

Análise de 47 casas usando tamanho e número de quartos para prever o preço.

## Executar no Windows

Com Python instalado, abra um terminal na raiz do repositório:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe fase2\rmdemo.py
```

Para salvar os resultados sem abrir gráficos, acrescente `--sem-janela`.

## Arquivos

- `regmultipla.py`: cálculo dos coeficientes pela equação normal, usando `numpy.linalg.solve`.
- `rmdemo.py`: análise descritiva, regressões simples e múltipla, gráficos e comparação com scikit-learn.
- `fase2.ipynb`: alternativa para uso em Jupyter, que requer um ambiente Jupyter instalado.
- `data.csv`: dados fornecidos na atividade, sem cabeçalho.
- `resultados/`: gráficos e respostas gerados pelo script.

O gráfico 3D apresenta o plano ajustado e pode ser girado na janela do Matplotlib.

## Resultado de referência

Para tamanho 1650 e 3 quartos, o CSV produz 293081,566874. O arquivo MAT fornecido na atividade produz 293081,464335, que arredonda para 293081. Foram identificadas diferenças de até 2 unidades em quatro preços entre os anexos. O projeto preserva os valores do CSV.

Os coeficientes e previsões foram comparados com `LinearRegression` do scikit-learn. O ajuste utiliza a base completa, conforme a atividade; essa comparação verifica a implementação, não o desempenho em dados novos.

Tamanho e preço permanecem nas unidades originais, não especificadas no enunciado.
