from dash import dcc
from dashboard.Loader import loader
import numpy as np
import plotly.express as px


list_of_values_in_column_of_Annuity_Rates_of_table_Generators_of_AirTable = \
    loader.list_values_in_column_of_table_Generators_of_AirTable(
        start_of_name_of_column = "Locked Annuity Rate for Current Contract"
    )

histogram_of_frequency_of_Annuity_Rate_vs_Rate_per_table_Generators_of_AirTable = px.histogram(
    np.array(list_of_values_in_column_of_Annuity_Rates_of_table_Generators_of_AirTable),
    nbins = 100,
    labels = {"value": "Annuity Rate"},
    title = "Histogram Of Frequency Of Annuity Rate Vs. Annuity Rate<br>Per Table Generators Of Database AirTable"
)
histogram_of_frequency_of_Annuity_Rate_vs_Rate_per_table_Generators_of_AirTable.update_layout(
    xaxis_title = "Annuity Rate",
    title_x = 0.5,
    yaxis_title = "Frequency Of Annuity Rate",
    showlegend = False
)

graph_of_frequency_of_Annuity_Rate_vs_Rate_per_table_Generators_of_AirTable = dcc.Graph(
    id = f"Histogram Of Frequency Of Annuity Rate Vs. Annuity Rate Per Table Generators Of AirTable",
    figure = histogram_of_frequency_of_Annuity_Rate_vs_Rate_per_table_Generators_of_AirTable
)