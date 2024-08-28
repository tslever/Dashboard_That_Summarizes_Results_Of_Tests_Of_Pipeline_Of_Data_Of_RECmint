from dash import dcc
from dashboard.Loader import loader
import numpy as np
import plotly.express as px


list_of_values_in_column_Quantity_Of_Unpurchased_RECs_of_table_Generators_of_AirTable = \
    loader.list_values_in_column_of_table_Generators_of_AirTable(
        start_of_name_of_column = "Qty Unpurchased RECs"
    )

histogram_of_frequency_of_Quantity_Of_Unpurchased_RECs_vs_Quantity_per_table_Generators_of_AirTable = px.histogram(
    np.log(np.array(list_of_values_in_column_Quantity_Of_Unpurchased_RECs_of_table_Generators_of_AirTable) + 1),
    nbins = 100,
    labels = {"value": "Quantity Of Unpurchased RECs"},
    title = "Histogram Of Frequency Of Quantity Of Unpurchased RECs Vs. Quantity<br>Per Table Generators Of Database AirTable"
)
histogram_of_frequency_of_Quantity_Of_Unpurchased_RECs_vs_Quantity_per_table_Generators_of_AirTable.update_layout(
    xaxis_title = "Quantity Of Unpurchased RECs",
    title_x = 0.5,
    yaxis_title = "Frequency Of Quantity Of Unpurchased RECs",
    showlegend = False
)

graph_of_frequency_of_Quantity_Of_Unpurchased_RECs_vs_Quantity_per_table_Generators_of_AirTable = dcc.Graph(
    id = f"Histogram Of Frequency Of Quantity Of Unpurchased RECs Vs. Quantity Per Table Generators Of AirTable",
    figure = histogram_of_frequency_of_Quantity_Of_Unpurchased_RECs_vs_Quantity_per_table_Generators_of_AirTable
)