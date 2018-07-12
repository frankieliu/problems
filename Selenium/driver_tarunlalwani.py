from selenium import webdriver

driver = webdriver.Chrome()
executor_url = driver.command_executor._url
session_id = driver.session_id
driver.get("http://tarunlalwani.com")

print(session_id)
print(executor_url)


driver2 = webdriver.Remote()
# command_executor=executor_url, desired_capabilities={})
driver2.session_id = session_id
print(driver2.current_url)
