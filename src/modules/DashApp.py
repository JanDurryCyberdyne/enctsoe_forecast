from src.modules.submodules.CalcEngine import CalcEngine
from src.modules.submodules.Webserver import Webserver
from src.modules.Controller import Controller
from src.modules.View import View
from src.modules.Model import Model

class DashApp:
    def __init__(self, Options):
        self.Webserver = Webserver(Options["webserver"])
        self.View = View(Webserver)
        self.CalcEngine = CalcEngine()
        self.Controller = Controller()
        self.Model = Model()
        self.API_KEY = Options["os"].getenv("API_KEY") 
        print(self.API_KEY)