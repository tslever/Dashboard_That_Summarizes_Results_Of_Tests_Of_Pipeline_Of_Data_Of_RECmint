from dash import dcc
from dashboard.Loader import loader
import numpy as np
import plotly.express as px


list_of_values_in_column_Average_Cost_Per_REC_of_table_Generators_of_AirTable = \
    loader.list_values_in_column_of_table_Generators_of_AirTable(name_of_column = "Average Cost/REC")

histogram_of_frequency_of_Average_Cost_Per_REC_vs_Cost_per_table_Generators_of_AirTable = px.histogram(
    np.log(np.array(list_of_values_in_column_Average_Cost_Per_REC_of_table_Generators_of_AirTable) + 1),
    nbins = 100,
    labels = {"value": "Average Cost Per REC"},
    title = "Histogram Of Frequency Of Average Cost Per REC Vs. Cost<br>Per Table Generators Of Database AirTable"
)
histogram_of_frequency_of_Average_Cost_Per_REC_vs_Cost_per_table_Generators_of_AirTable.update_layout(
    xaxis_title = "Values Of Column Average Cost Per REC",
    title_x = 0.5,
    yaxis_title = "Frequency Of Values Of Column Average Cost Per REC",
    showlegend = False
)

graph_of_frequency_of_Average_Cost_Per_REC_vs_Cost_per_table_Generators_of_AirTable = dcc.Graph(
    id = f"Histogram Of Frequency Of Average Cost Per REC Vs. Cost Per Table Generators Of AirTable",
    figure = histogram_of_frequency_of_Average_Cost_Per_REC_vs_Cost_per_table_Generators_of_AirTable
)