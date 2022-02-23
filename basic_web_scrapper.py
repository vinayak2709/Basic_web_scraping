# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 21:56:47 2022

@author: Vinayak
"""
import pandas as pd 

import bs4 as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

 
def csv_writer(number_list,url_list,data_list,file_save_path):
    
  
    # # dictionary of lists 
    data_dict = {'url_id': number_list, 'URL':url_list[:len(data_list)],"raw_data": data_list} 
         
    df = pd.DataFrame(data_dict)
    
    
    writer = pd.ExcelWriter(file_save_path, engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1')

    writer.save()
    # saving the dataframe
    # df.to_csv(file_save_path)
    


def web_scrap(URL):
    
    chrome_options = Options()
    # driver = webdriver.Chrome(r"C:\Users\Vinayak\Downloads\sql_python-20211215T060936Z-001\sql_python\chromedriver.exe", options=chrome_options)    
    driver = webdriver.Chrome(r"C:\Users\Vinayak\Downloads\sql_python-20211215T060936Z-001\sql_python\chromedriver.exe")    

    data=driver.get(URL)
    try:
        soup = bs.BeautifulSoup(driver.page_source)
        
    except:
        soup=data
        pass
    
    print(soup)
    
    # Close ChromeDriver.
    driver.close()
    return soup
  
    
    

base_excel_path=r'C:\Users\Vinayak\Downloads\input.xlsx'
file_save_path=r'C:\Users\Vinayak\Downloads\scrap_final22.xlsx'

df2=pd.read_excel(base_excel_path)

data_list=[]
number_list=[]
number=0   


for url in df2["URL"]:
    print(url)
    number+=1
    scrp_data=''
    scrp_data=web_scrap(url)
    
    data_list.append(scrp_data)
    number_list.append(number)
    
    if number==3:
        break
   
url_list=list(df2["URL"])
csv_writer(number_list,url_list,data_list,file_save_path)
    

    
    