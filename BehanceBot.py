from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BehanceBot():
    def __init__(self, email, password):
        self.browser = webdriver.Chrome(executable_path='D:\chromedriver.exe')
        self.email = email
        self.password = password

    def home_page(self):
        self.browser.get('https://www.behance.net/')
        wait = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Sign In")))
        time.sleep(5)

    def sign_in(self):
        self.browser.find_element_by_link_text("Sign In").click()
        wait = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((By.ID, 'adobeid_username'))
        )
        user_name_input = self.browser.find_element_by_id('adobeid_username')
        user_name_input.send_keys(self.email)
        time.sleep(5)

        password_input = self.browser.find_element_by_name('password')
        password_input.click()
        time.sleep(2)
        password_input.clear()
        password_input.send_keys(self.password)
        time.sleep(2)
        password_input.send_keys(Keys.ENTER)
        time.sleep(1000)

    def send_comments_on_projects(self):
        pass


def main():
    bot = BehanceBot('', '')
    bot.home_page()
    bot.sign_in()

if __name__ == '__main__':
    main()
