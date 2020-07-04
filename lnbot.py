from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
random_time = lambda: (int(int(round(time.time()*10000))%10)/2)
import os

class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

    def closeBrowser(self):
        self.driver.close()

    def login_linkedin(self,Email_or_Phone,_Password):
        self.driver.get("https://www.linkedin.com")
        time.sleep(2)
        signin_button = self.driver.find_element_by_xpath("//a[contains(text(),'Sign in')]")
        signin_button.click()
        time.sleep(2)
        Email_or_Phone_text_box = self.driver.find_element_by_xpath("//input[@aria-label='Email or Phone']")
        Email_or_Phone_text_box.click()
        Email_or_Phone_text_box.send_keys(Email_or_Phone)
        password_text_box = self.driver.find_element_by_xpath("//input[@aria-label='Password']")
        password_text_box.click()
        password_text_box.send_keys(_Password)
        signin_button = self.driver.find_element_by_xpath("//button[contains(text(),'Sign in')]")
        signin_button.click()
        time.sleep(5)

visiting_bot = Bot()
visiting_bot.login_linkedin(os.getenv('EMAIL'),os.getenv('EMAIL_PASSWD'))
