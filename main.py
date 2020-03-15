from src import yaml_loader
import importlib

config = yaml_loader.load_yaml('config/wematter.yaml')

api_name = config['wematter']['api']
api = importlib.import_module('api.'+api_name+'.'+api_name)

api.info()
