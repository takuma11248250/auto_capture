from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import chromedriver_binary
import time
import os
import csv

#------------------ディレクトリ作成------------------
cur_dir = os.getcwd()
sitecapture_dir = os.getenv("USERPROFILE") + "\\Desktop\\" + "サイトキャプチャーフォルダ"
sitecapture_dir2 = os.getenv("USERPROFILE") + "\\OneDrive - 株式会社　ＬＩＦＵＬＬ　Ｍａｒｋｅｔｉｎｇ　Ｐａｒｔｎｅｒｓ\\デスクトップ\\" + "サイトキャプチャーフォルダ"
if os.path.isdir(os.getenv("USERPROFILE") + "\\Desktop") == True:
	os.makedirs(sitecapture_dir, exist_ok=True)
elif os.path.isdir(os.getenv("USERPROFILE") + "\\OneDrive - 株式会社　ＬＩＦＵＬＬ　Ｍａｒｋｅｔｉｎｇ　Ｐａｒｔｎｅｒｓ\\デスクトップ") == True:
	os.makedirs(sitecapture_dir2, exist_ok=True)
#------------------------------------------------
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

def get_capture():
	options = Options()
	options.add_argument('--headless')
	options.add_argument('--no-sandbox')
	options.add_argument('--disable-dev-shm-usage')
	driver = webdriver.Chrome(resource_path('./driver/chromedriver.exe'), chrome_options=options)

	url_list_file = open(cur_dir + "/utl_list.csv")
	reader = csv.reader(url_list_file)
	number = 0
	for url in reader:
		driver.get(url[0])
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
		time.sleep(10)
		page_width = driver.execute_script('return document.body.scrollWidth')
		page_height = driver.execute_script('return document.body.scrollHeight')
		driver.set_window_size(page_width, page_height)
		if os.path.isdir(sitecapture_dir) == True:
			driver.save_screenshot(sitecapture_dir + "\\" + str(number) + "_" + title  + ".jpg")
		elif os.path.isdir(sitecapture_dir2) == True:
			driver.save_screenshot(sitecapture_dir2 + "\\"+ str(number) + "_" + title + ".jpg")
		number += 1
get_capture()