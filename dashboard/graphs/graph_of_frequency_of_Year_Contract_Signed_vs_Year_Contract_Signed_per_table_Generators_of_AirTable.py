from dash import dcc
from dashboard.Loader import loader
import numpy as np
import plotly.express as px


list_of_values_in_column_Year_Contract_Signed_of_table_Generators_of_AirTable = \
    loader.list_values_in_column_of_table_Generators_of_AirTable(
        start_of_name_of_column = "Year Contract Signed"
    )

histogram_of_frequency_of_Year_Contract_Signed_vs_Year_Contract_Signed_per_table_Generators_of_AirTable = px.histogram(
    np.array(list_of_values_in_column_Year_Contract_Signed_of_table_Generators_of_AirTable),
    nbins = 100,
    labels = {"value": "Year Contract Signed"},
    title = "Histogram Of Frequency Of Year Contract Signed Vs. Year Contract Signed<br>Per Table Generators Of Database AirTable"
)
histogram_of_frequency_of_Year_Contract_Signed_vs_Year_Contract_Signed_per_table_Generators_of_AirTable.update_layout(
    xaxis_title = "Year Contract Signed",
    title_x = 0.5,
    yaxis_title = "Frequency Of Year Contract Signed",
    showlegend = False
)

graph_of_frequency_of_Year_Contract_Signed_vs_Year_Contract_Signed_per_table_Generators_of_AirTable = dcc.Graph(
    id = f"Histogram Of Frequency Of Year Contract Signed Vs. Year Contract Signed Per Table Generators Of AirTable",
    figure = histogram_of_frequency_of_Year_Contract_Signed_vs_Year_Contract_Signed_per_table_Generators_of_AirTable
)