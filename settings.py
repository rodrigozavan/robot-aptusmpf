from dotenv import load_dotenv
import logging
import json
import os

BASE_DIR = os.path.dirname(__file__)
BASE_NAME = os.path.basename(BASE_DIR)
ENV_FILE = os.path.join(BASE_DIR, '.env')
LOG_FILE = os.path.join(BASE_DIR, f'{BASE_NAME}.log')
RESULT_FILE = os.path.join(BASE_DIR, f'dados_processo.json')

load_dotenv(ENV_FILE)

config = json.load(open(os.path.join(BASE_DIR, 'config.json')))

ENVIROMENT = os.environ['ENVIROMENT']

logging.basicConfig(
  filename=LOG_FILE,
  encoding='utf-8',
  level=logging.INFO,
  format='%(asctime)s %(levelname)s [module:(%(module)s) line:%(lineno)d]: %(message)s', # noqa E501
  datefmt='%d-%m-%Y %H:%M',
)

logger = logging.getLogger(BASE_NAME)

URL_CONSULT = config.get(ENVIROMENT).get('aptusmpf').get('url')
