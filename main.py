from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

PROXY_URL = "https://free-proxy-list.net/"

def startAttack():
	pass

def loadConfig():
	pass

def main():
	#init selinium
	driver = webdriver.Chrome('C:\\Users\\boton\OneDrive\\Desktop\\DDoS\\chromedriver')
	driver.get(PROXY_URL)
	proxies = driver.find_elements_by_xpath('//table[@class="table table-striped table-bordered"]')
	print(proxies)
	pass


if __name__ == '__main__':
	main()