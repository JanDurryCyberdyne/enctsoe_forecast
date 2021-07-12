import pytz
from src.modules.submodules.DateTimeHandler import DateTimeHandler
from src.modules.submodules.CalcEngine import CalcEngine
from src.modules.submodules.FileHandler import FileHandler
from src.modules.submodules.Webserver import Webserver
from src.modules.submodules.DateTimeHandler import DateTimeHandler
from src.modules.Controller import Controller
from src.modules.submodules.DataHandler import DataHandler
from src.modules.View import View
from src.modules.Model import Model
from dateutil.relativedelta import relativedelta

import datetime
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import os

from dotenv import load_dotenv#

# loads environment files .env
load_dotenv()

# options = {
#     "regions": {
#         "DE-50HZ","TENNET"
#     }
# }


class DashApp:
    def __init__(self):
        # self.Webserver = Webserver(Options["webserver"])
        # self.View = View(Webserver)
        # self.CalcEngine = CalcEngine()
        # self.Controller = Controller()
        # self.Model = Model()
        # self.API_KEY = Options["os"].getenv("API_KEY")
        # print(self.API_KEY)
        self.FileHandler = FileHandler(os)
        self.DateTimeHandler = DateTimeHandler(datetime,pytz,relativedelta,pd)
        # self.CalcEngine = CalcEngine(pd)
        self.DataHandler = DataHandler(os,pd)

DashApp = DashApp()
start,end = DashApp.DateTimeHandler.get_day_times()
#for option in options:

FileName = DashApp.FileHandler.get_filename(start,end,region = "DE-50HZ",data_type = "forecast", forecast_type = "statistical")   #options[selected_value]

DashApp.DataHandler.get_data(DashApp.FileHandler.test_file_exists(FileName),FileName,data_type = "forecast", forecast_type = "statistical")

print(FileName)
# print(DashApp.DataHandler.get_day_times())
# print(DashApp.DataHandler.get_filename(os))
# print(DashApp.DataHandler.get_forecast())

# if (DataHandler.File_Not_Found(Filename)):
#     create file