from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import config
import time
import random


comment_messages = [
    'Excellent work :)',
    'Awesome work!',
    'Good work. love it :)',
    'Very nice :)',
    'Nice work :)',
    'Superb work :)'
]


class BehanceBot():
    def __init__(self, email, password, driver_path):
        options = Options()
        options.headless = False
        self.browser = webdriver.Chrome(
            executable_path=driver_path,
            chrome_options=options
        )
        self.email = email
        self.password = password

    def home_page(self):
        self.browser.get('https://www.behance.net/')
        self.browser.maximize_window()
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
        time.sleep(15)

    def close_project_detail_page(self):
            close_button = self.browser.find_element_by_class_name('qa-overlay-close')
            close_button.click()

    def send_comments_on_projects(self):
        root_element_class = 'activity-layout'
        root_element = self.browser.find_element_by_class_name(root_element_class)
        if not root_element:
            return

        child_elements = root_element.find_elements_by_class_name('rf-project-cover__image')
        if not child_elements:
            return

        for child_element in child_elements:
            self.browser.execute_script('arguments[0].scrollIntoView(true);', child_element)
            time.sleep(1)
            child_element.click()
            time.sleep(3)
            # page_source = self.browser.page_source
            try:
                text_area = self.browser.find_element_by_xpath('//*[@id=\"comment\"]')
            except NoSuchElementException:
                text_area = None
            if not text_area:
                self.close_project_detail_page()
                time.sleep(3)
                continue

            try:
                self.browser.find_element_by_link_text('Raj Kumar')
                self.close_project_detail_page()
                time.sleep(3)
                continue
            except NoSuchElementException:
                pass

            message = random.choice(comment_messages)
            text_area.send_keys(message)
            time.sleep(2)

            submit_button = self.browser.find_element_by_class_name('js-submit')
            submit_button.click()
            time.sleep(3)

            self.close_project_detail_page()
            time.sleep(3)


def main():
    bot = BehanceBot(config.email, config.password, config.driver_path)
    bot.home_page()
    bot.sign_in()
    bot.send_comments_on_projects()

if __name__ == '__main__':
    main()
