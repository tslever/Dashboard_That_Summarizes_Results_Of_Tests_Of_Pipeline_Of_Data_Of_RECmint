from dash import dcc
from dashboard.Loader import loader
import numpy as np
import plotly.express as px


list_of_values_in_column_Count_Of_Generators_of_table_Generators_of_AirTable = \
    loader.list_values_in_column_of_table_Generators_of_AirTable(
        start_of_name_of_column = "Count - Gen Sync Not Computed"
    )

histogram_of_frequency_of_Count_Of_Generators_vs_Count_per_table_Generators_of_AirTable = px.histogram(
    np.array(list_of_values_in_column_Count_Of_Generators_of_table_Generators_of_AirTable),
    nbins = 100,
    labels = {"value": "Count Of Generators"},
    title = "Histogram Of Frequency Of Count Of Generators Vs. Count<br>Per Table Generators Of Database AirTable"
)
histogram_of_frequency_of_Count_Of_Generators_vs_Count_per_table_Generators_of_AirTable.update_layout(
    xaxis_title = "Count Of Generators",
    title_x = 0.5,
    yaxis_title = "Frequency Of Count Of Generators",
    showlegend = False
)

graph_of_frequency_of_Count_Of_Generators_vs_Count_per_table_Generators_of_AirTable = dcc.Graph(
    id = f"Histogram Of Frequency Of Count Of Generators Vs. Count Per Table Generators Of AirTable",
    figure = histogram_of_frequency_of_Count_Of_Generators_vs_Count_per_table_Generators_of_AirTable
)