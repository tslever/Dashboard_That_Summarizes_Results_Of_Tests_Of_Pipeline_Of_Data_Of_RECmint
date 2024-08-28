from dash import dcc
from dashboard.Loader import loader
import numpy as np
import plotly.express as px


list_of_values_in_column_STT1_Revenue_of_table_Generators_of_AirTable = \
    loader.list_values_in_column_of_table_Generators_of_AirTable(name_of_column = "STT1 Revenue")

histogram_of_frequency_of_STT1_Revenue_vs_Revenue_per_table_Generators_of_AirTable = px.histogram(
    np.array(list_of_values_in_column_STT1_Revenue_of_table_Generators_of_AirTable),
    nbins = 100,
    labels = {"value": "STT1 Revenue"},
    title = "Histogram Of Frequency Of STT1 Revenue Vs. Revenue<br>Per Table Generators Of Database AirTable"
)
histogram_of_frequency_of_STT1_Revenue_vs_Revenue_per_table_Generators_of_AirTable.update_layout(
    xaxis_title = "STT1 Revenue",
    title_x = 0.5,
    yaxis_title = "Frequency Of STT1 Revenue",
    showlegend = False
)

graph_of_frequency_of_STT1_Revenue_vs_Revenue_per_table_Generators_of_AirTable = dcc.Graph(
    id = f"Histogram Of Frequency Of MS Vs. MS Per Table Generators Of AirTable",
    figure = histogram_of_frequency_of_STT1_Revenue_vs_Revenue_per_table_Generators_of_AirTable
)