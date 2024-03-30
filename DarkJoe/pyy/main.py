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
    
    #=============================抓公司登記資料=====================
    fetch_data_and_insert_to_py_moea_input()
    #==============================================================
    
    #=============================抓環境部汙染======================
    fetch_data_and_insert_to_py_prtr_input()
    #==============================================================
    
    #=============================抓勞動部勞基法====================
    fetch_data_and_insert_to_py_mol_input()
    #==============================================================
    
    #============================抓動產資料=========================
    fetch_data_and_insert_to_py_ppstrq_input()
    #==============================================================
    
    #===========================從台灣公司網抓訴訟===================
    fetch_data_and_insert_to_twincn()
    #==============================================================
    
    #==========================抓所有table資料並轉成json並過濾autono===
    question=fetch_and_clean_data()
    #==============================================================
  
    #=========================把json丟給openai問他問題==============
    # fetch_openai_response(OPENAI_API_KEY,question)
    #==============================================================
if __name__ == '__main__':

    
    # 呼叫主函數
    main()
    
    
