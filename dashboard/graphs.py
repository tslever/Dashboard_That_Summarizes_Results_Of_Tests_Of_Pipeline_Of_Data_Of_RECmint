from dash import dcc
from dashboard.Loader import loader
import numpy as np
import plotly.express as px


list_of_values_in_column_Nameplate_of_table_Generators_of_AirTable = \
    loader.create_list_of_values_in_column_Nameplate_of_table_Generators_of_AirTable()

histogram_of_frequency_of_energy_vs_energy_per_table_Generators_of_AirTable = px.histogram(
    np.log(list_of_values_in_column_Nameplate_of_table_Generators_of_AirTable),
    nbins = 100,
    labels = {"value": "Log Of Energy"},
    title = "Histogram Of Frequency Vs. Log Of Energy<br>Per Table Generators Of Database AirTable"
)
histogram_of_frequency_of_energy_vs_energy_per_table_Generators_of_AirTable.update_layout(
    xaxis_title = "Log Of Energy",
    title_x = 0.5,
    yaxis_title = "Frequency Of Energy",
    showlegend = False
)

graph_of_frequency_of_energy_vs_energy_per_table_Generators_of_AirTable = dcc.Graph(
    id = f"Histogram Of Frequency Of Energy Vs. Energy Per Table Generators Of AirTable",
    figure = histogram_of_frequency_of_energy_vs_energy_per_table_Generators_of_AirTable
)


list_of_values_in_column_nominal_power_of_table_Generators_of_RECBus = \
    loader.create_list_of_values_in_column_nominal_power_of_table_Generators_of_RECBus()

histogram_of_frequency_of_energy_vs_energy_per_table_Generators_of_RECBus = px.histogram(
    np.log(list_of_values_in_column_nominal_power_of_table_Generators_of_RECBus),
    nbins = 100,
    labels = {"value": "Log Of Energy"},
    title = "Histogram Of Frequency Vs. Log Of Energy<br>Per Table Generators Of Database RECBus"
)
histogram_of_frequency_of_energy_vs_energy_per_table_Generators_of_RECBus.update_layout(
    xaxis_title = "Log Of Energy",
    title_x = 0.5,
    yaxis_title = "Frequency Of Energy",
    legend_title = "Legend",
    showlegend = False
)

graph_of_frequency_of_energy_vs_energy_per_table_Generators_of_RECBus = dcc.Graph(
    id = f"Histogram Of Frequency Of Energy Vs. Energy Per Table Generators Of RECBus",
    figure = histogram_of_frequency_of_energy_vs_energy_per_table_Generators_of_RECBus
)


list_powers_in_AirTable_and_RECBus = loader.list_powers_in_AirTable_and_RECBus()

histogram_of_frequency_of_energy_vs_energy_per_AirTable_and_RECBus = px.histogram(
    np.log(list_powers_in_AirTable_and_RECBus),
    nbins = 100,
    labels = {"value": "Log Of Energy"},
    title = "Histogram Of Frequency Of Energy Vs. Log Of Energy<br>Per AirTable And RECBus"
)
histogram_of_frequency_of_energy_vs_energy_per_AirTable_and_RECBus.update_layout(
    xaxis_title = "Log Of Energy",
    title_x = 0.5,
    yaxis_title = "Frequency Of Energy",
    legend_title = "Legend",
    showlegend = False
)

graph_of_frequency_of_energy_vs_energy_per_AirTable_and_RECBus = dcc.Graph(
    id = f"Histogram Of Frequency Of Energy Vs. Energy Per AirTable And RECBus",
    figure = histogram_of_frequency_of_energy_vs_energy_per_AirTable_and_RECBus
)