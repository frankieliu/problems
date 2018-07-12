from selenium import webdriver
driver = webdriver.Chrome()
# driver.get('http://seleniumhq.org/')
print(driver.session_id)
print(driver.command_executor._url)
# sid = 0xe1b598488118529220136ec50a0881cd
# browser.session_id = sid
print(len(driver.window_handles))
