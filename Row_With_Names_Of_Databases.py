from Cell import Cell
from dash import html

class Row_With_Names_Of_Databases(html.Tr):

    def __init__(self):
        super().__init__(
            children = [
                Cell(children = "AirTable", width = 50),
                Cell(children = "RECBus", width = 50)
            ]
        )