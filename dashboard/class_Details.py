from dash import html
from dash import dash_table
from dashboard.Table import Table


class Details(html.Details):

    def __init__(self, summary: str, table: Table | dash_table.DataTable, indentation: int = None):

        super().__init__(
            children = [
                html.Summary(summary),
                table
            ],
            style = {} if indentation == None else {"margin-left": f"{indentation}px"}
        )