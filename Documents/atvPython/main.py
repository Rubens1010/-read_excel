import utils
import pandas as pd

def main():
    file_path = input("Digite o caminho do arquivo Excel: ")
    try:
        document = pd.read_excel(file_path)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return

    invalid_data = []

    invalid_data.extend(utils.email_validator(document))

    invalid_data.extend(utils.row_id_validator(document))

    invalid_data.extend(utils.sales_validator(document))

    if invalid_data:
        print("Relatório de dados inválidos:")
        for item in invalid_data:
            print(f"Coordenadas: (linha: {item['row']}, coluna: {item['column']}) - Valor: {item['value']}")
    else:
        print("Nenhum dado inválido encontrado.")

    save_report = input("Deseja salvar o relatório inválido em um arquivo? (S/N): ")
    if save_report.lower() == 's':
        save_file_path = input("Digite o caminho do arquivo para salvar o relatório: ")
        with open(save_file_path, 'w') as f:
            for item in invalid_data:
                f.write(f"Coordenadas: (linha: {item['row']}, coluna: {item['column']}) - Valor: {item['value']}\n")
        print("Relatório salvo com sucesso.")

if __name__ == '__main__':
    main()
