import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard"),
    html.H2("Executive Summary"),
    html.H2("Summary of A/B Testing")
])

if __name__ == "__main__":
    app.run_server(debug = True)