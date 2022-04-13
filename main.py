import os
from cffi.setuptools_ext import execfile
from Data.merge_json import merge_json
from TextAnalyzer.clean_data import clean_data
from IMDB.imdb_scrap import initiate_scrapping_imdb
from SensCritique.sc_scrap import initiate_scrapping_sc

initiate_scrapping_imdb()
initiate_scrapping_sc()
merge_json()
clean_data()
execfile(os.path.abspath('Dashboard/app.py'))