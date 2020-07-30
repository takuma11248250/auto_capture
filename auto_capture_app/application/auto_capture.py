from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import chromedriver_binary
import time
import os

def get_capture(urls):
	urls = urls.split(",")
	options = Options()
	options.add_argument('--headless')
	driver = webdriver.Chrome(options=options)

	for url in urls:
	    driver.get(url)
	    time.sleep(10)
	    title = driver.title
	    if "|" in title:
	    	title = title.replace("|", "_")
	    elif "￥" in title:
	    	title = title.replace("￥", "_")
	    elif "/" in title:
	    	title = title.replace("/", "_")
	    elif ":" in title:
	    	title = title.replace(":", "_")
	    elif "*" in title:
	    	title = title.replace("*", "_")
	    elif "?" in title:
	    	title = title.replace("?", "_")
	    elif '"' in title:
	    	title = title.replace('"', "_")
	    elif '<' in title:
	    	title = title.replace('<', "_")
	    elif '>' in title:
	    	title = title.replace('>', "_")

	    page_width = driver.execute_script('return document.body.scrollWidth')
	    page_height = driver.execute_script('return document.body.scrollHeight')
	    driver.set_window_size(page_width, page_height)
	    driver.save_screenshot(os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") +"\\Desktop\\" + title + ".jpg")
	    if driver.save_screenshot(os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") +"\\Desktop\\" + title + ".jpg") == False:
	    	driver.save_screenshot(os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") +"\\OneDrive - 株式会社　ＬＩＦＵＬＬ　Ｍａｒｋｅｔｉｎｇ　Ｐａｒｔｎｅｒｓ\\デスクトップ\\" + title + ".jpg")