from Cell import Cell
from dash import html
import Grapher


class Row_With_Graphs_Of_Frequency_Of_Energy_Vs_Energy(html.Tr):

    def __init__(self):
        super().__init__(
            children = [
                Cell(
                    Grapher.create_graph_of_frequency_of_energy_vs_energy_per_table_Generators_of("AirTable")
                ),
                Cell(
                    Grapher.create_graph_of_frequency_of_energy_vs_energy_per_table_Generators_of("RECBus")
                )
            ]
        )