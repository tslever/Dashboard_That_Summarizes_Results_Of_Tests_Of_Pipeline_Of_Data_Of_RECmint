from dash import dcc
from dashboard.Loader import loader
import numpy as np
import plotly.express as px


list_of_values_in_column_Number_Of_Mismatches_of_table_Generators_of_AirTable = \
    loader.list_values_in_column_of_table_Generators_of_AirTable(
        start_of_name_of_column = "TEMP - GenSync row mismatch (expected RECs"
    )

histogram_of_frequency_of_Number_Of_Mismatches_vs_Number_per_table_Generators_of_AirTable = px.histogram(
    np.array(list_of_values_in_column_Number_Of_Mismatches_of_table_Generators_of_AirTable) + 1,
    nbins = 100,
    labels = {"value": "Number Of Mismatches"},
    title = "Histogram Of Frequency Of Number Of Mismatches Vs. Number<br>Per Table Generators Of Database AirTable"
)
histogram_of_frequency_of_Number_Of_Mismatches_vs_Number_per_table_Generators_of_AirTable.update_layout(
    xaxis_title = "Number Of Mismatches",
    title_x = 0.5,
    yaxis_title = "Frequency Of Number Of Mismatches",
    showlegend = False
)

graph_of_frequency_of_Number_Of_Mismatches_vs_Number_per_table_Generators_of_AirTable = dcc.Graph(
    id = f"Histogram Of Frequency Of Number Of Mismatches Vs. Number Per Table Generators Of AirTable",
    figure = histogram_of_frequency_of_Number_Of_Mismatches_vs_Number_per_table_Generators_of_AirTable
)