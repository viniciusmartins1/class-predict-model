# %%

import pandas as pd
df = pd.read_excel("data/dados_frutas.xlsx")
df = pd.get_dummies(df, columns=["Cor"], dtype=int)
df

from sklearn import tree
arvore = tree.DecisionTreeClassifier(random_state=42)

caracteristicas = ["Arredondada", 
                   "Acida", 
                   "Doce", 
                   "Cor_Amarela", 
                   "Cor_Laranja", 
                   "Cor_Verde", 
                   "Cor_Vermelha", 
                   "Tamanho"
                  ]

X = df[caracteristicas]
X = X.replace({
  "pequena": 1, "media": 2, "grande": 3
})
y = df['Fruta']

# ISSO AQUI É MACHINE LEARNING
arvore.fit(X, y)


#%%

nova_fruta = pd.DataFrame([{
    "Arredondada": 1,
    "Acida": 0,
    "Doce": 1,
    "Cor_Amarela": 0,
    "Cor_Laranja": 1,
    "Cor_Verde": 0,
    "Cor_Vermelha": 0,
    "Tamanho": 3
}])

arvore.predict(nova_fruta)

# %%

# Árvore de Decisão - Visualmente
import matplotlib.pyplot as plt

plt.figure(dpi=400)

tree.plot_tree(arvore, 
               feature_names=caracteristicas, 
               class_names=arvore.classes_, 
               filled=True)
