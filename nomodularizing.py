import pandas as pd
import matplotlib.pyplot as plt

with open('Incendios.csv', 'r') as file:
    df = pd.read_csv(file, sep=';')

df.columns = ['Ano', 'Estado', 'Mês', 'Número']

# Todos os estados presentes no df
estados = df['Estado'].unique()
print(estados, '\n')

# Todos os meses presentes no df
mes = df['Mês'].unique()
print(mes)

# Modificações no DF
df['Mês'] = df['Mês'].replace('MarÃ§o', 'Março')

df['Estado'] = df['Estado'].replace('CearÃ¡', 'Ceará')
df['Estado'] = df['Estado'].replace('MaranhÃ£o', 'Maranhão')
df['Estado'] = df['Estado'].replace('ParÃ¡', 'Pará')
df['Estado'] = df['Estado'].replace('ParanÃ¡', 'Paraná')
df['Estado'] = df['Estado'].replace('SÃ£o Paulo', 'São Paulo')

# Contagem de valores nulos
nulos = df.isnull().sum()
print("\nValores nulos:\n", nulos)

titulo = "\nIncêndios no Brasil (por Ano, Estado, Mês e Número).\n"

print(titulo)
print(df)

# Analise Exploratoria

# Total de Incendios por ano
total_incendios_por_ano = df.groupby('Ano')['Número'].sum()
ano_com_mais_incendios = total_incendios_por_ano.idxmax()
max_incendios = total_incendios_por_ano.max()

print(f"\nO ano com mais incêndios foi {ano_com_mais_incendios} com um total de {int(max_incendios)} incêndios.\n")

# Total de Incendios por mês (no ano de 2023)
total_incendios_por_mes = df.groupby('Mês')['Número'].sum()
mes_com_mais_incendios = total_incendios_por_mes.idxmax()
m_incendios = total_incendios_por_mes.max()

print(f"O mês de 2023 com mais incêndios foi {mes_com_mais_incendios} com um total de {int(m_incendios)} incêndios.\n")

# Incendios por estado (ano de 2023)
incendios_2023 = df[df['Ano'] == 2023]
#print(incendios_2023)

incendios_por_estado = incendios_2023.groupby('Estado')['Número'].sum()
estado_max_incendios = incendios_por_estado.idxmax()
max_incendios = incendios_por_estado.max()

print(f'O estado com mais incêndios em 2023 foi {estado_max_incendios} com um total de {int(max_incendios)} incêndios.\n')


# Ano com menos incendios
incendios_por_ano = df.groupby('Ano')['Número'].sum().reset_index()
menos_incendios_ano = incendios_por_ano.loc[incendios_por_ano['Número'].idxmin()]

print(f'O ano com menos incêndios foi {int(menos_incendios_ano["Ano"])} com um total de {int(menos_incendios_ano["Número"])} incêndios.\n')

# Ano com menos incendios:
ano_2013 = df[df['Ano'] == 2013]

incendios_2013 = ano_2013 .groupby('Mês')['Número'].sum().reset_index()
mes_max_incendios = incendios_2013.loc[incendios_2013['Número'].idxmax()]
mes_min_incendios = incendios_2013.loc[incendios_2013['Número'].idxmin()]

print(f'O mês com mais incêndios em 2013 foi {mes_max_incendios["Mês"]} com um total de {int(mes_max_incendios["Número"])} incêndios.\n')
print(f'O mês com menos incêndios em 2013 foi {mes_min_incendios["Mês"]} com um total de {int(mes_min_incendios["Número"])} incêndios.\n')


#############################
incendios_por_mes = incendios_2023.groupby('Mês')['Número'].sum().reindex([
    'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
])

plt.figure(figsize=(10, 5))
plt.bar(incendios_por_ano['Ano'], incendios_por_ano['Número'], color='orange')
plt.axhline(y=menos_incendios_ano['Número'], color='red', linestyle='--', label='Ano com menos incêndios')
plt.title('Total de Incêndios por ano')
plt.xlabel('Ano')
plt.ylabel('Número de Incêndios')
plt.legend()
plt.xticks(rotation = 45)
plt.tight_layout()

plt.figure(figsize=(10, 5))
plt.bar(incendios_2013['Mês'], incendios_2013['Número'], color='blue')
plt.title('Incêndios - 2013')
plt.xlabel('Mês')
plt.ylabel('Número de Incêndios')
plt.xticks(rotation = 45)
plt.tight_layout()

incendios_por_estado = ano_2013.groupby('Estado')['Número'].sum().reset_index()
#print("Incendios 2013 por estado", incendios_por_estado)
plt.figure(figsize=(12, 6))
plt.bar(incendios_por_estado['Estado'], incendios_por_estado['Número'], color='purple')

for index, row in incendios_por_estado.iterrows():
    plt.text(row['Estado'], row['Número'], str(int(row['Número'])), ha='center', va='bottom')

plt.title('Total de Incêndios por Estado em 2013')
plt.xlabel('Estado')
plt.ylabel('Número de Incêndios')
plt.xticks(rotation = 45)
plt.tight_layout()


plt.figure(figsize=(10, 6))
plt.bar(incendios_por_mes.index, incendios_por_mes.values, color='orange')
plt.title('Total de Incêndios em 2023')
plt.xlabel('Mês')
plt.ylabel('Número de Incêndios')
plt.xticks(rotation = 45)
plt.grid(axis = 'y')
plt.tight_layout()


incendios_por_estado = incendios_2023.groupby('Estado')['Número'].sum().reset_index()
#incendios_por_estado = incendios_por_estado.sort_values(by='Número', ascending=False)
#print("Incendios 2023 por estado", incendios_por_estado)
plt.figure(figsize=(12, 6))
plt.bar(incendios_por_estado['Estado'], incendios_por_estado['Número'], color='red')
plt.title('Total de Incêndios por Estado em 2023')
plt.xlabel('Estado')
plt.ylabel('Número de Incêndios') 
plt.xticks(rotation = 45)  

for index, row in incendios_por_estado.iterrows():
    plt.text(row['Estado'], row['Número'], str(int(row['Número'])), ha='center', va='bottom')

plt.tight_layout()  
plt.show()