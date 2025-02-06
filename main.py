from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import time
import os
from dotenv import load_dotenv



load_dotenv()

similar_account = "nvidia"
INSTAGRAM_EMAIL = os.environ.get("EMAIL")
INSTAGRAM_PASSWORD = os.environ.get("PASSWORD")


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        # credentials
        try:
            accept_cookies = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Accept')]")
            accept_cookies.click()
            time.sleep(2)
        except NoSuchElementException:
            pass

        # enter username and password
        user_input = self.driver.find_element(By.NAME, "username")
        user_input.send_keys(INSTAGRAM_EMAIL)
        pass_input = self.driver.find_element(By.NAME, "password")
        pass_input.send_keys(INSTAGRAM_PASSWORD)

        # click login
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        time.sleep(5)

        # Dismiss Save your login info or Turn on Notifications
        try:
            not_now_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
            not_now_button.click()
            time.sleep(2)
        except NoSuchElementException:
            pass
        try:
            not_now_notification = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
            not_now_notification.click()
            time.sleep(2)
        except NoSuchElementException:
            pass

    # def find_followers(self):
    #     self.driver.get(f"https://www.instagram.com/{similar_account}/followers")
    #     time.sleep(3)
    #
    #     # Click on followers link
    #     followers_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "followers")
    #     followers_link.click()
    #
    #     time.sleep(2)
    #
    #     # Scroll the modal to load more
    #     modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
    #     modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
    #     for i in range(5):
    #         self.driver.execute_script(
    #             "arguments[0].scrollTop = arguments[0].scrollHeight", modal)
    #         time.sleep(2)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{similar_account}/followers")
        time.sleep(5)

        followers_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "followers")
        followers_link.click()
        followers_list = self.driver.find_element(By.XPATH, value="/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div/button")
        followers_list.click()
        time.sleep(3)
        dialog = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        for i in range (10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
            time.sleep(2)

    def follow(self):
        dialog = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        follow_buttons = dialog.find_elements(By.TAG_NAME, value='button')
        for element in follow_buttons:
            try:
                element.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, value='//button[contains(text(), "Cancel")]')
                cancel_button.click()
                time.sleep(1)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()