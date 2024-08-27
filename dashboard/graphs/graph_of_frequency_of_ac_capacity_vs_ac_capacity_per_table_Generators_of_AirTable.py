from dash import dcc
from Loader import loader
import numpy as np
import plotly.express as px


list_of_values_in_column_AC_Capacity_of_table_Generators_of_AirTable = \
    loader.list_values_in_column_of_table_Generators_of_AirTable(name_of_column = "AC Capacity (kW AC)")

histogram_of_frequency_of_ac_capacity_vs_ac_capacity_per_table_Generators_of_AirTable = px.histogram(
    np.log(np.array(list_of_values_in_column_AC_Capacity_of_table_Generators_of_AirTable) + 1),
    nbins = 100,
    labels = {"value": "AC Capacity (kW AC)"},
    title = "Histogram Of Frequency Of AC Capacity Vs. AC Capacity<br>Per Table Generators Of Database AirTable"
)
histogram_of_frequency_of_ac_capacity_vs_ac_capacity_per_table_Generators_of_AirTable.update_layout(
    xaxis_title = "AC Capacity (kW AC)",
    title_x = 0.5,
    yaxis_title = "Frequency Of AC Capacity (kW AC)",
    showlegend = False
)

graph_of_frequency_of_ac_capacity_vs_ac_capacity_per_table_Generators_of_AirTable = dcc.Graph(
    id = f"Histogram Of Frequency Of AC Capacity (kW AC) Vs. AC Capacity Per Table Generators Of AirTable",
    figure = histogram_of_frequency_of_ac_capacity_vs_ac_capacity_per_table_Generators_of_AirTable
)