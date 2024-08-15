from dash import dcc
from Loader import loader
import numpy as np
import plotly.express as px


list_of_values_in_column_Nameplate_of_table_Generators_of_AirTable = \
    loader.create_list_of_values_in_column_Nameplate_of_table_Generators_of_AirTable()

histogram_of_frequency_of_energy_vs_energy_per_table_Generators_of_AirTable = px.histogram(
    np.log(list_of_values_in_column_Nameplate_of_table_Generators_of_AirTable),
    nbins = 100
)

graph_of_frequency_of_energy_vs_energy_per_table_Generators_of_AirTable = dcc.Graph(
    id = f"Histogram Of Frequency Of Energy Vs. Energy Per Table Generators Of AirTable",
    figure = histogram_of_frequency_of_energy_vs_energy_per_table_Generators_of_AirTable
)

list_of_values_in_column_nominal_power_of_table_Generators_of_RECBus = \
    loader.create_list_of_values_in_column_nominal_power_of_table_Generators_of_RECBus()

histogram_of_frequency_of_energy_vs_energy_per_table_Generators_of_RECBus = px.histogram(
    np.log(list_of_values_in_column_nominal_power_of_table_Generators_of_RECBus),
    nbins = 100
)

graph_of_frequency_of_energy_vs_energy_per_table_Generators_of_RECBus = dcc.Graph(
    id = f"Histogram Of Frequency Of Energy Vs. Energy Per Table Generators Of RECBus",
    figure = histogram_of_frequency_of_energy_vs_energy_per_table_Generators_of_RECBus
)