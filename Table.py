from dash import html
import Styler


class Table(html.Table):

    def __init__(self, children, width: int):

        super().__init__(children = children, style = Styler.create_style(width = width))