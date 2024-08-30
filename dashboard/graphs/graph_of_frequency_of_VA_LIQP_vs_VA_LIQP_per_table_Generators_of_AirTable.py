from dash import dcc
from dashboard.Loader import loader
import numpy as np
import plotly.express as px


list_of_values_in_column_VA_LIQP_of_table_Generators_of_AirTable = \
    loader.list_values_in_column_of_table_Generators_of_AirTable(
        start_of_name_of_column = "VA LIQP"
    )

histogram_of_frequency_of_VA_LIQP_vs_VA_LIQP_per_table_Generators_of_AirTable = px.histogram(
    np.array(list_of_values_in_column_VA_LIQP_of_table_Generators_of_AirTable),
    nbins = 100,
    labels = {"value": "VA_LIQP"},
    title = "Histogram Of Frequency Of VA_LIQP Vs. VA_LIQP<br>Per Table Generators Of Database AirTable"
)
histogram_of_frequency_of_VA_LIQP_vs_VA_LIQP_per_table_Generators_of_AirTable.update_layout(
    xaxis_title = "VA_LIQP",
    title_x = 0.5,
    yaxis_title = "Frequency Of VA_LIQP",
    showlegend = False
)

graph_of_frequency_of_VA_LIQP_vs_VA_LIQP_per_table_Generators_of_AirTable = dcc.Graph(
    id = f"Histogram Of Frequency Of VA LIQP Vs. LIQP Per Table Generators Of AirTable",
    figure = histogram_of_frequency_of_VA_LIQP_vs_VA_LIQP_per_table_Generators_of_AirTable
)