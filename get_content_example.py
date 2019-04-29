import csfg
from selenium import webdriver

# we will use the list from get_link_example.py (if you not yer run, run that file first)
# in this example we will scrape the html of text content from the given url list

drive_url = 'driver/chromedriver.exe'
driver = webdriver.Chrome(drive_url)
driver.implicitly_wait(30)

selector_title = '.post-title'      # custom the css selector for title
selector_content = '.entry-content'     # custom the css selector for content

with open('url_list.txt','r') as f:     # custom the list of url file
    for url in f:
        post_url = url.replace('\n','')
        try:
            csfg.get_content(driver,post_url,selector_title,selector_content)
            # here you have 3 option of function you can use
            ### csfg.get_content = will retrieve content in html style
            ### csfg.get_content_translate = will retrieve content translated to indonesian in html style
            #### if use tranlate, you must provide yandex api
            ### csfg.get_content_raw = will retrieve raw content, text only
        except:
            pass

driver.close()