"""
Log into Facebook using selenium webdriver. Take a screenshot of the page after login
and save the image by the name "LoginFailed.png"
"""


from selenium import webdriver

driver = webdriver.Chrome()
driver.set_page_load_timeout(20)
driver.get("https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_id("email").send_keys("tejshree@abc.com")
driver.find_element_by_name("pass").send_keys("Tejshree")
driver.find_element_by_id("loginbutton").click()
driver.get_screenshot_as_file("LoginFailed.png")
driver.quit()
