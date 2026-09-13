# Fase 2 — Resultados e interpretação

Fonte: data.csv fornecido na atividade. 47 casas, sem exclusões.
O enunciado não informa a unidade de tamanho nem a moeda; foram mantidas as unidades originais.

## b) Estatística descritiva

```
           tamanho    quartos          preco
count    47.000000  47.000000      47.000000
mean   2000.680851   3.170213  340412.765957
std     794.702354   0.760982  125039.911223
min     852.000000   1.000000  169900.000000
25%    1432.000000   3.000000  249900.000000
50%    1888.000000   3.000000  299900.000000
75%    2269.000000   4.000000  384450.000000
max    4478.000000   5.000000  699900.000000
```
Preço médio: 340412.77.
Casa(s) de menor tamanho:
```
 tamanho  quartos    preco
     852        2 179900.0
```
Casa(s) mais cara(s):
```
 tamanho  quartos    preco
    4478        5 699900.0
```

## c) Matrizes
X tem dimensão (47, 3): colunas [1, tamanho, quartos]. y tem 47 preços.

## d–g) Correlações e regressão
r(tamanho, preço) = 0.854988; r(quartos, preço) = 0.442262.
Preço previsto = 89597.765961 + 139.210635 × tamanho -8737.915420 × quartos.
O plano é contínuo para visualização; o número de quartos observado é inteiro.
As correlações exibidas são bivariadas, não correlações parciais.

## h) Previsão e alteração de quartos
Para tamanho 1650 e 3 quartos: 293081.566874. Com o CSV, o arredondamento inteiro é 293082.
Na conferência dos anexos, os preços das linhas 8, 11, 13 e 19 do CSV diferem dos do MAT em até 2 unidades. O MAT gera 293081.464335, que arredonda para 293081, valor do enunciado. Esta implementação usa o CSV, uma das opções permitidas, sem alterar os valores.
```
 tamanho  quartos  preco_previsto
    1650        1   310557.397714
    1650        2   301819.482294
    1650        3   293081.566874
    1650        4   284343.651453
    1650        5   275605.736033
```
Mantendo o tamanho fixo, cada quarto adicional altera a previsão em -8737.92.
O coeficiente negativo de quartos descreve uma associação condicional nesta amostra. A correlação simples positiva também incorpora a associação entre tamanho e quartos. No ajuste múltiplo, o efeito do tamanho é considerado separadamente. Isso não demonstra que adicionar um quarto cause queda no preço. Mais quartos em uma mesma área podem representar ambientes menores, mas os dados não comprovam essa explicação.
Os cenários são uma análise do modelo; nem toda combinação precisa existir na amostra.

## i) Comparação com scikit-learn
```
               equacao_normal       sklearn  diferenca_absoluta
beta0            89597.765961  89597.765961        8.440111e-10
beta1_tamanho      139.210635    139.210635        1.421085e-13
beta2_quartos    -8737.915420  -8737.915420        3.565219e-10
```
Previsão sklearn (1650, 3): 293081.566874.
Coeficientes e previsões conferidos com assert_allclose. As pequenas diferenças são numéricas.
O ajuste usa toda a base, como solicitado. A comparação valida a implementação, não a capacidade de prever casas fora da amostra.