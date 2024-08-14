from dash import dcc
import Loader
import numpy as np
import plotly.express as px


def create_graph_of_frequency_of_energy_vs_energy_per_table_Generators_of(name_of_database: str) -> dcc.Graph:

    list_of_values_in_column_Nameplate_of_table_Generators_of_database = \
        Loader.create_list_of_values_in_column_Nameplate_of_table_Generators_of(name_of_database)
    
    histogram_of_frequency_of_energy_vs_energy_per_table_Generators_of_database = px.histogram(
        np.log(list_of_values_in_column_Nameplate_of_table_Generators_of_database),
        nbins = 100
    )

    graph_of_frequency_of_energy_vs_energy_per_table_Generators_of_database = dcc.Graph(
        id = f"Histogram Of Frequency Of Energy Vs. Energy Per Table Generators Of {name_of_database}",
        figure = histogram_of_frequency_of_energy_vs_energy_per_table_Generators_of_database
    )

    return graph_of_frequency_of_energy_vs_energy_per_table_Generators_of_database