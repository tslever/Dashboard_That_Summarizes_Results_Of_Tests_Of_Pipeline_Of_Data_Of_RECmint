from dash import dcc
from dashboard.Loader import loader
import numpy as np
import plotly.express as px


list_of_values_in_column_MS_of_table_Generators_of_AirTable = \
    loader.list_values_in_column_of_table_Generators_of_AirTable(name_of_column = "M&S - Fee%")

histogram_of_frequency_of_MS_vs_MS_per_table_Generators_of_AirTable = px.histogram(
    np.array(list_of_values_in_column_MS_of_table_Generators_of_AirTable),
    nbins = 100,
    labels = {"value": "MS"},
    title = "Histogram Of Frequency Of MS Vs. MS<br>Per Table Generators Of Database AirTable"
)
histogram_of_frequency_of_MS_vs_MS_per_table_Generators_of_AirTable.update_layout(
    xaxis_title = "MS",
    title_x = 0.5,
    yaxis_title = "Frequency Of MS",
    showlegend = False
)

graph_of_frequency_of_MS_vs_MS_per_table_Generators_of_AirTable = dcc.Graph(
    id = f"Histogram Of Frequency Of MS Vs. MS Per Table Generators Of AirTable",
    figure = histogram_of_frequency_of_MS_vs_MS_per_table_Generators_of_AirTable
)