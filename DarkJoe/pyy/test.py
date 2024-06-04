import threading
import time
from connet_db import connect
from fetch import fetch_data_and_insert_to_twincn
from propertyQuery import fetch_data_and_insert_to_py_ppstrq_input
from MOL_SQL import fetch_data_and_insert_to_py_mol_input
from PRTRtest import fetch_data_and_insert_to_py_prtr_input
from moea import fetch_data_and_insert_to_py_moea_input

def fetch_moea():
    time.sleep(1)
    fetch_data_and_insert_to_py_moea_input()

def fetch_prtr():
    fetch_data_and_insert_to_py_prtr_input()

def fetch_mol():
    fetch_data_and_insert_to_py_mol_input()

def fetch_ppstrq():
    fetch_data_and_insert_to_py_ppstrq_input()

def fetch_twincn():
    fetch_data_and_insert_to_twincn()

def main():
    threads = []
    
    # 創建多線程
    threads.append(threading.Thread(target=fetch_moea))
    threads.append(threading.Thread(target=fetch_prtr))
    threads.append(threading.Thread(target=fetch_mol))
    threads.append(threading.Thread(target=fetch_ppstrq))
    threads.append(threading.Thread(target=fetch_twincn))
    
    # 啟動所有線程
    for thread in threads:
        thread.start()
    
    # 等待所有線程完成
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
