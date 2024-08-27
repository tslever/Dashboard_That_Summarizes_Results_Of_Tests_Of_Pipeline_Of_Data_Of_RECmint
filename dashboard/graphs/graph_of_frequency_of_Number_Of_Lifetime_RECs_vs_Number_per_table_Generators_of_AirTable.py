from dash import dcc
from dashboard.Loader import loader
import numpy as np
import plotly.express as px


list_of_values_in_column_Lifetime_RECs_of_table_Generators_of_AirTable = \
    loader.list_values_in_column_of_table_Generators_of_AirTable(name_of_column = "Lifetime RECs")

histogram_of_frequency_of_Number_Of_Lifetime_RECs_vs_Log_Of_Number_per_table_Generators_of_AirTable = px.histogram(
    np.log(np.array(list_of_values_in_column_Lifetime_RECs_of_table_Generators_of_AirTable) + 1),
    nbins = 100,
    labels = {"value": "Log Of Number Of Lifetime RECs"},
    title = "Histogram Of Frequency Of Number Of Lifetime RECs Vs. Log Of Number<br>Per Table Generators Of Database AirTable"
)
histogram_of_frequency_of_Number_Of_Lifetime_RECs_vs_Log_Of_Number_per_table_Generators_of_AirTable.update_layout(
    xaxis_title = "Log Of Number Of Lifetime RECs",
    title_x = 0.5,
    yaxis_title = "Frequency Of Numbers Of Lifetime RECs",
    showlegend = False
)

graph_of_frequency_of_Number_Of_Lifetime_RECs_vs_Number_per_table_Generators_of_AirTable = dcc.Graph(
    id = f"Histogram Of Frequency Of Number Of Lifetime RECs Vs. Log Of Number Per Table Generators Of AirTable",
    figure = histogram_of_frequency_of_Number_Of_Lifetime_RECs_vs_Log_Of_Number_per_table_Generators_of_AirTable
)