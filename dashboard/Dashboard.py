import dash
from dash import html
from dashboard.headings import heading_Dashboard, heading_Executive_Summary, heading_Summary_Of_AB_Testing
from dashboard.set_of_tabs import set_of_tabs


class Factory():

    def create_dash(self):
        app = dash.Dash(__name__)

        list_of_children = [
            heading_Dashboard,
            heading_Executive_Summary,
            heading_Summary_Of_AB_Testing,
            set_of_tabs
        ]

        div = html.Div(list_of_children)

        app.layout = div
        return app


if __name__ == "__main__":

    factory = Factory()
    app = factory.create_dash()
    app.run_server(debug = True)