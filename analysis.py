
import pandas as pd

def analyze_data(df):
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
    incendios_por_estado = incendios_2023.groupby('Estado')['Número'].sum()
    estado_max_incendios = incendios_por_estado.idxmax()
    max_incendios = incendios_por_estado.max()
    print(f'O estado com mais incêndios em 2023 foi {estado_max_incendios} com um total de {int(max_incendios)} incêndios.\n')

    incendios_por_estado_2023 = incendios_2023.groupby('Estado')['Número'].sum().reset_index()
    estado_menos_incendios_2023 = incendios_por_estado_2023.loc[incendios_por_estado_2023['Número'].idxmin()]
    print(f'O estado com menos incêndios em 2023 foi {estado_menos_incendios_2023["Estado"]} com um total de {int(estado_menos_incendios_2023["Número"])} incêndios.\n')

    # Ano com menos incêndios
    incendios_por_ano = df.groupby('Ano')['Número'].sum().reset_index()
    menos_incendios_ano = incendios_por_ano.loc[incendios_por_ano['Número'].idxmin()]
    print(f'O ano com menos incêndios foi {int(menos_incendios_ano["Ano"])} com um total de {int(menos_incendios_ano["Número"])} incêndios.\n')

    # Ano de 2013
    ano_2013 = df[df['Ano'] == 2013]
    incendios_2013 = ano_2013.groupby('Mês')['Número'].sum().reset_index()
    mes_max_incendios = incendios_2013.loc[incendios_2013['Número'].idxmax()]
    mes_min_incendios = incendios_2013.loc[incendios_2013['Número'].idxmin()]
    print(f'O mês com mais incêndios em 2013 foi {mes_max_incendios["Mês"]} com um total de {int(mes_max_incendios["Número"])} incêndios.\n')
    print(f'O mês com menos incêndios em 2013 foi {mes_min_incendios["Mês"]} com um total de {int(mes_min_incendios["Número"])} incêndios.\n')

    incendios_por_estado_2013 = ano_2013.groupby('Estado')['Número'].sum().reset_index()
    estado_menos_incendios_2013 = incendios_por_estado_2013.loc[incendios_por_estado_2013['Número'].idxmin()]
    print(f'O estado com menos incêndios em 2013 foi {estado_menos_incendios_2013["Estado"]} com um total de {int(estado_menos_incendios_2013["Número"])} incêndios.\n')

if __name__ == "__main__":
    df = pd.read_csv('Incendios.csv', sep=';')
    df.columns = ['Ano', 'Estado', 'Mês', 'Número']
    analyze_data(df)
