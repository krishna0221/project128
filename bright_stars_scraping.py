from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

#Link
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

#Webdriver
browser = webdriver.Chrome('D:/Setup/chromedriver_win32/chromedriver.exe')
browser.get(START_URL)

time.sleep(10)

scraped_data = []

#define data scraping method
def scrape():
    
        time.sleep(2)

        soup = BeautifulSoup(browser.page_source, "html.parser")

        #find table
        bright_star_table = soup.find("table",attrs={"class","wikitable"})

        #find <tbody>
        table_body = bright_star_table.find("tbody")

        #find <tr>
        table_rows = table_body.find_all("tr")

        #get data from <td>
        for row in table_rows:
            table_cols = row.find_all("td")
            print(table_cols)

            temp_list = []

            for col_data in table_cols:
                #print only column using .text
                #print(col_data.text)

                #removing extra white spaces using .strip
                data = col_data.text.strip()
                #print(data)

                temp_list.append(data)
            scraped_data.append(temp_list)
scrape()

stars_data = []
for i in range(0,len(scraped_data)):
    Star_name = scraped_data[i][1]
    Distance = scraped_data[i][3]
    Mass = scraped_data[i][5]
    Radius = scraped_data[i][6]
    Lum = scraped_data[i][7]

    required_data = [Star_name,Distance,Mass,Radius,Lum]
    stars_data.append(required_data)

headers = ["Star_Name","Distance","Mass","Radius","Luminosity"]
star_df_1 = pd.DataFrame(stars_data,columns=headers)

star_df_1.to_csv("bright_stars.csv",index = True,index_label = "id")