from selenium import webdriver
driver = webdriver.Remote(
    command_executor="http://127.0.0.1:39743")
driver.session_id = 0x06b402576939f6e791e2ddf549bdbcbc
# print(driver2.current_url)
print(len(driver2.window_handles))
print("done")
