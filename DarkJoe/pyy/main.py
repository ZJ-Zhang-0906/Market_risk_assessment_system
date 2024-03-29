from connet_db import connect
from fetch import fetch_data_and_insert_to_twincn
from propertyQuery import fetch_data_and_insert_to_py_ppstrq_input
from  MOL_SQL  import fetch_data_and_insert_to_py_mol_input
from PRTRtest import fetch_data_and_insert_to_py_prtr_input , fetch_and_clean_data
from openaitest import fetch_openai_response
from moea import fetch_data_and_insert_to_py_moea_input
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')





