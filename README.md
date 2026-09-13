# Regressão Linear — Fases 1 e 2

Projeto acadêmico de análise de correlação e regressão linear com Python.

## Organização

| Pasta | Conteúdo | Script principal |
|---|---|---|
| [fase1](fase1/README.md) | Correlação e regressão simples, com análise dos conjuntos e de pontos influentes | `fase1/demo.py` |
| [fase2](fase2/README.md) | Regressão múltipla para preço de casas usando tamanho e quartos | `fase2/rmdemo.py` |

Cada fase contém seu notebook e a pasta `resultados` com os gráficos. As dependências são compartilhadas no `requirements.txt` da raiz.

## Executar no Windows

Com Python instalado, abra o terminal na raiz do repositório:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe fase1\demo.py
.\.venv\Scripts\python.exe fase2\rmdemo.py
```

Se já houver um ambiente Python configurado, utilize seu executável. O comando global `python` precisa apontar para uma instalação real, e não para o atalho da Microsoft Store.

Acrescente `--sem-janela` para salvar os gráficos sem abrir janelas. Os scripts encontram seus dados e salvam os resultados em suas próprias pastas.

Para os notebooks, abra a pasta da fase correspondente no Jupyter e utilize um kernel com as dependências instaladas. Jupyter não é necessário para executar os scripts.

## Dados e validação

A fase 1 preserva os vetores do notebook enviado originalmente. O quinto conjunto é uma comparação sem o possível outlier do conjunto 4. A fase 2 preserva o CSV fornecido na atividade. Não são compartilhados ambientes Python, credenciais ou arquivos temporários.

Os coeficientes da fase 1 foram conferidos com NumPy. Na fase 2, coeficientes e previsões foram comparados com scikit-learn. Consulte os documentos de cada fase para as interpretações e limitações.
