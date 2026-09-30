# 🍎 Modelo Preditivo com Machine Learning

Material de apoio da aula **“Como construir um modelo preditivo utilizando Machine Learning”**.

Neste projeto utilizamos **Python, Pandas e Scikit-learn** para criar um modelo de **Árvore de Decisão** capaz de classificar frutas a partir de suas características.

## 📁 Estrutura

```text
modelo-preditivo-machine-learning/
├── data/
│   └── dados_frutas.xlsx
├── frutas.py
└── README.md
```

## 🛠️ Tecnologias

* Python
* Pandas
* Scikit-learn
* Matplotlib
* Jupyter
* Anaconda

## 🐍 Instalação

Recomenda-se utilizar o **Anaconda**, que facilita a instalação e o gerenciamento do ambiente Python.

Após instalar, clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
cd modelo-preditivo-machine-learning
```

Instale as bibliotecas necessárias (caso você não utilize Anaconda):

```bash
pip install pandas scikit-learn matplotlib openpyxl jupyter
```

## 💻 Executando no VS Code

Instale no VS Code as extensões:

* **Python** — Microsoft
* **Jupyter** — Microsoft

No arquivo Python, utilizamos `# %%` para separar o código em células:

```python
# %%
import pandas as pd

df = pd.read_excel("data/dados_frutas.xlsx")
```

O VS Code exibirá a opção **Run Cell**, permitindo executar cada bloco individualmente, de forma semelhante a um Jupyter Notebook.

## 🤖 Executando o modelo

O projeto utiliza uma **Árvore de Decisão** através do Scikit-learn:

```python
from sklearn import tree

arvore = tree.DecisionTreeClassifier(random_state=42)

arvore.fit(X, y)
```

Depois do treinamento, podemos fornecer as características de uma nova fruta:

```python
arvore.predict(nova_fruta)
```

O projeto também possui um exemplo de **visualização da Árvore de Decisão** utilizando Matplotlib.

## 📚 Sobre as bibliotecas

**Pandas:** utilizada para manipulação e preparação dos dados.

**Scikit-learn:** fornece algoritmos e ferramentas para Machine Learning.

**Matplotlib:** utilizada para visualização de dados e da Árvore de Decisão.

---

> 💡 **Dica:** mantenha o arquivo `dados_frutas.xlsx` dentro da pasta `data/`, pois o código utiliza esse caminho para carregar os dados.
