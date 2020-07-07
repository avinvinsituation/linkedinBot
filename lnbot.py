import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def get_random_time():
    wait_time = int(int(round(time.time()*10000))%10/2)
    if wait_time:
        print(wait_time)
    return wait_time if wait_time else get_random_time()

class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

    def closeBrowser(self):
        self.driver.close()

    def login_linkedin(self,Email_or_Phone,_Password):
        self.driver.get("https://www.linkedin.com")
        time.sleep(get_random_time())
        signin_button = self.driver.find_element_by_xpath("//a[contains(text(),'Sign in')]")
        signin_button.click()
        time.sleep(get_random_time())
        Email_or_Phone_text_box = self.driver.find_element_by_xpath("//input[@aria-label='Email or Phone']")
        Email_or_Phone_text_box.click()
        Email_or_Phone_text_box.send_keys(Email_or_Phone)
        password_text_box = self.driver.find_element_by_xpath("//input[@aria-label='Password']")
        password_text_box.click()
        password_text_box.send_keys(_Password)
        signin_button = self.driver.find_element_by_xpath("//button[contains(text(),'Sign in')]")
        signin_button.click()
        time.sleep(get_random_time())

    def search_keyword(self,keywords):
        search_box = self.driver.find_element_by_xpath("//input[@placeholder='Search']")
        search_box.click()
        search_box.send_keys(keywords)
        search_box.send_keys(Keys.ENTER)
        time.sleep(get_random_time())

    def scroll_entire_page(self):
        body = self.driver.find_element_by_css_selector('body')
        for i in range(20):
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.1)
        body.send_keys(Keys.END)
        time.sleep(get_random_time())
        body.send_keys(Keys.HOME)
        """time.sleep(get_random_time())
        for i in range(20):
            body.send_keys(Keys.PAGE_UP)
            time.sleep(get_random_time())
        body.send_keys(Keys.HOME)
        time.sleep(get_random_time())"""

    def visit_every_search_result(self,number_of_pages_to_visit = 1):
        while(number_of_pages_to_visit >= 0):
            number_of_pages_to_visit -= 1
            self.open_profiles_in_new_tabs()
            self.visit_and_scroll_all_tabs()
            try:
                if number_of_pages_to_visit:
                    next_page_button = self.driver.find_element_by_xpath("//button[@aria-label='Next']")
                    next_page_button.click()
                else:
                    print("Search complete.")
            except Exception as e:
                if number_of_pages_to_visit>0:
                    print("Number of results are lesser than the number of pages.")
                print("Search Ended.")
                break

    def open_profiles_in_new_tabs(self):
        self.scroll_entire_page()
        result_items = []
        result_items = self.driver.find_elements_by_xpath("//figure[@class='search-result__image']")
        for profile in result_items:
            ActionChains(self.driver).key_down(Keys.CONTROL).click(profile).key_up(Keys.CONTROL).perform()
            time.sleep(get_random_time())

    def visit_and_scroll_all_tabs(self):
        result_window = self.driver.current_window_handle
        open_window_handles = self.driver.window_handles
        for window in open_window_handles:
            self.driver.switch_to.window(window)
            if self.driver.current_window_handle != result_window:
                self.scroll_entire_page()
                visiting_bot.closeBrowser()
        self.driver.switch_to.window(self.driver.window_handles[0])

visiting_bot = Bot()
visiting_bot.login_linkedin(os.getenv('EMAIL'),os.getenv('EMAIL_PASSWD'))
# visiting_bot.search_keyword("hiring")
# visiting_bot.visit_every_search_result()
