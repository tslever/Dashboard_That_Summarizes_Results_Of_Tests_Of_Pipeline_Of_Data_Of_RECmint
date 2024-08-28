from dash import dcc
from dashboard.Loader import loader
import numpy as np
import plotly.express as px


list_of_values_in_column_Zip_Code_of_table_Generators_of_AirTable = \
    loader.list_values_in_column_of_table_Generators_of_AirTable(
        start_of_name_of_column = "Zip Code"
    )

histogram_of_frequency_of_Zip_Code_vs_Zip_Code_per_table_Generators_of_AirTable = px.histogram(
    np.array(list_of_values_in_column_Zip_Code_of_table_Generators_of_AirTable),
    nbins = 100,
    labels = {"value": "Zip Code"},
    title = "Histogram Of Frequency Of Zip Code Vs. Zip Code<br>Per Table Generators Of Database AirTable"
)
histogram_of_frequency_of_Zip_Code_vs_Zip_Code_per_table_Generators_of_AirTable.update_layout(
    xaxis_title = "Zip Code",
    title_x = 0.5,
    yaxis_title = "Frequency Of Zip Code",
    showlegend = False
)

graph_of_frequency_of_Zip_Code_vs_Zip_Code_per_table_Generators_of_AirTable = dcc.Graph(
    id = f"Histogram Of Frequency Of Zip Code Vs. Zip Code Per Table Generators Of AirTable",
    figure = histogram_of_frequency_of_Zip_Code_vs_Zip_Code_per_table_Generators_of_AirTable
)