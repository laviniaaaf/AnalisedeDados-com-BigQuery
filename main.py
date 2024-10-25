import pandas as pd

def load_data(file_path):
    with open(file_path, 'r') as file:
        df = pd.read_csv(file, sep=';')
    return df

def preprocess_data(df):
    df.columns = ['Ano', 'Estado', 'Mês', 'Número']

    # Modificações no DF
    df['Mês'] = df['Mês'].replace('MarÃ§o', 'Março')
    df['Estado'] = df['Estado'].replace('CearÃ¡', 'Ceará')
    df['Estado'] = df['Estado'].replace('MaranhÃ£o', 'Maranhão')
    df['Estado'] = df['Estado'].replace('ParÃ¡', 'Pará')
    df['Estado'] = df['Estado'].replace('ParanÃ¡', 'Paraná')
    df['Estado'] = df['Estado'].replace('SÃ£o Paulo', 'São Paulo')
    
    return df

def main():
    df = load_data('Incendios.csv')
    df = preprocess_data(df)

    estados = df['Estado'].unique()
    print(estados, '\n')

    mes = df['Mês'].unique()
    print(mes)

    # Contagem de valores nulos
    nulos = df.isnull().sum()
    print("\nValores nulos:\n", nulos)

    titulo = "\nIncêndios no Brasil (por Ano, Estado, Mês e Número).\n"
    print(titulo)
    print(df)

if __name__ == "__main__":
    main()
