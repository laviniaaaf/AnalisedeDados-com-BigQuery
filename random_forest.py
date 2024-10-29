import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

with open('Incendios.csv', 'r') as file:
    df = pd.read_csv(file, sep=';')

df.columns = ['Ano', 'Estado', 'Mês', 'Número']

df['Mês'] = df['Mês'].replace('MarÃ§o', 'Março')
df['Estado'] = df['Estado'].replace({
    'CearÃ¡': 'Ceará',
    'MaranhÃ£o': 'Maranhão',
    'ParÃ¡': 'Pará',
    'ParanÃ¡': 'Paraná',
    'SÃ£o Paulo': 'São Paulo'
})

label_encoder = LabelEncoder()
df['Estado'] = label_encoder.fit_transform(df['Estado'])
df['Mês'] = label_encoder.fit_transform(df['Mês'])

X = df[['Ano', 'Estado', 'Mês']]
y = df['Número'] # variavel dependente

X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y, 
                                                    test_size = 0.2, 
                                                    random_state = 42)

modelo_forest = RandomForestRegressor(
    max_depth = 10,
    max_features = 'sqrt',
    min_samples_leaf = 4,
    min_samples_split = 10,
    n_estimators = 100,
    random_state = 42
)

modelo_forest.fit(X_train, y_train)

y_pred = modelo_forest.predict(X_test)
mae_forest = mean_absolute_error(y_test, y_pred)
rmse_forest = np.sqrt(mean_squared_error(y_test, y_pred))
r2_forest = r2_score(y_test, y_pred)

print("Random Forest - Mean Absolute Error:\n", mae_forest)
print("Random Forest - RMSE:\n", rmse_forest)
print("Random Forest - R²:\n", r2_forest)


plt.figure(figsize = (10, 5))

# Quanto mais proximos da linha (x = y), melhor o desempenho.
plt.subplot(1, 2, 1)
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r')
plt.xlabel("Valores Reais")
plt.ylabel("Valores Preditos")
plt.title("Comparação entre Valores Reais e Valore Preditos")

plt.subplot(1, 2, 2)
sns.histplot(y_test - y_pred, 
             kde = True, 
             bins = 30)
plt.xlabel("Erro de Predição")
plt.title("Distribuição dos Erros de Predição")
# o grafico juda a verificar se os erros seguem uma distribuição próxima de zero, o que indica que o modelo está bem

plt.tight_layout()
plt.show()

