from dash import dcc
from Loader import loader
import numpy as np
import plotly.express as px


list_of_DC_powers_in_AirTable_and_RECBus = loader.list_DC_powers_in_AirTable_and_RECBus()

histogram_of_frequency_of_DC_power_vs_DC_power_per_AirTable_and_RECBus = px.histogram(
    np.log(np.array(list_of_DC_powers_in_AirTable_and_RECBus) + 1),
    nbins = 100,
    labels = {"value": "Log Of DC Power"},
    title = "Histogram Of Frequency Of DC Power Vs. Log Of DC Power<br>Per AirTable And RECBus"
)
histogram_of_frequency_of_DC_power_vs_DC_power_per_AirTable_and_RECBus.update_layout(
    xaxis_title = "Log Of DC Power",
    title_x = 0.5,
    yaxis_title = "Frequency Of DC Power",
    legend_title = "Legend",
    showlegend = False
)

graph_of_frequency_of_DC_power_vs_DC_power_per_AirTable_and_RECBus = dcc.Graph(
    id = f"Histogram Of Frequency Of DC Power Vs. DC Power Per AirTable And RECBus",
    figure = histogram_of_frequency_of_DC_power_vs_DC_power_per_AirTable_and_RECBus
)