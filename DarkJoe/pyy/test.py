from connet_db import connect
import threading
from fetch import fetch_data_and_insert_to_twincn
from propertyQuery import fetch_data_and_insert_to_py_ppstrq_input
from  MOL_SQL  import fetch_data_and_insert_to_py_mol_input
from PRTRtest import fetch_data_and_insert_to_py_prtr_input , fetch_and_clean_data
from openaitest import fetch_openai_response
from moea import fetch_data_and_insert_to_py_moea_input
import os
import time


os.environ["OPENAI_API_KEY"] = "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"


def main():
    threads = []
    
    #=============================抓公司登記資料=====================
    time.sleep(1)
    threads.append(threading.Thread(target=fetch_data_and_insert_to_py_moea_input))
    #==============================================================
    
    #=============================抓環境部汙染======================
    threads.append(threading.Thread(target=fetch_data_and_insert_to_py_prtr_input))
    #==============================================================
    
    #=============================抓勞動部勞基法====================
    threads.append(threading.Thread(target=fetch_data_and_insert_to_py_mol_input))
    #==============================================================
    
    #============================抓動產資料=========================
    threads.append(threading.Thread(target=fetch_data_and_insert_to_py_ppstrq_input))
    #==============================================================
    
    #===========================從台灣公司網抓訴訟===================
    threads.append(threading.Thread(target=fetch_data_and_insert_to_twincn))
    #==============================================================
    # 啟動所有線程
    for thread in threads:
        thread.start()
    
    # 等待所有線程完成
    for thread in threads:
        thread.join()
    #==========================抓所有table資料並轉成json並過濾autono===
    question=fetch_and_clean_data()
    OPENAI_API_KEY=os.environ["OPENAI_API_KEY"]
    # print(question)     #測試 是否有把json傳入
    #==============================================================
  
    #=========================把json丟給openai問他問題==============
    fetch_openai_response(OPENAI_API_KEY,question)
    # print(fetch_openai_response(OPENAI_API_KEY,question))
    #==============================================================
if __name__ == '__main__':

    
    # 呼叫主函數
    main()
    
    
    