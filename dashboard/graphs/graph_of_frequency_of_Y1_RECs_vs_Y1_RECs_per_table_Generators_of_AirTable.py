from dash import dcc
from dashboard.Loader import loader
import numpy as np
import plotly.express as px


list_of_values_in_column_Y1_RECs_of_table_Generators_of_AirTable = \
    loader.list_values_in_column_of_table_Generators_of_AirTable(
        start_of_name_of_column = "Y1 RECs (calc)"
    )

histogram_of_frequency_of_Y1_RECs_vs_Y1_RECs_per_table_Generators_of_AirTable = px.histogram(
    np.log(np.array(list_of_values_in_column_Y1_RECs_of_table_Generators_of_AirTable) + 1),
    nbins = 100,
    labels = {"value": "Y1 RECs"},
    title = "Histogram Of Frequency Of Y1 RECs Vs. Y1 RECs<br>Per Table Generators Of Database AirTable"
)
histogram_of_frequency_of_Y1_RECs_vs_Y1_RECs_per_table_Generators_of_AirTable.update_layout(
    xaxis_title = "Y1 RECs",
    title_x = 0.5,
    yaxis_title = "Frequency Of Y1 RECs",
    showlegend = False
)

graph_of_frequency_of_Y1_RECs_vs_Y1_RECs_per_table_Generators_of_AirTable = dcc.Graph(
    id = f"Histogram Of Frequency Of Y1 RECs Vs. Y1 RECs Per Table Generators Of AirTable",
    figure = histogram_of_frequency_of_Y1_RECs_vs_Y1_RECs_per_table_Generators_of_AirTable
)