import os
from src.modules.submodules.CalcEngine import CalcEngine
from src.modules.Controller import Controller
from src.modules.View import View
from src.modules.Model import Model
from dotenv import load_dotenv

class DashApp:
    
    def __init__(self): 
        load_dotenv()
        self.View = View()
        self.CalcEngine = CalcEngine()
        self.Controller = Controller()
        self.Model = Model()
        self.API_KEY = os.getenv("API_KEY")
        print(self.API_KEY)
