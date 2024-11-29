import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

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
                                                    test_size = 0.2, 
                                                    random_state = 42)

modelo_forest = RandomForestRegressor(random_state = 42)

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['auto', 'sqrt', 'log2']
}

grid_search = GridSearchCV(estimator = modelo_forest, 
                           param_grid = param_grid, 
                           cv = 3, 
                           n_jobs = -1, 
                           scoring = 'neg_mean_absolute_error',  
                           verbose = 2)

grid_search.fit(X_train,
                 y_train)

best_model = grid_search.best_estimator_

y_pred = best_model.predict(X_test)
mae_forest = mean_absolute_error(y_test, y_pred)
rmse_forest = np.sqrt(mean_squared_error(y_test, y_pred))

print("Melhores hiperparâmetros: \n", grid_search.best_params_)
print("Random Forest otimizado - Mean Absolute Error:", mae_forest)
print("Random Forest otimizado - RMSE:", rmse_forest)


