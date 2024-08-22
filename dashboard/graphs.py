from dash import dcc
from dashboard.Loader import loader
import numpy as np
import plotly.express as px


list_of_values_in_column_Nameplate_of_table_Generators_of_AirTable = \
    loader.list_values_in_column_of_table_Generators_of_AirTable(name_of_column = "Nameplate (kW DC)")

histogram_of_frequency_of_Nameplate_vs_Nameplate_per_table_Generators_of_AirTable = px.histogram(
    np.log(list_of_values_in_column_Nameplate_of_table_Generators_of_AirTable),
    nbins = 100,
    labels = {"value": "Log Of Values In Column Nameplate"},
    title = "Histogram Of Frequency Of Nameplate Vs. Log Of Nameplate<br>Per Table Generators Of Database AirTable"
)
histogram_of_frequency_of_Nameplate_vs_Nameplate_per_table_Generators_of_AirTable.update_layout(
    xaxis_title = "Log Of Values In Column Nameplate",
    title_x = 0.5,
    yaxis_title = "Frequency Of Values In Column Nameplate",
    showlegend = False
)

graph_of_frequency_of_Nameplate_vs_Nameplate_per_table_Generators_of_AirTable = dcc.Graph(
    id = f"Histogram Of Frequency Of Nameplate Vs. Nameplate Per Table Generators Of AirTable",
    figure = histogram_of_frequency_of_Nameplate_vs_Nameplate_per_table_Generators_of_AirTable
)


list_of_values_in_column_nominal_power_of_table_Generators_of_RECBus = \
    loader.list_values_in_column_nominal_power_of_table_Generators_of_RECBus()

histogram_of_frequency_of_nominal_power_vs_nominal_power_per_table_Generators_of_RECBus = px.histogram(
    np.log(list_of_values_in_column_nominal_power_of_table_Generators_of_RECBus),
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


list_of_DC_powers_in_AirTable_and_RECBus = loader.list_DC_powers_in_AirTable_and_RECBus()

histogram_of_frequency_of_DC_power_vs_DC_power_per_AirTable_and_RECBus = px.histogram(
    np.log(list_of_DC_powers_in_AirTable_and_RECBus),
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


list_of_values_in_column_AC_Capacity_of_table_Generators_of_AirTable = \
    loader.list_values_in_column_of_table_Generators_of_AirTable(name_of_column = "AC Capacity (kW AC)")

histogram_of_frequency_of_ac_capacity_vs_ac_capacity_per_table_Generators_of_AirTable = px.histogram(
    list_of_values_in_column_AC_Capacity_of_table_Generators_of_AirTable,
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