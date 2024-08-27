from dash import dcc
from dashboard.Loader import loader
import numpy as np
import plotly.express as px


list_of_values_in_column_nominal_power_of_table_Generators_of_RECBus = \
    loader.list_values_in_column_of_table_Generators_of_RECBus(name_of_column = "nominal-power")

histogram_of_frequency_of_nominal_power_vs_nominal_power_per_table_Generators_of_RECBus = px.histogram(
    np.log(np.array(list_of_values_in_column_nominal_power_of_table_Generators_of_RECBus) + 1),
    nbins = 100,
    labels = {"value": "Log Of Values In Column nominal-power"},
    title = "Histogram Of Frequency Of nominal-power Vs. Log Of nominal-power<br>Per Table Generators Of Database RECBus"
)
histogram_of_frequency_of_nominal_power_vs_nominal_power_per_table_Generators_of_RECBus.update_layout(
    xaxis_title = "Log Of Values In Column nominal-power",
    title_x = 0.5,
    yaxis_title = "Frequency Of Values In Column nominal-power",
    legend_title = "Legend",
    showlegend = False
)

graph_of_frequency_of_nominal_power_vs_nominal_power_per_table_Generators_of_RECBus = dcc.Graph(
    id = f"Histogram Of Frequency Of nominal-power Vs. nominal-power Per Table Generators Of RECBus",
    figure = histogram_of_frequency_of_nominal_power_vs_nominal_power_per_table_Generators_of_RECBus
)