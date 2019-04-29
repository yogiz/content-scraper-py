import csfg
from selenium import webdriver


# we will try to scrape list of post url in this demo theme page
# https://btemplates.com/2016/blogger-template-nordic/demo/

drive_url = 'driver/chromedriver.exe'
driver = webdriver.Chrome(drive_url)
driver.implicitly_wait(30)

driver.get('https://nordic-btemplates.blogspot.com/')
link_selector ='.entry-title a'     # in that page, the css selector of posts link like this

csfg.get_links(driver,link_selector)    # we can use custom filename, but this name just default

driver.close()  #dont forget close the driver after finish


# after you run, you will find the result in url_list.txt
# customize the link and link selector, to start scraping on your own
# you can use loop for scraping in many page
# now its yours