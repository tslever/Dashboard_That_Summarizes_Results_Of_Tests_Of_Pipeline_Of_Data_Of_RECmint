from dash import html


class Table(html.Table):

    def __init__(self, children, width: int):

        super().__init__(
            children = children,
            style = {"width": f"{width}%"}
        )
