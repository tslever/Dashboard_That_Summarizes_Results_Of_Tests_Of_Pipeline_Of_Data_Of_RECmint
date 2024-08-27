from dash import dcc
from dashboard.Loader import loader
import numpy as np
import plotly.express as px


list_of_values_in_column_nominal_power_AC_of_table_Generators_of_RECBus = \
    loader.list_values_in_column_of_table_Generators_of_RECBus(name_of_column = "nominal-power-AC")

histogram_of_frequency_of_nominal_power_AC_vs_nominal_power_AC_per_table_Generators_of_RECBus = px.histogram(
    np.log(np.array(list_of_values_in_column_nominal_power_AC_of_table_Generators_of_RECBus) + 1),
    nbins = 100,
    labels = {"value": "nominal-power-AC"},
    title = "Histogram Of Frequency Of nominal-power-AC Vs. nominal-power-AC<br>Per Table Generators Of Database RECBus"
)
histogram_of_frequency_of_nominal_power_AC_vs_nominal_power_AC_per_table_Generators_of_RECBus.update_layout(
    xaxis_title = "Values Of Column nominal-power-AC",
    title_x = 0.5,
    yaxis_title = "Frequency Of Values Of Column nominal-power-AC",
    showlegend = False
)

graph_of_frequency_of_nominal_power_AC_vs_nominal_power_AC_per_table_Generators_of_RECBus = dcc.Graph(
    id = f"Histogram Of Frequency Of nominal-power-AC Vs. nominal-power-AC Per Table Generators Of RECBus",
    figure = histogram_of_frequency_of_nominal_power_AC_vs_nominal_power_AC_per_table_Generators_of_RECBus
)