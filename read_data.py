# -*- coding: utf-8 -*-

import pandas as pd
class ReadData:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_and_select_columns(self, sheet_name, columns, start_date=None, end_date=None):
        try:
            # Load the Excel sheet
            df = pd.read_excel(self.file_path, sheet_name=sheet_name)
            
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
            print("Error: The file {} does not exist.".format(self.file_path))
        except KeyError as e:
            print("Error: Column {} not found in the file.".format(e))
