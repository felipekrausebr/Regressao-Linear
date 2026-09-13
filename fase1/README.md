# Fase 1 — Correlação e regressão linear simples

Execute `python demo.py` nesta pasta. Para apenas salvar: `python demo.py --sem-janela`.

Os dados foram recuperados do notebook fornecido pelo aluno. O arquivo original datasetFase1.txt não foi fornecido; os vetores estão preservados em demo.py. Os conflitos de Git do notebook foram resolvidos usando a versão que contém os quatro conjuntos e o cálculo completo da regressão.

- `funcoes.py`: funções correlacao(x, y) e regressao(x, y). A segunda retorna beta1 e beta0, nessa ordem, preservando a convenção do código original.
- `demo.py`: cinco gráficos, com os quatro conjuntos e o experimento sem o possível outlier do conjunto 4.
- `fase1.ipynb`: versão para Jupyter, mantendo os arquivos juntos.
- `resultados/regressoes.png`: gráfico gerado pela execução.

## Interpretação

O conjunto 2 apresenta um padrão curvo, inadequado para um ajuste por reta. Uma correlação positiva não garante que a forma da relação seja linear.

No conjunto 3, dez observações têm x=8 e uma tem x=19. A inclinação é muito influenciada por esse único ponto; o resultado exige cautela. Removê-lo deixa x constante e impede estimar a inclinação por essa fórmula.

No conjunto 4, o ponto (13, 12.74) se afasta da tendência dos demais. Antes de ajustar, deve-se investigar sua origem e influência. O conjunto 5 ilustra o resultado sem ele, mas removê-lo definitivamente exige justificativa; um valor extremo pode ser uma observação válida.

No código recuperado, a ordem dos dados e a convenção de retorno da regressão simples foram preservadas. Na fase 2, a função de regressão simples retorna beta0 e beta1; cada script usa corretamente sua própria convenção.
