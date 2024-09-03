from dash import dcc
from Loader import loader
import numpy as np
import plotly.express as px


class Grapher():


    def graph_frequency_of_quantity_vs_quantity(
        self,
        name_of_database: str,
        quantity: str,
        log_should_be_applied: bool
    ) -> dcc.Graph:

        list_of_values = loader.list_values_in_column_of_table_Generators(name_of_database = name_of_database, start_of_name_of_column = quantity)
        array_of_values = np.array(list_of_values)

        histogram = px.histogram(
            np.log(array_of_values + 1) if log_should_be_applied else array_of_values,
            nbins = 100,
            labels = {"value": quantity},
            title = f"Histogram Of Frequency Of {quantity} Vs. {quantity}"
        )
        histogram.update_layout(
            xaxis_title = quantity,
            title_x = 0.5,
            yaxis_title = f"Frequency Of quantity",
            showlegend = False
        )

        graph_of_frequency_of_quantity_vs_quantity = dcc.Graph(
            id = f"Histogram Of Frequency Of {quantity} Vs. {quantity}",
            figure = histogram
        )

        return graph_of_frequency_of_quantity_vs_quantity
    

grapher = Grapher()