from dash import html


class Cell(html.Td):

    def __init__(
            self,
            children,
            width: int = None,
            colSpan: int = 1
        ):

        super().__init__(
            children = children,
            style = {"width": f"{width}%"},
            colSpan = colSpan
        )