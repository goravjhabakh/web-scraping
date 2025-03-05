import os
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://arxiv.org/')

search_box = driver.find_element(By.NAME, 'query')
search_query = 'Deep Learning'

search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)

time.sleep(3) # Wait for results to load

papers = driver.find_elements(By.CLASS_NAME, 'arxiv-result')

with open('Src/Arxiv/arxiv_result.txt', 'w', encoding='utf-8') as f:
    for paper in papers[:5]:
        try:
            title = paper.find_element(By.CLASS_NAME, 'title').text.strip()
            id = paper.find_element(By.TAG_NAME, 'a').get_attribute('href').split('/')[-1]
            link = f"https://arxiv.org/pdf/{id}.pdf"

            response = requests.get(link, stream=True)
            if response.status_code == 200:
                path = f'Src/Arxiv/papers/{title}.pdf'
                with open(path, 'wb') as pdf_file:
                    pdf_file.write(response.content)
                    f.write(f"Title: {title}\n{link}\n{path}\n\n")
            else:
                f.write(f"Title: {title}\n{link}\nFailed to download\n\n")
            

        except Exception as e:
            f.write(f'Error: {e}')  

driver.close()