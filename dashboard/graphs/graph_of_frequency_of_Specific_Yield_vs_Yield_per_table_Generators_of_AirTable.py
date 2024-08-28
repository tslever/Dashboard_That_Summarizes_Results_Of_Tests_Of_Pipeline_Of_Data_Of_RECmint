from dash import dcc
from dashboard.Loader import loader
import numpy as np
import plotly.express as px


list_of_values_in_column_Specific_Yield_of_table_Generators_of_AirTable = \
    loader.list_values_in_column_of_table_Generators_of_AirTable(
        start_of_name_of_column = "Specific Yield (given)"
    )

histogram_of_frequency_of_Specific_Yield_vs_Yield_per_table_Generators_of_AirTable = px.histogram(
    np.array(list_of_values_in_column_Specific_Yield_of_table_Generators_of_AirTable),
    nbins = 100,
    labels = {"value": "Specific Yield"},
    title = "Histogram Of Frequency Of Specific Yield Vs. Yield<br>Per Table Generators Of Database AirTable"
)
histogram_of_frequency_of_Specific_Yield_vs_Yield_per_table_Generators_of_AirTable.update_layout(
    xaxis_title = "Specific Yield",
    title_x = 0.5,
    yaxis_title = "Frequency Of Specific Yield",
    showlegend = False
)

graph_of_frequency_of_Specific_Yield_vs_Yield_per_table_Generators_of_AirTable = dcc.Graph(
    id = f"Histogram Of Frequency Of Specific Yield Vs. Yield Per Table Generators Of AirTable",
    figure = histogram_of_frequency_of_Specific_Yield_vs_Yield_per_table_Generators_of_AirTable
)