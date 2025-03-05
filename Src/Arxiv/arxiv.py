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
        title = paper.find_element(By.CLASS_NAME, 'title').text.strip()
        authors = paper.find_element(By.CLASS_NAME, 'authors').text.strip()

        f.write(f"Title: {title}\n{authors}\n\n")

driver.close()