# -*- coding: utf-8 -*-
import pandas as pd

def read_and_select_columns(file_path, sheet_name, columns, start_date=None, end_date=None):
    try:
        # Load the Excel sheet
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        
        # Convert the 'pagamento' column to datetime format (replace with your actual date column name)
        df['Pagamento'] = pd.to_datetime(df['Pagamento'], errors='coerce')

        # Filter by date range if specified
        if start_date is not None:
            df = df[df['Pagamento'] >= pd.to_datetime(start_date)]
        if end_date is not None:
            df = df[df['Pagamento'] <= pd.to_datetime(end_date)]

        # Group and sum the selected data
        selected_data = df[columns].groupby("Região")["Pago"].sum()
        
        return selected_data
    except FileNotFoundError:
        print("Error: The file {} does not exist.".format(file_path))
    except KeyError as e:
        print("Error: Column {} not found in the file.".format(e))

# Example usage
if __name__ == "__main__":
    file_path = './planilha.xlsx' 
    sheet_name_incomes = "Receitas_ate_set"
    sheet_name_expenses = "Despesas_ate_set"
    columns_to_select = ['Região', 'UF', 'Pago', 'Pagamento']  # Ensure 'pagamento' is included

    # Define date range for filtering
    start_date = '2024-01-01'  # Example start date
    end_date = '2024-12-31'    # Example end date

    # Get income and expense data filtered by date
    incomes = read_and_select_columns(file_path, sheet_name_incomes, columns_to_select, start_date, end_date)
    expenses = read_and_select_columns(file_path, sheet_name_expenses, columns_to_select, start_date, end_date)

    if incomes is not None:
        print("Receitas:\n", incomes)
    if expenses is not None:
        print("Despesas:\n", expenses)
