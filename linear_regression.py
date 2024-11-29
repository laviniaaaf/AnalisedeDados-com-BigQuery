import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import LabelEncoder, StandardScaler

with open('Incendios.csv', 'r') as file:
    df = pd.read_csv(file, sep=';')

df.columns = ['Ano', 'Estado', 'Mês', 'Número']

df['Estado'] = df['Estado'].astype(str)
df['Estado'] = df['Estado'].replace('ParÃ¡', 'Pará')

label_encoder = LabelEncoder()
df['Estado'] = label_encoder.fit_transform(df['Estado'])

df['Media_dos_anos_anteriores'] = df.groupby('Estado')['Número'].transform(lambda x: x.shift().expanding().mean())
df = df.dropna(subset = ['Media_dos_anos_anteriores'])

X = df[['Ano', 'Estado', 'Media_dos_anos_anteriores']]
y = df['Número']

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y, 
                                                    test_size = 0.2, 
                                                    random_state = 42)

modelo_regressao = LinearRegression()
modelo_regressao.fit(X_train, y_train)

y_pred_regressao = modelo_regressao.predict(X_test)

mae_regressao = mean_absolute_error(y_test, y_pred_regressao)
mse_regressao = mean_squared_error(y_test, y_pred_regressao)
rmse_regressao = np.sqrt(mean_squared_error(y_test, y_pred_regressao))

print("Regressão Linear - MAE:", int(mae_regressao), "\nRMSE:", int(rmse_regressao))
print("MSE:", int(mse_regressao), ".\n")

ano = 2024
estados = ['Acre', 'Pará', 'Distrito Federal', 'Bahia']

for estado in estados:
    estado_codificado = label_encoder.transform([estado])[0]

    media_anos_anteriores = df[(df['Ano'] < ano) & (df['Estado'] == estado_codificado)]['Número'].mean()
    
    if np.isnan(media_anos_anteriores):
        print(f"Dados insuficientes para calcular média histórica para {estado}.")
        continue

    novo = np.array([[ano, estado_codificado, media_anos_anteriores]])
    novo = scaler.transform(novo)
    previsao = modelo_regressao.predict(novo)
    
    print(f"Previsão do número de incêndios em {estado} para o ano {ano}: {int(previsao[0])}.")
