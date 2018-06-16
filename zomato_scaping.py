from selenium import webdriver
import csv

with open('Zomato.csv','w') as  restList:
    restList.write('RestaurantsName  , RestaurantsAddress  , RestaurantsCategory  \n')

driver = webdriver.Chrome("C://Users//UJJVAL RANA//chromedriver.exe")
driver.get("https://www.zomato.com/bhopal/restaurants?q=restaurants")

resto_names = driver.find_elements_by_css_selector("a.result-title.hover_feedback.zred.bold.ln24.fontsize0")
for x in resto_names:
    print(x.text)
resto_address= driver.find_elements_by_css_selector("div.col-m-16.search-result-address.grey-text.nowrap.ln22")
resto_category=driver.find_elements_by_css_selector("span.col-s-11.col-m-12.nowrap.pl0")
resto_cost=driver.find_elements_by_css_selector("span.col-s-11.col-m-12.pl0")
resto_timings=driver.find_elements_by_css_selector("div.col-s-11.col-m-12.pl0.search-grid-right-text")
# with open('Zomato.csv','a') as  restList:
#     for x in range(len(restaurants_list)):
#         restList.write(
#             restaurants_list[x].text + "," + restaurants_address[x].text + "," + restaurants_category[x].text + "\n")
#
#
#

