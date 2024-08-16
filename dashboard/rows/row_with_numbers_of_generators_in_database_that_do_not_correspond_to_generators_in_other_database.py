from dashboard.Cell import Cell
from dash import html
from dashboard.Loader import loader


number_of_generators_in_AirTable_that_do_not_correspond_to_generators_in_RECBus = \
    loader.calculate_number_of_generators_in_AirTable_that_do_not_correspond_to_generators_in_RECBus()

number_of_generators_in_RECBus_that_do_not_correspond_to_generators_in_AirTable = \
    loader.calculate_number_of_generators_in_RECBus_that_do_not_correspond_to_generators_in_AirTable()

list_of_children = [
    Cell("number of generators in AirTable that do not correspond to generators in RECBus"),
    Cell(number_of_generators_in_AirTable_that_do_not_correspond_to_generators_in_RECBus),
    Cell("number of generators in RECBus that do not correspond to generators in AirTable"),
    Cell(number_of_generators_in_RECBus_that_do_not_correspond_to_generators_in_AirTable)
]

row_with_numbers_of_generators_in_database_that_do_not_correspond_to_generators_in_other_database = \
    html.Tr(list_of_children)