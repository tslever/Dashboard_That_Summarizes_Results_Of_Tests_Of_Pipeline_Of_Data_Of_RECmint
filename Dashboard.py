import dash
from dash import dcc
from dash import html
from Table_Of_Visualizations_Of_Tables_Of_Databases import Table_Of_Visualizations_Of_Tables_Of_Databases


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1("Dashboard"),

        html.H2("Executive Summary"),

        html.H2("Summary of A/B Testing"),

        dcc.Tabs(
            id = "Summary Of AB Testing",
            value = 'Generators',
            children = [
                dcc.Tab(
                    label = "Contracts",
                    value = "Contracts"
                ),
                dcc.Tab(
                    label = "Generators",
                    value = "Generators",
                    children = Table_Of_Visualizations_Of_Tables_Of_Databases()
                )
            ]
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug = True)