
from selenium import webdriver
from selenium.webdriver import ActionChains
from tabulate import tabulate
import time

# Make sure to have the correct path 
PATH = "/Users/deepankarbhade/Dev/chromedriver"
driver = webdriver.Chrome(PATH)

# site to scrap
driver.get('https://www.forbes.com/real-time-billionaires/#48e869f63d78')

time.sleep(3)

print("\n---REAL-TIME BILLIONAIRES FORBES---\n")

tableData = []

# Lopping through the table row and appendig the data into a lsit
for x in range(1, 11):
  tempPath = f"/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div/section[4]/div[2]/div/div[4]/div[1]/table/tbody/tr[{x}]"
  tempSel =  driver.find_element_by_xpath(tempPath)
  data = ((tempSel.text).splitlines())

  tableData.append([data[0],data[1],data[2],data[5]])

# Formating the data with adding headers
print(tabulate(tableData,headers=['Rank', 'Name','Net Worth' ,'Company']))  

# closing the browser tab
driver.close()



