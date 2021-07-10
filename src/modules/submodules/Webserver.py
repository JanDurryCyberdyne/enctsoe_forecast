class Webserver:
    def __init__(self, webserver):
        app = webserver["dash"].dash.Dash(__name__)
        if __name__ == 'src.modules.submodules.Webserver':
            app.run_server(debug=True)
            print("Webserver initiated")