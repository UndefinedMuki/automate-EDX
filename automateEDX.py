#install selenium
#install geckodriver
#python v27

from selenium import webdriver
import time

def scroll():
	# Get scroll height
	last_height = browser.execute_script("return document.body.scrollHeight")
	
	while True:
		# Scroll down to bottom
		browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		
		# Wait to load page
		time.sleep(SCROLL_PAUSE_TIME)
		new_height = browser.execute_script("return document.body.scrollHeight")
		
		# Calculate new scroll height and compare with last scroll height
		if new_height == last_height:
			break
		last_height = new_height
		
SCROLL_PAUSE_TIME = 2

browser = webdriver.Firefox()
browser.get('https://www.edx.org/course?language=English')
scroll()