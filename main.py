# -*- coding: utf-8 -*-
from src.modules.read_data import ReadData
from src.modules.show_data import ShowData


# Example usage
if __name__ == "__main__":
    # file_path = 'https://docs.google.com/spreadsheets/d/11GDoU19HzAqSE1pWMIqjXr6E-qvAP7Ni/edit?usp=drive_link&ouid=105427989285473046763&rtpof=true&sd=true'
    file_path = "planilha.xlsx"
    sheet_name_incomes = "Receitas_ate_set"
    sheet_name_expenses = "Despesas_ate_set"
    columns_to_select_incomes = ["UF", "Pago"]
    columns_to_select_expenses = [
        "UF",
        "Valor",
    ]  # Ensure 'pagamento' is included

    # Define date range for filtering
    start_date = "2024-01-01"  # Example start date
    end_date = "2024-12-31"  # Example end date

    readData = ReadData(file_path)

 
    incomes = readData.read_and_select_columns(
        sheet_name_incomes, columns_to_select_incomes
    )
    expenses = readData.read_and_select_columns(
        sheet_name_expenses, columns_to_select_expenses
    )
    
    incomes = incomes.rename(columns = {"UF":"Estado","Pago":"Receita"})
    expenses = expenses.rename(columns = {"UF":"Estado","Valor":"Despesa"})

    # if incomes is not None:
    #     print("Receitas:\n", incomes)
    #     print("Receitas agrupado:\n", readData.group_by(incomes,"UF"))
    # if expenses is not None:
    #     print("Despesas:\n", expenses)
        
    incomes_grouped = incomes.groupby("Estado", as_index=False).sum()
    expenses_grouped = expenses.groupby("Estado", as_index=False).sum()
    merged_df = readData.merge_data_frames(incomes_grouped,expenses_grouped,["Estado"])
    
    print(merged_df)
