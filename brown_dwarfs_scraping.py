from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

#Link
url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
response=requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')

table = soup.find_all('table',{'class':'wikitable sortable jquery-tablesorter'})
#total_table = len(table)
temp_list=[]

t_rows = table[1].find_all('tr')
for tr in t_rows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)

Star_Name = []
Distance=[]
Mass=[]
Radius=[]
print(temp_list)
print(len(temp_list))

for i in range(1,len(temp_list)):
    Star_Name.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])


headers = ["Star_Name","Distance","Mass","Radius"]
star_df_2 = pd.DataFrame(list(zip(Star_Name,Distance,Mass,Radius)),columns=headers)

star_df_2.to_csv("dwarf_stars.csv",index = True,index_label = "id")