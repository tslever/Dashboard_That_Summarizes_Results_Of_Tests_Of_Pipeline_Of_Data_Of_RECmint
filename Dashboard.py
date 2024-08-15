import dash
from div import div


class Factory():

    def create_dash(self):
        app = dash.Dash(__name__)
        app.layout = div
        return app


if __name__ == "__main__":

    factory = Factory()
    app = factory.create_dash()
    app.run_server(debug = True)