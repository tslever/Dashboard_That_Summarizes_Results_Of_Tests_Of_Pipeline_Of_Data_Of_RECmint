from dash import html
import Styler


class Cell(html.Td):

    def __init__(self, children, width: int = None):

        super().__init__(children = children, style = Styler.create_style(width = width))