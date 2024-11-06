# -*- coding: utf-8 -*-

import pandas as pd
class ReadData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.start_date = '2024-01-01'
        self.end_date = '2024-12-31'
        
    def filter_by_date_range(self,df,column_date):
        # Convert the 'pagamento' column to datetime format (replace with your actual date column name)
        df['DATA'] = pd.to_datetime(df[column_date], errors='coerce')

        # Filter by date range if specified
        if self.start_date is not None:
            df = df[df[column_date] >= pd.to_datetime(self.start_date)]
        if self.end_date is not None:
            df = df[df[column_date] <= pd.to_datetime(self.end_date)]
            
        return df

    def read_and_select_columns(self, sheet_name, columns):
        try:
            
            # Load the Excel sheet
            df = pd.read_excel(self.file_path, sheet_name=sheet_name)

            # Group and sum the selected data
            selected_data = df[columns]
            
            return selected_data
        except FileNotFoundError:
            print("Error: The file {} does not exist.".format(self.file_path))
        except KeyError as e:
            print("Error: Column {} not found in the file.".format(e))
            
    def merge_data_frames(self,df1,df2, aggregator):
        return pd.merge(df1, df2, on=aggregator, how='inner')
    
    def group_by(self,data_frame,columns):
        print(data_frame)
        print(columns)
        return data_frame.groupby([columns]).agg(
            {columns: ['sum', 'count','count']}
        )
