#web scaping -> Just dial
#sometime's geckodriver required. go to github page

from selenium import webdriver
import csv
import time

rating_dict ={"s10": 1,"s9": 0.9,"s8": 0.8, "s7": 0.7, "s6": 0.6, "s5": 0.5,  "s4": 0.4, "s3": 0.3, "s2": 0.2, "s1":0.1, "s0": 0.0}
digit_dict ={"dc": '+',
"fe": '(',
"ji": 9,
"yz": 1,
"hg": ')',
"ba": '-',
"rq": 5,
"wx": 2,
"po": 6,
"acb": 0,
"ts": 4,
"vu": 3,
"lk": 8,
"nm": 7
}


driver = webdriver.Chrome("C://Users//UJJVAL RANA//chromedriver.exe")
driver.get("https://www.justdial.com/Bhopal/Restaurants")

time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(22)


resto_list = driver.find_elements_by_class_name('store-name')
resto_address = driver.find_elements_by_css_selector('p.address-info.tme_adrssec')


# resto_category=[]
# for x in  range(len(resto_list)):
#         cat=driver.find_element_by_css_selector('p.address-info.adinfoex')
#
#resto_category = driver.find_elements_by_css_selector('p.address-info.adinfoex ')
resto_rating_votes = driver.find_elements_by_class_name('newrtings')
resto_ratings =[]
resto_contact= []


for x in resto_list:
    print(x.text)


for y in resto_address:
    print(y.text)

# for z in resto_category:
#     print(z.text)
print("size of rest names:" + str(len(resto_list)) +"size of res address " +str(len(resto_address))+ "  size of rest category:  ")

for r in range(0,len(resto_list)):
    score = 0
    for a in range(1, 6):
        resto_rating_head = driver.find_elements_by_xpath(
            '//*[@id="bcard{}"]/div[1]/section/div[1]/p[1]/a/span[1]/span[{}]'.format(r, a))

        for each in resto_rating_head:
            rate = each.get_attribute("class")
            score+= rating_dict[rate]
    resto_ratings.append(score)

for r in range(0,len(resto_list)):
    contact_number = ""
    for a in range(1, 17):
        resto_contact_head = driver.find_elements_by_xpath(
            '//*[@id="bcard{}"]/div[1]/section/div[1]/p[2]/span/a/b/span[{}]'.format(r,a))
        for each in resto_contact_head:
            digit = each.get_attribute("class")
            contact_number += str(digit_dict[(digit[14:])])
    resto_contact.append(contact_number)









# resto_list.append(driver.find_elements_by_class_name('store-name'))
# resto_address.append(driver.find_elements_by_css_selector('p.address-info.tme_adrssec'))
# resto_category.append(driver.find_elements_by_css_selector('p.address-info.adinfoex '))
# resto_rating_votes.append(driver.find_elements_by_class_name('newrtings'))

with open('JustDial.csv', 'w') as jd_info:
    for i in range(len(resto_list)):
        jd_info.write(resto_list[i].text.replace(","," ") + "," + resto_address[i].text.replace(","," ") +  "," + resto_rating_votes[i].text.replace(","," ") + "," +str(resto_ratings[i]).replace(","," ") + "," + str(resto_contact[i]).replace(","," ") +"\n",)

import pandas as pd
df =pd.read_csv('JustDial.csv', delimiter=',')
print(df)
# import  time
#
# driver.get('https://www.google.co.in/search?q=techsimplus&oq=techsimplus&aqs=chrome..69i57.22284j0j8&sourceid=chrome&ie=UTF-8')
#
# url_list = driver.find_elements_by_class_name('r')
#
# for url in url_list:
#     print(url.text)
#


# resto_list = driver.find_elements_by_class_name('store-name')
# resto_address = driver.find_elements_by_css_selector('p.address-info.tme_adrssec')
# resto_category = driver.find_elements_by_css_selector('p.address-info.adinfoex ')
# resto_rating_votes = driver.find_elements_by_class_name('newrtings')
#
#
# for x in resto_list:
#     print(x.text)
# #
# button_list = driver.find_elements_by_class_name('fl')
#
# for button in button_list:
#     # button.click()
#     print(button.text)
#    # url_list.append(driver.find_elements_by_class_name('r'))
