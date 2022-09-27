from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

driver = webdriver.Firefox(executable_path='C:/Users/Administrador/Desktop/python/geckodriver') 

driver.get('https://www.adamchoi.co.uk/teamgoals/detailed')

all_matches_button = driver.find_element('xpath','//label[@analytics-event="All matches"]')
all_matches_button.click()


box = driver.find_element('class name','panel-body')
dropdown = Select(box.find_element('id' ,'country'))
dropdown.select_by_visible_text('Spain')

time.sleep(5)

matches = driver.find_elements('css selector' ,'tr')

all_matches = [match.text for match in matches]

driver.quit()

df = pd.DataFrame({'goals': all_matches})
print(df)
df.to_csv('matches.csv', index=False)
