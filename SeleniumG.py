import time
from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome('D:\\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://feebee.com.tw/');
time.sleep(3) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('50吋電視')
search_box.submit()
time.sleep(2)
for page in range(1,10):
	driver.get(driver.current_url+"&page="+str(page))
	#print(driver.current_url)
	soup = BeautifulSoup(driver.page_source, 'html.parser')
	#print(soup)
	for span in soup.find_all('span',{"class": "pure-u items_container"}):
			print(span.find('h3',{"class": "large"}).get_text())
			if span.find('span',{"class": "price ellipsis xlarge"}) is not None:
				print(span.find('span',{"class": "price ellipsis xlarge"}).get_text())
			else:
				print(span.find('li',{"class": "price ellipsis xlarge"}).get_text())
	 # Let the user actually see something!
driver.quit()