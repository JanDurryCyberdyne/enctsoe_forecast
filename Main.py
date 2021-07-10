import dash
import dash_html_components as html
import dash_core_components as dcc
import os

from dotenv import load_dotenv
from dash.dependencies import Input,Output
from src.modules.DashApp import DashApp

load_dotenv()

options = {
    "os": os,
    "webserver": {
        "dash": dash,
        "Input": Input,
        "Output": Output
    }
}

DashApp = DashApp(options)