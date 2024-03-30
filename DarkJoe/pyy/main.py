from connet_db import connect
from fetch import fetch_data_and_insert_to_twincn
from propertyQuery import fetch_data_and_insert_to_py_ppstrq_input
from  MOL_SQL  import fetch_data_and_insert_to_py_mol_input
from PRTRtest import fetch_data_and_insert_to_py_prtr_input , fetch_and_clean_data
from openaitest import fetch_openai_response
from moea import fetch_data_and_insert_to_py_moea_input
import os
from dotenv import load_dotenv
# import datetime
import time


load_dotenv()
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')


def main():
    

    fetch_data_and_insert_to_py_moea_input()
    fetch_data_and_insert_to_py_prtr_input()
    fetch_data_and_insert_to_py_mol_input()
    fetch_data_and_insert_to_py_ppstrq_input()
    fetch_data_and_insert_to_twincn()
    question=fetch_and_clean_data()
  

    # fetch_openai_response(OPENAI_API_KEY,question)
if __name__ == '__main__':

    
    # 呼叫主函數
    main()
    
    
