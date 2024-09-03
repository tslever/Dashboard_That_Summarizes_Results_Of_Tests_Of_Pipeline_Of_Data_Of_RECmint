from dash import dash_table
from dashboard.Creator_Of_Rows import creator_of_rows


list_of_columns = [
    {"name": "Description Of Statistic For AirTable", "id": "Description Of Statistic For AirTable"},
    {"name": "Value Of Statistic For AirTable", "id": "Value Of Statistic For AirTable"},
    {"name": "Description Of Statistic For RECBus", "id": "Description Of Statistic For RECBus"},
    {"name": "Value Of Statistic For RECBus", "id": "Value Of Statistic For RECBus"}
]


table_of_statistics_of_table_Generators = dash_table.DataTable(
    columns = list_of_columns,
    data = creator_of_rows.create_list_of_rows_of_statistics(),
    style_table = {"width": "100%"},
    style_cell = {
        "max-width": "0px",
        "white-space": "break-spaces"
    }
)