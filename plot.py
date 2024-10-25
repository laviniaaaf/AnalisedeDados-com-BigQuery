import pandas as pd
import matplotlib.pyplot as plt

def plot_data(df):
    # Total de incêndios por ano
    incendios_por_ano = df.groupby('Ano')['Número'].sum().reset_index()
    menos_incendios_ano = incendios_por_ano.loc[incendios_por_ano['Número'].idxmin()]

    plt.figure(figsize=(10, 5))
    plt.bar(incendios_por_ano['Ano'], incendios_por_ano['Número'], color='orange')
    plt.axhline(y=menos_incendios_ano['Número'], color='red', linestyle='--', label='Ano com menos incêndios')
    plt.title('Total de Incêndios (por ano)')
    plt.xlabel('Ano')
    plt.ylabel('Número de Incêndios')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Incêndios em 2013
    ano_2013 = df[df['Ano'] == 2013]
    incendios_2013 = ano_2013.groupby('Mês')['Número'].sum().reset_index()

    plt.figure(figsize=(10, 5))
    plt.bar(incendios_2013['Mês'], incendios_2013['Número'], color='blue')
    plt.title('Incêndios - 2013')
    plt.xlabel('Mês')
    plt.ylabel('Número de Incêndios')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Total de incêndios por estado em 2013
    incendios_por_estado = ano_2013.groupby('Estado')['Número'].sum().reset_index()
    plt.figure(figsize=(12, 6))
    plt.bar(incendios_por_estado['Estado'], incendios_por_estado['Número'], color='purple')

    for index, row in incendios_por_estado.iterrows():
        plt.text(row['Estado'], row['Número'], str(int(row['Número'])), ha='center', va='bottom')

    plt.title('Total de Incêndios por Estado em 2013')
    plt.xlabel('Estado')
    plt.ylabel('Número de Incêndios')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Total de incêndios em 2023
    incendios_2023 = df[df['Ano'] == 2023]
    incendios_por_mes = incendios_2023.groupby('Mês')['Número'].sum().reindex([
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ])

    plt.figure(figsize=(10, 6))
    plt.bar(incendios_por_mes.index, incendios_por_mes.values, color='orange')
    plt.title('Total de Incêndios em 2023')
    plt.xlabel('Mês')
    plt.ylabel('Número de Incêndios')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()

    # Total de incêndios por estado em 2023
    incendios_por_estado_2023 = incendios_2023.groupby('Estado')['Número'].sum().reset_index()
    plt.figure(figsize=(12, 6))
    plt.bar(incendios_por_estado_2023['Estado'], incendios_por_estado_2023['Número'], color='red')
    plt.title('Total de Incêndios por Estado em 2023')
    plt.xlabel('Estado')
    plt.ylabel('Número de Incêndios')
    plt.xticks(rotation=45)

    for index, row in incendios_por_estado_2023.iterrows():
        plt.text(row['Estado'], row['Número'], str(int(row['Número'])), ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv('Incendios.csv', sep=';')
    df.columns = ['Ano', 'Estado', 'Mês', 'Número']
    plot_data(df)
