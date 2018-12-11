import pandas as pd
from bs4 import BeautifulSoup as view
from splinter import Browser
import requests

def scrape():
    executable_path = {'executable_path': 'HW Instructions/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = view(html, 'html.parser')
    contentTitle = soup.find('div', class_="content_title").get_text()
    print(contentTitle) 
    contentTeaser = soup.find('div', class_="article_teaser_body").get_text()
    print(contentTeaser)
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)
    browser.find_by_id('full_image').click()
    browser.is_element_present_by_text('more_info', wait_time=1)
    browser.find_link_by_partial_text('more info').click()
    html2 = browser.html
    soup = view(html2, 'html.parser')
    mainImage = soup.find(class_='main_image')
    print(mainImage['src'])
    mainImageSRC = mainImage['src']
    fullImageURL = "https://www.jpl.nasa.gov/" + mainImageSRC
    print(fullImageURL)
    url3 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url3)
    html3 = browser.html
    soup = view(html3, 'html.parser')
    tweet = soup.find(class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").get_text()
    print(tweet)
    browser.quit()
    mars = {
        "contentTitle": contentTitle,
        "contentTeaser": contentTeaser,
        "mainImage": fullImageURL,
        "tweet": tweet
    }
    return(mars)