from dashboard.Cell import Cell
from dash import html
from dashboard.samples import sample_of_table_Generators_of_AirTable, sample_of_table_Generators_of_RECBus


list_of_children = [
    Cell(sample_of_table_Generators_of_AirTable),
    Cell(sample_of_table_Generators_of_RECBus)
]

row_with_samples_of_table_Generators = html.Tr(list_of_children)