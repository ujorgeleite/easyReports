# -*- coding: utf-8 -*-
from read_data import ReadData
from show_data import ShowData


# Example usage
if __name__ == "__main__":
    file_path = './planilha.xlsx' 
    sheet_name_incomes = "Plan_comercial"
    sheet_name_expenses = "Despesas"
    columns_to_select_incomes = ['UF', 'VALOR FECHADO', 'DATA']
    columns_to_select_expenses = ['Valor', 'Referência']# Ensure 'pagamento' is included

    # Define date range for filtering
    start_date = '2024-01-01'  # Example start date
    end_date = '2024-12-31'    # Example end date

    readData = ReadData(file_path)
    

    # Get income and expense data filtered by date
    incomes = readData.read_and_select_columns(sheet_name_incomes, columns_to_select_incomes)
    expenses = readData.read_and_select_columns(sheet_name_expenses, columns_to_select_expenses)

    if incomes is not None:
        print("Receitas:\n", incomes)
    if expenses is not None:
        print("Despesas:\n", expenses)
