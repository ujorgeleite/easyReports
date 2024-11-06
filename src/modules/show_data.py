from dash import Dash, html, dash_table
import plotly.express as px

class ShowData:
    
    def __init__(self, dataFrame):
        self.df = dataFrame
        self.dash = Dash()
        
    
    def show_basic_dashboard(self):
        
        try:
          
           self.dash.layout = [
                html.H1(children='Dados da planilha', style={'textAlign':'center'}),
                dash_table.DataTable(data=self.df.to_dict('records'), page_size=10)
            ]
           self.dash.run(debug=True)
          
            
        except Exception as ex:
            print("Error trying to generate dashboard {}", ex)