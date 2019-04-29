import re
from yandex_translate import YandexTranslate
import codecs

# Function for getting list of link in page
def get_links(driver,link_selector,filename='url_list.txt') :
    urls_post = driver.find_elements_by_css_selector(link_selector)
    with open(filename,'a') as f:
        for url in urls_post :
            item = url.get_attribute("href")
            f.write("%s\n" % item)

# remove tag link from string
def remove_tag_link(data):
    cari_tag = re.compile(r'<a.*?>|</a>')
    hasil = cari_tag.sub('',data)
    return hasil

#translate content to indonesia with yandex
def translate_id(content,api) :
    translate = YandexTranslate(api)
    hasil_translate = translate.translate(content, 'en-id')
    hasil_translate = str(hasil_translate['text'])
    hasil_translate = hasil_translate[2:-2]
    return hasil_translate

# convert raw html string to list for each paragraph
def html_tolist(html):
    html = html.replace('</p>','</p> |newline|')
    result = html.split('|newline|')
    return result

# Get content only in html
def get_content(driver, url, selector_title, selector_content):
    driver.get(url)
    title = driver.find_element_by_css_selector(selector_title)
    content = driver.find_element_by_css_selector(selector_content)
    text_title = title.text
    src_content = content.get_attribute('innerHTML')

    # proses content
    pure_content = remove_tag_link(src_content)
    pure_content = html_tolist(pure_content)

    # translating to indonesia and creating file
    filename = re.sub('[^\w\-_\. ]', '_', text_title) + '.txt'
    with codecs.open('results/' + filename, 'w', 'utf-8') as f:
        f.write(text_title + '\n')
        for kata in pure_content:
            f.write(kata + '\n')

# Get content only in html
def get_content_raw(driver, url, selector_title, selector_content):
    driver.get(url)
    title = driver.find_element_by_css_selector(selector_title)
    content = driver.find_element_by_css_selector(selector_content)
    text_title = title.text
    src_content = content.text

    # translating to indonesia and creating file
    filename = re.sub('[^\w\-_\. ]', '_', text_title) + '.txt'
    with open('results/' + filename, 'w') as f:
        f.write(text_title + '\n')
        f.write(src_content + '\n')

#   get content and translate it to indonesia using yandex
def get_content_translate(driver, url, selector_title, selector_content,yandex_api):
    driver.get(url)
    title = driver.find_element_by_css_selector(selector_title)
    content = driver.find_element_by_css_selector(selector_content)
    text_title = title.text
    src_content = content.get_attribute('innerHTML')

    # proses content
    pure_content = remove_tag_link(src_content)
    pure_content = html_tolist(pure_content)

    # translating to indonesia and creating file
    filename = re.sub('[^\w\-_\. ]', '_', text_title) + '.txt'
    with codecs.open('results/' + filename, 'w', 'utf-8') as f:
        try:
            text_title = translate_id(text_title, yandex_api)
        except:
            pass
        f.write(text_title + '\n')
        for kata in pure_content:
            try:
                kata = translate_id(kata, yandex_api)
            except:
                pass
            f.write(kata + '\n')
