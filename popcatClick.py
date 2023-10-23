from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
# options.add_argument("--headless")              #不開啟實體瀏覽器背景執行
options.add_argument("--start-maximized")         #最大化視窗
options.add_argument("--incognito")               #開啟無痕模式
options.add_argument("--disable-popup-blocking")  #禁用彈出攔截
options.add_argument("--disable-notifications")   #取消通知

driver_path=ChromeDriverManager().install()
driver = webdriver.Chrome(
	options = options,
	service = Service(ChromeDriverManager().install())
)

driver.get('https://popcat.click/')
sleep(3)

ac = ActionChains(driver)
ac.move_by_offset(724, 289)
for i in range(50000):
	ac.click()

	# 設定一些休息時間
	if (i+1)%8 == 0:
		ac.pause(0.1)
	if (i+1)%45 == 0:
		ac.pause(0.2)
	if (i+1)%599 == 0:
		ac.pause(0.3)
ac.perform()

driver.quit()