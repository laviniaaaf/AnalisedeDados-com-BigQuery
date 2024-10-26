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

label_encoder = LabelEncoder()
df['Estado'] = label_encoder.fit_transform(df['Estado'])

X = df[['Ano', 'Estado']]
y = df['Número']

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y, 
                                                    test_size=0.2, 
                                                    random_state=42)

modelo_regressao = LinearRegression()
modelo_regressao.fit(X_train, y_train)

y_pred_regressao = modelo_regressao.predict(X_test)

mae_regressao = mean_absolute_error(y_test, y_pred_regressao)
rmse_regressao = np.sqrt(mean_squared_error(y_test, y_pred_regressao))

print("Regressão Linear - Mean Absolute Error:", mae_regressao, "\nRMSE:", rmse_regressao)

ano_novo = 2024
estado_novo = 'Acre'
estado_novo_codificado = label_encoder.transform([estado_novo])[0]
X_novo = scaler.transform([[ano_novo, estado_novo_codificado]])
previsao = modelo_regressao.predict(X_novo)

print(f"Previsão do número de incêndios em {estado_novo} para o ano {ano_novo}: {previsao[0]}.")
