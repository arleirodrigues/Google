
"""		Pyautomator Framework de teste 

			Google"""

from Pyautomators import *
from time import sleep
from Pyautomators.web import Web
from Pyautomators import Ambiente

def before_all(context):
	context.path = Ambiente.path_atual()
	context.app = Web('Chrome',context.path+'driver/chromedriver.exe')
	context.app.maximiza()

def before_feature(context,feature):
	pass

def before_scenario(context,scenario):
	pass

def before_step(context,step):
	pass

def after_step(context,step):
	pass

def after_scenario(context,scenario):
	pass

def after_feature(context,feature):
	pass

def after_all(context):
	context.app.fechar_programa()

