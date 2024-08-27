from dash import dcc
from dashboard.Loader import loader
import numpy as np
import plotly.express as px


list_of_values_in_column_Nameplate_of_table_Generators_of_AirTable = \
    loader.list_values_in_column_of_table_Generators_of_AirTable(name_of_column = "Nameplate (kW DC)")

histogram_of_frequency_of_Nameplate_vs_Nameplate_per_table_Generators_of_AirTable = px.histogram(
    np.log(np.array(list_of_values_in_column_Nameplate_of_table_Generators_of_AirTable) + 1),
    nbins = 100,
    labels = {"value": "Log Of Values In Column Nameplate"},
    title = "Histogram Of Frequency Of Nameplate Vs. Log Of Nameplate<br>Per Table Generators Of Database AirTable"
)
histogram_of_frequency_of_Nameplate_vs_Nameplate_per_table_Generators_of_AirTable.update_layout(
    xaxis_title = "Log Of Values In Column Nameplate",
    title_x = 0.5,
    yaxis_title = "Frequency Of Values In Column Nameplate",
    showlegend = False
)

graph_of_frequency_of_Nameplate_vs_Nameplate_per_table_Generators_of_AirTable = dcc.Graph(
    id = f"Histogram Of Frequency Of Nameplate Vs. Nameplate Per Table Generators Of AirTable",
    figure = histogram_of_frequency_of_Nameplate_vs_Nameplate_per_table_Generators_of_AirTable
)