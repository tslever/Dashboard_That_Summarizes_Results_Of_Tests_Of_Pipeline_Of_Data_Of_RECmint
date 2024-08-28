from dash import dcc
from dashboard.Loader import loader
import numpy as np
import plotly.express as px


list_of_values_in_column_AP_to_Date_of_table_Generators_of_AirTable = \
    loader.list_values_in_column_of_table_Generators_of_AirTable(
        start_of_name_of_column = "AP to Date"
    )

histogram_of_frequency_of_AP_to_Date_vs_AP_to_Date_per_table_Generators_of_AirTable = px.histogram(
    np.log(np.array(list_of_values_in_column_AP_to_Date_of_table_Generators_of_AirTable) + 1),
    nbins = 100,
    labels = {"value": "AP to Date"},
    title = "Histogram Of Frequency Of AP to Date Vs. AP to Date<br>Per Table Generators Of Database AirTable"
)
histogram_of_frequency_of_AP_to_Date_vs_AP_to_Date_per_table_Generators_of_AirTable.update_layout(
    xaxis_title = "Values Of Column AP to Date",
    title_x = 0.5,
    yaxis_title = "Frequency Of Values Of Column AP to Date",
    showlegend = False
)

graph_of_frequency_of_AP_to_Date_vs_AP_to_Date_per_table_Generators_of_AirTable = dcc.Graph(
    id = f"Histogram Of Frequency Of AP to Date Vs. AP to Date Per Table Generators Of AirTable",
    figure = histogram_of_frequency_of_AP_to_Date_vs_AP_to_Date_per_table_Generators_of_AirTable
)