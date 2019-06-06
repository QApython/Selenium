from selenium import webdriver

driver= webdriver.Chrome(executable_path="D:/Python_Selenium/Drivers/chromedriver.exe")
driver.get ("https://facebook.com")

#driver.find_element_by_xpath("//input[@id='email']").sendkeys()
FirstName = driver.find_element_by_xpath("//input[@name= 'firstname']").send_keys("Jaya")
LastName = driver.find_element_by_xpath("//input[@name= 'lastname']").send_keys("Lakshmi")
Email = driver.find_element_by_xpath("//input[@name= 'reg_email__']").send_keys("kjaya2008@gmail.com")
NewPassword = driver.find_element_by_xpath("//input[@name= 'reg_passwd__']").send_keys("Dhoni1@csk")
Day = driver.find_element_by_xpath("//select[@id= 'day']").send_keys("17")
Month = driver.find_element_by_xpath("//select[@id= 'month']").send_keys("Apr")
Year = driver.find_element_by_xpath("//select[@id= 'year']").send_keys("1987")

Gender = driver.find_element_by_xpath("//input[@id= 'u_0_8']").click()
Submit = driver.find_element_by_xpath("//button[@name= 'websubmit']").click()